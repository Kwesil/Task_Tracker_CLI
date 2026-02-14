# 📝 Task Tracker CLI

A simple, lightweight command-line task management application built with Python. Track your tasks, mark them as complete, and stay organized—all from your terminal.

## ✨ Features

- ✅ Add tasks with descriptions
- 📋 List all tasks or filter by status (pending/completed)
- ✓ Mark tasks as complete
- 🗑️ Delete tasks
- 💾 Persistent storage using JSON
- 🎨 Clean, formatted output with visual indicators
- ⚡ Fast and lightweight

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher
- No external dependencies required! Uses only Python standard library.

### Installation

1. Download the `task_tracker.py` file
2. Make it executable (optional):
   ```bash
   chmod +x task_tracker.py
   ```

That's it! You're ready to start tracking tasks.

## 📖 Usage

### Basic Commands

```bash
python task_tracker.py <command> [arguments]
```

### Available Commands

| Command | Description | Example |
|---------|-------------|---------|
| `add <description>` | Add a new task | `python task_tracker.py add "Buy groceries"` |
| `list [status]` | List all tasks or filter by status | `python task_tracker.py list` |
| `complete <id>` | Mark a task as completed | `python task_tracker.py complete 1` |
| `delete <id>` | Delete a task | `python task_tracker.py delete 2` |
| `help` | Show help message | `python task_tracker.py help` |

### Examples

#### Adding Tasks

```bash
python task_tracker.py add "Buy groceries"
python task_tracker.py add "Write documentation"
python task_tracker.py add "Review pull requests"
```

**Output:**
```
✓ Task added: #1 - Buy groceries
```

#### Listing All Tasks

```bash
python task_tracker.py list
```

**Output:**
```
======================================================================
ID    Status       Description                              Created        
======================================================================
1     ○ pending    Buy groceries                            2026-02-09     
2     ○ pending    Write documentation                      2026-02-09     
3     ○ pending    Review pull requests                     2026-02-09     
======================================================================
```

#### Filtering Tasks by Status

List only pending tasks:
```bash
python task_tracker.py list pending
```

List only completed tasks:
```bash
python task_tracker.py list completed
```

#### Completing a Task

```bash
python task_tracker.py complete 1
```

**Output:**
```
✓ Task #1 marked as completed: Buy groceries
```

#### Deleting a Task

```bash
python task_tracker.py delete 2
```

**Output:**
```
✓ Task #2 deleted: Write documentation
```

## 🗂️ Data Storage

Tasks are stored in a `tasks.json` file in the same directory as the script. The file is created automatically when you add your first task.

### Task Structure

Each task is stored with the following information:

```json
{
  "id": 1,
  "description": "Buy groceries",
  "status": "pending",
  "created_at": "2026-02-09T10:30:00",
  "completed_at": null
}
```

## 🎯 Use Cases

- **Daily Task Management**: Keep track of your daily to-dos
- **Project Planning**: Manage small project tasks
- **Quick Reminders**: Add quick tasks without leaving the terminal
- **Development Workflow**: Track bugs, features, and code review tasks
- **Learning Tool**: Simple codebase for learning CLI development in Python

## 🛠️ Technical Details

### Architecture

The application follows a simple object-oriented design:

- **TaskTracker Class**: Manages all task operations (add, list, complete, delete)
- **JSON Storage**: Persistent data storage using Python's built-in `json` module
- **CLI Interface**: Command-line argument parsing using `sys.argv`

### Code Structure

```
task_tracker.py
├── TaskTracker class
│   ├── __init__()          # Initialize and load tasks
│   ├── load_tasks()        # Load tasks from JSON
│   ├── save_tasks()        # Save tasks to JSON
│   ├── add_task()          # Add a new task
│   ├── list_tasks()        # Display tasks
│   ├── complete_task()     # Mark task as complete
│   └── delete_task()       # Remove a task
├── print_help()            # Display help message
└── main()                  # CLI entry point
```

## 🧪 Testing

Run the included demo script to see all features in action:

```bash
python demo.py
```

This will demonstrate:
- Adding multiple tasks
- Listing all tasks
- Completing tasks
- Filtering by status
- Deleting tasks

## 🤝 Contributing

Feel free to fork this project and add your own features! Some ideas:

- [ ] Task priorities (high, medium, low)
- [ ] Due dates and reminders
- [ ] Task categories/tags
- [ ] Edit task descriptions
- [ ] Search functionality
- [ ] Task notes/comments
- [ ] Export to CSV or other formats
- [ ] Colorized output
- [ ] Progress statistics

## 📝 License

This project is open source and available for anyone to use and modify.

## 🙋 Support

If you encounter any issues or have questions:

1. Check the help command: `python task_tracker.py help`
2. Make sure you're using Python 3.6+
3. Verify the `tasks.json` file isn't corrupted

## 🎓 Learning Resources

This project demonstrates:

- Python classes and object-oriented programming
- File I/O operations
- JSON data handling
- Command-line argument parsing
- Error handling
- Working with dates and timestamps

Perfect for beginners learning Python CLI development!

---

**Happy Task Tracking! 🚀**

Made with ❤️ using Python