# Priority Based Scheduling Simulator

This project is a Priority Based Scheduling Simulator built with Streamlit. It allows users to simulate the scheduling of tasks based on their arrival time, duration, and priority, and visualize the schedule using a Gantt chart.

## Features

- User-friendly interface for inputting task details.
- Options to set the number of tasks and priority type (higher priority or lower priority).
- Dynamic simulation of task scheduling.
- Visualization of the scheduling process using a Gantt chart.
- Display of simulation results, including start and end times for each task.

## Installation

To run this project, you need to have Python installed along with the required libraries. You can install the necessary libraries using the following command:

```bash
pip install streamlit matplotlib
```

## Usage

1. Clone this repository or download the `project.py` file.
2. Open a terminal and navigate to the directory containing `project.py`.
3. Run the Streamlit app with the following command:

```bash
streamlit run project.py
```

4. The Streamlit app will open in your default web browser. You can use the sidebar to input the number of tasks, priority type, and details for each task (arrival time, duration, and priority).
5. Click the "Run Simulation" button to simulate the scheduling and visualize the results.

## Configuration Options

- **Number of Tasks**: Set the total number of tasks to be scheduled.
- **Priority Type**: Choose between "higher" (larger numbers have higher priority) and "lower" (smaller numbers have higher priority).
- **Task Details**: For each task, input the arrival time, duration, and priority.

## Visualization

The Gantt chart provides a visual representation of the task scheduling process. Each task is represented by a horizontal bar, with the length of the bar corresponding to the task duration. Idle periods are also displayed

as bars to show when no tasks were scheduled.

## Example

Here is an example of how to use the simulator:

1. Set the number of tasks to 5.
2. Choose "higher" as the priority type.
3. Input the following task details:
   - Task 1: Arrival Time = 0, Duration = 3, Priority = 2
   - Task 2: Arrival Time = 1, Duration = 2, Priority = 1
   - Task 3: Arrival Time = 2, Duration = 1, Priority = 3
   - Task 4: Arrival Time = 3, Duration = 4, Priority = 2
   - Task 5: Arrival Time = 4, Duration = 2, Priority = 1

4. Click "Run Simulation".

The Gantt chart will display the scheduling of tasks, and the results section will show the start and end times for each task.

## Code Overview

- **Imports**: The necessary libraries are imported, including Streamlit, deque from collections, matplotlib for plotting, and datetime for time manipulation.
- **Streamlit Interface**: The Streamlit app interface is set up with options for user input in the sidebar.
- **Simulation Logic**: The core scheduling simulation logic is implemented, sorting tasks based on arrival time and priority, and managing a ready queue.
- **Visualization**: The Gantt chart is plotted using matplotlib and displayed in the Streamlit app.
- **Results Display**: The start and end times for each task are displayed in the app.
