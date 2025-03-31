class Task:
    def __init__(self, title, description="", status="pending"):
        self.title = title
        self.description = description
        self.status = status

    def mark_completed(self):
        self.status = "completed"

    def mark_pending(self):
        self.status = "pending"

    def update_description(self, new_description):
        self.description = new_description

    def __repr__(self):
        return f"Task(title={self.title}, description={self.description}, status={self.status})"