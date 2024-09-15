def generate_report(tasks):
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task['completed'])
    
    st.write(f"Total Tasks: {total_tasks}")
    st.write(f"Completed Tasks: {completed_tasks}")
    st.write(f"Completion Rate: {completed_tasks / total_tasks * 100}%")
