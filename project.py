import streamlit as st
from collections import deque
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

st.title('Priority Based Scheduling Simulator')

# Configuration options
num_tasks = st.sidebar.number_input('Number of Tasks', min_value=1, value=5, step=1)
priority_type = st.sidebar.radio('Priority type ("higher" means larger numbers are higher priority, and "Lower" means smaller numbers have higher priority)', ['higher', 'lower'])

tasks = []
for i in range(num_tasks):
    col1, col2, col3 = st.sidebar.columns(3)
    with col1:
        arrival = st.number_input(f'Arrival Time for Task {i+1}', value=i, step=1, key=f'arrival{i}')
    with col2:
        duration = st.number_input(f'Duration for Task {i+1}', min_value=1, value=1, step=1, key=f'duration{i}')
    with col3:
        priority = st.number_input(f'Priority for Task {i+1}', value=i, step=1, key=f'priority{i}')
    tasks.append((arrival, duration, priority, i))  # (arrival_time, duration, priority, task_id)

# button to run the simulation
run_simulation = st.sidebar.button('Run Simulation')

if run_simulation:
    tasks.sort()
    ready_queue = deque()
    current_time = 0
    finished_tasks = []
    task_periods = []

    # Simulation of the scheduler
    while tasks or ready_queue:
        if tasks and not ready_queue:
            next_arrival_time, _, _, _ = tasks[0]
            if next_arrival_time > current_time:
                task_periods.append((current_time, next_arrival_time, 'Idle'))
                current_time = next_arrival_time

        while tasks and tasks[0][0] <= current_time:
            task = tasks.pop(0)
            ready_queue.append(task)
        
        if ready_queue:
            # Sort based on priority
            if priority_type == 'higher':
                ready_queue = deque(sorted(list(ready_queue), key=lambda x: (-x[2], x[0])))
            else:
                ready_queue = deque(sorted(list(ready_queue), key=lambda x: (x[2], x[0])))

            current_task = ready_queue.popleft()
            start = current_time
            end = current_time + current_task[1]
            finished_tasks.append((current_task[3], start, end))
            task_periods.append((start, end, f'Task {current_task[3]+1}'))
            current_time += current_task[1]

    # Plotting the Gantt chart using matplotlib
    fig, ax = plt.subplots(figsize=(10, 5))
    yticks = []
    yticklabels = []
    
    for i, (start, end, label) in enumerate(task_periods):
        ax.barh(label, end-start, left=start, color='skyblue' if 'Idle' in label else 'lightgreen')
        yticks.append(label)
        yticklabels.append(label)

    ax.set_yticks(yticks)
    ax.set_yticklabels(yticklabels)
    ax.invert_yaxis()
    ax.set_xlabel('Time')
    ax.set_title('Gantt Chart of Task Scheduling')
    
    # Formatting time axis
    plt.tight_layout()
    st.pyplot(fig)

    # Display results
    st.header('Simulation Results:')
    for task_id, start, end in finished_tasks:
        st.write(f'Task {task_id + 1} starts at {start} and ends at {end}.')
