def validate_task_title(title):
    if not title or len(title) < 3:
        raise ValueError("Task title must be at least 3 characters long.")
    return True

def format_task_description(description):
    return description.strip() if description else "No description provided."

def validate_group_name(name):
    if not name or len(name) < 3:
        raise ValueError("Group name must be at least 3 characters long.")
    return True

def format_group_info(info):
    return info.strip() if info else "No additional info provided."