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


