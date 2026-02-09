"""
Docstring for backend_projects.task_tracker_cli.app
-> Plan
--> Step 1: Create a simple task tracker that can add, list, and mark tasks as complete. Store the tasks in a JSON file.


"""

import json
import os
import sys
from datetime import datetime

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

