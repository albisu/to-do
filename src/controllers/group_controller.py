class GroupController:
    def __init__(self):
        self.groups = []

    def create_group(self, name):
        new_group = {'name': name, 'tasks': [], 'subgroups': []}
        self.groups.append(new_group)
        return new_group

    def delete_group(self, name):
        self.groups = [group for group in self.groups if group['name'] != name]

    def get_groups(self):
        return self.groups

    def find_group(self, name):
        for group in self.groups:
            if group['name'] == name:
                return group
        return None

    def add_subgroup(self, parent_group_name, subgroup_name):
        parent_group = self.find_group(parent_group_name)
        if parent_group:
            new_subgroup = {'name': subgroup_name, 'tasks': [], 'subgroups': []}
            parent_group['subgroups'].append(new_subgroup)
            return new_subgroup
        return None

    def add_task_to_group(self, group_name, task):
        group = self.find_group(group_name)
        if group:
            group['tasks'].append(task)
            return task
        return None

    def remove_task_from_group(self, group_name, task):
        group = self.find_group(group_name)
        if group and task in group['tasks']:
            group['tasks'].remove(task)
            return task
        return None