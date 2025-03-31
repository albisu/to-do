class TaskController:
    def __init__(self):
        self.tasks = []

    def create_task(self, title, description):
        task = {
            'title': title,
            'description': description,
            'status': 'pending'
        }
        self.tasks.append(task)
        return task

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            return self.tasks.pop(task_index)
        return None

    def update_task(self, task_index, title=None, description=None, status=None):
        if 0 <= task_index < len(self.tasks):
            if title is not None:
                self.tasks[task_index]['title'] = title
            if description is not None:
                self.tasks[task_index]['description'] = description
            if status is not None:
                self.tasks[task_index]['status'] = status
            return self.tasks[task_index]
        return None

    def get_tasks(self):
        return self.tasks[:]  # Return a copy of the task list