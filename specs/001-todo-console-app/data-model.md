# Data Model: Phase-I In-Memory Todo Console App

**Date**: 2025-12-29
**Feature**: 001-todo-console-app

## Entity: Task

Represents a single todo item in the system.

### Attributes

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| `id` | int | > 0, unique, auto-increment | Unique identifier for the task |
| `title` | str | 1-200 chars after strip | Task description |
| `completed` | bool | default: False | Completion status |

### Validation Rules

1. **ID Validation**
   - Must exist in the tasks list
   - Must be a positive integer
   - Cannot be modified after creation

2. **Title Validation**
   - Cannot be empty or whitespace-only
   - Leading/trailing whitespace is stripped before storage
   - Maximum length: 200 characters (reasonable console display limit)

3. **Completed Validation**
   - Boolean value only (True/False)
   - Default: False for new tasks

### State Transitions

```
            +-------+
            | New   |
            +-------+
               |
               v
         +-----------+
         | Incomplete| <-------+
         +-----------+          |
              |                 | Toggle
              | Toggle          | (set to False)
              v                 |
         +-----------+          |
         | Complete  | --------+
         +-----------+
```

### Operations Affecting State

| Operation | ID Change | Title Change | Completed Change |
|-----------|-----------|--------------|------------------|
| Add | Assigned new ID | Set from input | False |
| Update | Unchanged | Updated | Unchanged |
| Delete | Removed | N/A | N/A |
| Toggle | Unchanged | Unchanged | Flipped |

## State Management

### Global State

```python
tasks: List[Dict[str, Any]] = []      # Storage: list of task dictionaries
next_task_id: int = 1                 # ID counter for new tasks
```

### State Invariants

1. All task IDs in `tasks` are unique
2. `next_task_id` equals `max(task["id"] for task in tasks) + 1` or 1 if empty
3. All tasks have the same key structure

## Data Examples

### Empty State

```python
tasks = []
next_task_id = 1
```

### Single Task

```python
tasks = [
    {
        "id": 1,
        "title": "Buy groceries",
        "completed": False
    }
]
next_task_id = 2
```

### Multiple Tasks

```python
tasks = [
    {"id": 1, "title": "Buy groceries", "completed": False},
    {"id": 2, "title": "Pay bills", "completed": True},
    {"id": 3, "title": "Walk the dog", "completed": False}
]
next_task_id = 4
```
