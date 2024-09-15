from plyer import notification

def send_notification(task_name, due_date):
    notification.notify(
        title=f"Task Reminder: {task_name}",
        message=f"Due date: {due_date}",
        timeout=10
    )
