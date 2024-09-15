def add_category_tag(tasks, category, tag):
    for task in tasks:
        task['category'] = category
        task['tags'] = tag

def filter_by_category_tag(tasks, category_or_tag):
    return [task for task in tasks if task.get('category') == category_or_tag or category_or_tag in task.get('tags', [])]
