import pandas as pd
import os
from datetime import datetime

# Directory and file path
DIRECTORY = "data"
FILE_PATH = os.path.join(DIRECTORY, "tasks.csv")

# Load tasks from CSV
def load_tasks():
    if not os.path.exists(FILE_PATH):
        return pd.DataFrame(columns=["Name", "Priority", "Due", "Category", "Progress", "Recurrence", "Dependencies", "Tags"])
    return pd.read_csv(FILE_PATH)

# Save a new task to CSV
def save_task(task_data):
    tasks = load_tasks()
    new_task = pd.DataFrame([task_data])
    tasks = pd.concat([tasks, new_task], ignore_index=True)
    tasks.to_csv(FILE_PATH, index=False)

# Update an existing task
def update_task(task_name, updates):
    tasks = load_tasks()
    for key, value in updates.items():
        tasks.loc[tasks["Name"] == task_name, key] = value
    tasks.to_csv(FILE_PATH, index=False)

# Delete a task from the CSV file
def delete_task(task_name):
    tasks = load_tasks()
    tasks = tasks[tasks["Name"] != task_name]
    tasks.to_csv(FILE_PATH, index=False)
