class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)

    def update_task(self, old_task, new_task):
        index = self.tasks.index(old_task) if old_task in self.tasks else -1
        if index != -1:
            self.tasks[index] = new_task

    def get_tasks(self):
        return self.tasks

    def clear_tasks(self):
        self.tasks.clear()