import json
from task import Task

class TaskManager:
    def __init__(self, storage_file):
        self.storage_file = storage_file
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.storage_file, 'r') as file:
                return [Task(**task) for task in json.load(file)]
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open(self.storage_file, 'w') as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def add_task(self, title, description, category, due_date, priority):
        task_id = len(self.tasks) + 1
        new_task = Task(task_id, title, description, category, due_date, priority)
        self.tasks.append(new_task)
        self.save_tasks()
        return new_task

    def get_tasks(self, category=None):
        if category:
            return [task for task in self.tasks if task.category == category]
        return self.tasks

    def mark_task_completed(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                task.status = "Выполнена"
                self.save_tasks()
                return task
        return None

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        self.save_tasks()

    def search_tasks(self, keyword=None, category=None, status=None):
        return [task for task in self.tasks if
                (not keyword or keyword.lower() in task.title.lower() or keyword.lower() in task.description.lower()) and
                (not category or category == task.category) and
                (not status or status == task.status)]