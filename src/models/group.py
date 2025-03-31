class Group:
    def __init__(self, name):
        self.name = name
        self.tasks = {}  # Dictionary to store tasks and their states
        self.subgroups = []  # List of sub-groups in this group

    def add_task(self, task_name):
        self.tasks[task_name] = "TO-DO"  # Default state is TO-DO

    def toggle_task_state(self, task_name):
        if task_name in self.tasks:
            self.tasks[task_name] = "DONE" if self.tasks[task_name] == "TO-DO" else "TO-DO"

    def add_subgroup(self, subgroup_name):
        subgroup = Group(subgroup_name)
        self.subgroups.append(subgroup)
        return subgroup