from tkinter import ttk, simpledialog, messagebox
from ttkthemes import ThemedStyle
from models.group import Group
import tkinter as tk
import json
import os


class AppWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("To-Do List")
        self.root.geometry("800x600")

        # Set the dark theme for ttk widgets
        style = ttk.Style(self.root)
        style.theme_use("clam")  # Use the "clam" theme
        style.configure("Treeview", background="#2e2e2e", foreground="white", fieldbackground="#2e2e2e")
        style.configure("TButton", background="#444444", foreground="white")
        style.configure("TLabel", background="#2e2e2e", foreground="white")
        style.configure("TFrame", background="#2e2e2e")
        style.configure("TScrollbar", background="#444444")

        # Set the main window background
        self.root.configure(bg="#2e2e2e")

        # Data structure to hold groups
        self.groups = []

        # Create a Treeview for groups and sub-groups
        self.tree_frame = ttk.Frame(self.root)
        self.tree_frame.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10, expand=True)

        self.tree_label = ttk.Label(self.tree_frame, text="Groups and Sub-Groups")
        self.tree_label.pack()

        self.tree = ttk.Treeview(self.tree_frame, show="tree")
        self.tree.pack(fill=tk.BOTH, expand=True)
        self.tree.bind("<<TreeviewSelect>>", self.display_group_details)

        self.tree_scrollbar = ttk.Scrollbar(self.tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.tree_scrollbar.set)
        self.tree_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.add_group_button = ttk.Button(self.tree_frame, text="Add Group", command=self.add_group)
        self.add_group_button.pack(pady=5)

        self.add_subgroup_button = ttk.Button(self.tree_frame, text="Add Sub-Group", command=self.add_subgroup)
        self.add_subgroup_button.pack(pady=5)

        self.delete_group_button = ttk.Button(self.tree_frame, text="Delete Selected", command=self.delete_selected_group)
        self.delete_group_button.pack(pady=5)

        # Create a frame for tasks
        self.task_frame = ttk.Frame(self.root)
        self.task_frame.pack(side=tk.RIGHT, fill=tk.BOTH, padx=10, pady=10, expand=True)

        self.task_label = ttk.Label(self.task_frame, text="Tasks")
        self.task_label.pack()

        self.task_listbox = tk.Listbox(
            self.task_frame,
            bg="#2e2e2e",  # Dark background
            fg="white",    # White text
            selectbackground="#444444",  # Highlight color
            selectforeground="white"     # Highlighted text color
        )
        self.task_listbox.pack(fill=tk.BOTH, expand=True)

        self.add_task_button = ttk.Button(self.task_frame, text="Add Task", command=self.add_task)
        self.add_task_button.pack(pady=5)

        self.delete_task_button = ttk.Button(self.task_frame, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack(pady=5)

        self.toggle_task_button = ttk.Button(self.task_frame, text="Toggle Task State", command=self.toggle_task_state)
        self.toggle_task_button.pack(pady=5)

        self.selected_group = None  # Currently selected group or sub-group

        # Load saved data
        self.load_data()

    def add_group(self):
        group_name = simpledialog.askstring("New Group", "Enter group name:")
        if group_name:
            group = Group(group_name)
            self.groups.append(group)
            self.tree.insert("", tk.END, group.name, text=group.name)
            self.save_data()

    def add_subgroup(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("No Group Selected", "Please select a group to add a sub-group.")
            return

        parent_group_name = self.tree.item(selected_item, "text")
        parent_group = self.find_group_by_name(parent_group_name)

        if parent_group:
            subgroup_name = simpledialog.askstring("New Sub-Group", "Enter sub-group name:")
            if subgroup_name:
                subgroup = parent_group.add_subgroup(subgroup_name)
                self.tree.insert(selected_item, tk.END, subgroup.name, text=subgroup.name)
                self.save_data()

    def delete_selected_group(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("No Group Selected", "Please select a group or sub-group to delete.")
            return

        group_name = self.tree.item(selected_item, "text")
        self.delete_group_by_name(group_name)
        self.tree.delete(selected_item)
        self.task_listbox.delete(0, tk.END)
        self.save_data()

    def add_task(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("No Group Selected", "Please select a group or sub-group first.")
            return

        group_name = self.tree.item(selected_item, "text")
        self.selected_group = self.find_group_by_name(group_name)

        if not self.selected_group:
            messagebox.showerror("Error", "Could not find the selected group or sub-group.")
            return

        task_name = simpledialog.askstring("New Task", "Enter task name:")
        if task_name:
            self.selected_group.add_task(task_name)
            self.display_group_details()
            self.save_data()

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if not selected_task_index:
            messagebox.showwarning("No Task Selected", "Please select a task to delete.")
            return

        selected_task = self.task_listbox.get(selected_task_index)
        task_name = selected_task.split(" [")[0]

        if self.selected_group and task_name in self.selected_group.tasks:
            del self.selected_group.tasks[task_name]
            self.display_group_details()
            self.save_data()

    def toggle_task_state(self):
        selected_task_index = self.task_listbox.curselection()
        if not selected_task_index:
            messagebox.showwarning("No Task Selected", "Please select a task to toggle its state.")
            return

        selected_task = self.task_listbox.get(selected_task_index)
        task_name = selected_task.split(" [")[0]

        if self.selected_group and task_name in self.selected_group.tasks:
            self.selected_group.toggle_task_state(task_name)
            self.display_group_details()
            self.save_data()

    def display_group_details(self, event=None):
        self.task_listbox.delete(0, tk.END)

        selected_item = self.tree.selection()
        if not selected_item:
            self.selected_group = None
            return

        group_name = self.tree.item(selected_item, "text")
        self.selected_group = self.find_group_by_name(group_name)

        if self.selected_group:
            for task, state in self.selected_group.tasks.items():
                self.task_listbox.insert(tk.END, f"{task} [{state}]")

    def find_group_by_name(self, name):
        def recursive_search(groups):
            for group in groups:
                if group.name == name:
                    return group
                result = recursive_search(group.subgroups)
                if result:
                    return result
            return None

        return recursive_search(self.groups)

    def delete_group_by_name(self, name):
        def recursive_delete(groups):
            for group in groups:
                if group.name == name:
                    groups.remove(group)
                    return True
                if recursive_delete(group.subgroups):
                    return True
            return False

        recursive_delete(self.groups)

    def save_data(self):
        data = [{"name": group.name, "tasks": group.tasks, "subgroups": self.serialize_subgroups(group.subgroups)} for group in self.groups]
        with open("to_do_data.json", "w") as file:
            json.dump(data, file)

    def load_data(self):
        if not os.path.exists("to_do_data.json"):
            return

        with open("to_do_data.json", "r") as file:
            data = json.load(file)

        for group_data in data:
            group = Group(group_data["name"])
            group.tasks = group_data["tasks"]
            group.subgroups = self.deserialize_subgroups(group_data["subgroups"])
            self.groups.append(group)
            self.tree.insert("", tk.END, group.name, text=group.name)
            self.load_subgroups(group, group.name)

    def load_subgroups(self, group, parent_id):
        for subgroup in group.subgroups:
            subgroup_id = self.tree.insert(parent_id, tk.END, subgroup.name, text=subgroup.name)
            self.load_subgroups(subgroup, subgroup_id)

    def serialize_subgroups(self, subgroups):
        return [{"name": sg.name, "tasks": sg.tasks, "subgroups": self.serialize_subgroups(sg.subgroups)} for sg in subgroups]

    def deserialize_subgroups(self, subgroups_data):
        subgroups = []
        for sg_data in subgroups_data:
            subgroup = Group(sg_data["name"])
            subgroup.tasks = sg_data["tasks"]
            subgroup.subgroups = self.deserialize_subgroups(sg_data["subgroups"])
            subgroups.append(subgroup)
        return subgroups

    def run(self):
        self.root.mainloop()