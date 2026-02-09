"""
Docstring for backend_projects.task_tracker_cli.app
-> Plan
--> Step 1: Create a simple task tracker that can add, list, and mark tasks as complete. Store the tasks in a JSON file.


"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path

class TaskTracker:
    # Initialization
    def __init__(self, data_file="tasks.json"):
        self.data_file = data_file
        self.tasks = self.load_tasks()


    # Loading tasks
    def load_tasks(self):
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return []
        return []

    # Saving tasks
    def save_tasks(self):
        with open(self.data_file, 'w') as f:
            json.dump(self.tasks, f, indent=2) # indent=2 is used for readable formatting

    # Adding tasks
    def add_task(self, description):
        task = {
            'id': len(self.tasks) + 1,
            'description': description,
            'status': 'pending',
            'created at': datetime.nowo().isoformat(),
            'completed at': None
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"✓ Task added: #{task['id']} - {description}")

    # Listing tasks
    def list_tasks(self, filter_status=None):
        if not self.tasks:
            print("No tasks found. Add one with: task add <description>")
            return
        # Filter tasks if status is specified
        tasks_to_show = self.tasks
        if filter_status:
            tasks_to_show = [t for t in self.tasks if t['status'] == filter_status]
        if not tasks_to_show:
            print(f"No {filter_status} tasks found.")
            return
        
        # Display header
        print("\n" + "=" * 70)
        print(f"{'ID':<5} {'Status':<12} {'Description':<40} {'Created':<15}")
        print("=" * 70)

        # Display tasks
        for task in tasks_to_show:
            status_symbol = "✓" if task['status'] == 'completed' else 'o'
            created = datetime.fromisoformat(task['created_at']).strftime('%Y-%m-%d')
            
            print(f"{task['id']:<5} {status_symbol} {task['status']:<10} {task['description']:<40} {created:<15}")
        print("=" * 70 + "\n")

    # Completing tasks
    def complete_task(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                task['status'] = 'completed'
                task['completed_at'] = datetime.now().isoformat()
                self.save_tasks()

    # Deleting tasks
    def delete_task(self, task_id):
        for i, task in enumerate(self.tasks):
            if task['id'] == task_id:
                deleted_task = self.tasks.pop(i)
                self.save_tasks()

def print_help():
    """Print usage instructions"""
    help_text = """
Task Tracker CLI - Simple task management from the command line

USAGE:
    python task_tracker.py <command> [arguments]

COMMANDS:
        add <description>       Add a new task
        list [status]           List all tasks (optional: pending/completed)
        complete <id>           Mark a task as completed
        delete <id>             Delete a task
        help                    Sshow this help message

EXAMPLES:
        python task_tracker.py add "Buy groceries"
        python task_tracker.py list
        python task_tracker.py list pending
        python task_tracker.py complete 1
        python task_tracker.py delete 2
"""
    print(help_text)

# Command-line interface
def main():
    """Main entry point for the CLI"""
    tracker = TaskTracker()

    # Check if any command was provided
    if len(sys.argv) < 2:
        print("Error: No command provided.")
        print_help()
        sys.exit(1)

    command = sys.argv[1].lower()

    # Handle different commands
    if command == "add":
        if len(sys.argv) < 3:
            print("Erroor: Please provide a task description.")
            print("Usage: python task_tracker.py add <description>")
            sys.exit(1)

        # Join all arguments after "add" as the description
        description = " ".join(sys.argv[2:])
        tracker.add_task(description)

    elif command == "list":
        # optional filter by status
        filter_status = sys.argv[2].lower() if len(sys.argv) > 2 else None
        if filter_status and filter_status not in ['pen  ding', 'completed']:
            print(f"Error: Invalid status '{filter_status}'. Use 'pending' or 'completed'.")
            sys.exit(1)
        tracker.list_tasks(filter_status)

    elif command == "complete":
        if len(sys.argv) < 3:
            print("Error: Please provide a task ID.")
            print("Usage: python task_tracker.py complete <id>")
            sys.exit(1)
        
        try:
            task_id = int(sys.argv[2])
            tracker.complete_task(task_id)
        except ValueError:
            print("Error: Task ID must be a number.")
            sys.exit(1)

    elif command == "delete":
        if len(sys.argv) < 3:
            print("Error: Please provide a task ID.")
            print("Usage: python task_tracker.py delete <id>")
            sys.exit(1)
        try: 
            task_id = int(sys.argv[2])
            tracker.delete_task(task_id)
        except ValueError:
            print("Error: task ID must be a number.")
            sys.exit(1)

    elif command == "help":
        print_help()
    
    else:
        print(f"Error: unknown command '{command}'.")
        print_help()
        sys.exit(1)

    

if __name__ == "__main__":
    main()