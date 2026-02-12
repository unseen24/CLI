Commands

| Command | Arguments | Description | Example |
|---------|-----------|-------------|---------|
| `-add` | `[Task Name]` | Add a new task | `python task_tracker.py -add "Buy milk"` |
| `-update` | `[Task ID] [New Description]` | Update task description | `python task_tracker.py -update 1 "Buy milk and bread"` |
| `-delete` | `[Task ID]` | Delete a task | `python task_tracker.py -delete 1` |
| `-in-progress` | `[Task ID]` | Mark task as in progress | `python task_tracker.py -in-progress 1` |
| `-done` | `[Task ID]` | Mark task as done | `python task_tracker.py -done 1` |
| `-list-all` | None | List all tasks | `python task_tracker.py -list-all` |
| `-list-todo` | None | List tasks with "todo" status | `python task_tracker.py -list-todo` |
| `-list-done` | None | List completed tasks | `python task_tracker.py -list-done` |
| `-list-in-progress` | None | List tasks in progress | `python task_tracker.py -list-in-progress` |
