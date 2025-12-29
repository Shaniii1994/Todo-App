# Quickstart: Phase-I In-Memory Todo Console App

**Date**: 2025-12-29
**Feature**: 001-todo-console-app

## Running the Application

```bash
python todo.py
```

## User Guide

### Main Menu

```
=== Todo Application ===
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Toggle Complete
6. Exit
```

### Adding a Task

1. Select option 1
2. Enter task title when prompted
3. Task is added with auto-generated ID

### Viewing Tasks

1. Select option 2
2. All tasks display with ID, title, and completion status
3. Completed tasks show `[X]`, incomplete show `[ ]`

### Updating a Task

1. Select option 3
2. Enter the task ID to update
3. Enter the new title
4. Task title is updated

### Deleting a Task

1. Select option 4
2. Enter the task ID to delete
3. Confirm deletion when prompted
4. Task is removed from the list

### Toggling Completion

1. Select option 5
2. Enter the task ID
3. Completion status flips (complete ↔ incomplete)

### Exiting

1. Select option 6
2. Application terminates
3. **Note**: All tasks are lost (in-memory storage)

## Error Messages

| Situation | Message |
|-----------|---------|
| Invalid menu choice | "Invalid choice. Please enter a number between 1 and 6." |
| Task ID not found | "Task with ID X not found." |
| Empty task title | "Task title cannot be empty." |
| Invalid ID input | "Please enter a valid task ID number." |
| Delete cancellation | "Delete cancelled." |

## Example Session

```
=== Todo Application ===
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Toggle Complete
6. Exit
> 1
Enter task title: Buy groceries
Task added!

=== Todo Application ===
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Toggle Complete
6. Exit
> 1
Enter task title: Pay bills
Task added!

=== Todo Application ===
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Toggle Complete
6. Exit
> 2
Tasks:
[ ] 1. Buy groceries
[ ] 2. Pay bills

=== Todo Application ===
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Toggle Complete
6. Exit
> 5
Enter task ID: 1
Task marked as complete!

=== Todo Application ===
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Toggle Complete
6. Exit
> 2
Tasks:
[X] 1. Buy groceries
[ ] 2. Pay bills

=== Todo Application ===
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Toggle Complete
6. Exit
> 6
Goodbye!
```
