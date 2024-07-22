import os
import json
from datetime import datetime

TASKS_FILE = 'tasks.json'

class TaskManager:
    def __init__(self):
        """Initialize the TaskManager and load tasks from file."""
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        """Load tasks from a JSON file if it exists."""
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, 'r') as file:
                self.tasks = json.load(file)
        else:
            print("No tasks file found. Starting with an empty task list.")

    def save_tasks(self):
        """Save the current tasks to a JSON file."""
        with open(TASKS_FILE, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, description, priority, due_date):
        """Add a new task with a description, priority, and due date."""
        try:
            task = {
                'id': len(self.tasks) + 1,
                'description': description,
                'priority': priority,
                'due_date': due_date,
                'completed': False,
                'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            self.tasks.append(task)
            self.save_tasks()
            print(f"Task added: '{description}' with priority '{priority}' and due date '{due_date}'.")
        except Exception as e:
            print(f"Failed to add task: {e}")

    def list_tasks(self):
        """List all tasks with their details."""
        if not self.tasks:
            print("No tasks found. Your task list is empty.")
            return
        for task in self.tasks:
            status = "✔" if task['completed'] else "✘"
            print(f"[{status}] Task ID: {task['id']}\n"
                  f"Description: {task['description']}\n"
                  f"Priority: {task['priority']}\n"
                  f"Due Date: {task['due_date']}\n"
                  f"Created At: {task['created_at']}\n")

    def mark_task_completed(self, task_id):
        """Mark a task as completed by its ID."""
        try:
            for task in self.tasks:
                if task['id'] == task_id:
                    task['completed'] = True
                    self.save_tasks()
                    print(f"Task ID {task_id} marked as completed.")
                    return
            print(f"Task ID {task_id} not found.")
        except Exception as e:
            print(f"Failed to mark task as completed: {e}")

    def delete_task(self, task_id):
        """Delete a task by its ID."""
        try:
            self.tasks = [task for task in self.tasks if task['id'] != task_id]
            self.save_tasks()
            print(f"Task ID {task_id} deleted.")
        except Exception as e:
            print(f"Failed to delete task: {e}")

    def search_tasks(self, keyword):
        """Search for tasks containing a specific keyword."""
        try:
            found_tasks = [task for task in self.tasks if keyword.lower() in task['description'].lower()]
            if not found_tasks:
                print(f"No tasks found containing '{keyword}'.")
            else:
                for task in found_tasks:
                    status = "✔" if task['completed'] else "✘"
                    print(f"[{status}] Task ID: {task['id']}\n"
                          f"Description: {task['description']}\n"
                          f"Priority: {task['priority']}\n"
                          f"Due Date: {task['due_date']}\n"
                          f"Created At: {task['created_at']}\n")
        except Exception as e:
            print(f"Failed to search tasks: {e}")

    def edit_task(self, task_id, description=None, priority=None, due_date=None):
        """Edit an existing task by its ID."""
        try:
            for task in self.tasks:
                if task['id'] == task_id:
                    if description:
                        task['description'] = description
                    if priority:
                        task['priority'] = priority
                    if due_date:
                        task['due_date'] = due_date
                    self.save_tasks()
                    print(f"Task ID {task_id} updated.")
                    return
            print(f"Task ID {task_id} not found.")
        except Exception as e:
            print(f"Failed to edit task: {e}")

def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Manager\n")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Search Tasks")
        print("6. Edit Task")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            priority = input("Enter task priority (High/Medium/Low): ")
            due_date = input("Enter task due date (YYYY-MM-DD): ")
            task_manager.add_task(description, priority, due_date)
        elif choice == '2':
            task_manager.list_tasks()
        elif choice == '3':
            task_id = int(input("Enter task ID to mark as completed: "))
            task_manager.mark_task_completed(task_id)
        elif choice == '4':
            task_id = int(input("Enter task ID to delete: "))
            task_manager.delete_task(task_id)
        elif choice == '5':
            keyword = input("Enter keyword to search tasks: ")
            task_manager.search_tasks(keyword)
        elif choice == '6':
            task_id = int(input("Enter task ID to edit: "))
            description = input("Enter new description (leave blank to keep current): ")
            priority = input("Enter new priority (leave blank to keep current): ")
            due_date = input("Enter new due date (leave blank to keep current): ")
            task_manager.edit_task(task_id, description, priority, due_date)
        elif choice == '7':
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
