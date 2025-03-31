class GroupList:
    def __init__(self):
        self.groups = []

    def create_group(self, name):
        group = {'name': name, 'tasks': [], 'subgroups': []}
        self.groups.append(group)

    def delete_group(self, name):
        self.groups = [group for group in self.groups if group['name'] != name]

    def navigate_to_group(self, name):
        for group in self.groups:
            if group['name'] == name:
                return group
        return None

    def get_groups(self):
        return self.groups