def track_achievements(tasks):
    completed_tasks = sum(1 for task in tasks if task['completed'])
    
    if completed_tasks > 10:
        st.write("Achievement Unlocked: Task Master")
    elif completed_tasks > 20:
        st.write("Achievement Unlocked: Productivity King")
