from datetime import datetime, timedelta

def handle_recurring_tasks(tasks):
    today = datetime.now().strftime('%Y-%m-%d')
    updated_tasks = []

    for task in tasks:
        due_date = datetime.strptime(task['due_date'], '%Y-%m-%d')
        if task['recurring'] == "Daily" and due_date < datetime.now():
            task['due_date'] = (due_date + timedelta(days=1)).strftime('%Y-%m-%d')
        elif task['recurring'] == "Weekly" and due_date < datetime.now():
            task['due_date'] = (due_date + timedelta(weeks=1)).strftime('%Y-%m-%d')
        elif task['recurring'] == "Monthly" and due_date < datetime.now():
            task['due_date'] = (due_date + timedelta(days=30)).strftime('%Y-%m-%d')

        updated_tasks.append(task)

    return updated_tasks
