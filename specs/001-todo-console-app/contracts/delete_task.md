# Contract: delete_task

**Type**: Function
**Module**: todo.py

## Signature

```python
def delete_task(tasks: List[Dict]) -> bool:
```

## Inputs

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `tasks` | List[Dict] | Yes | Current task list (modified in place) |

## Outputs

| Output | Type | Description |
|--------|------|-------------|
| success | bool | True if deleted, False otherwise |

## Behavior

1. Prompt user for task ID
2. Find task with matching ID
3. If not found, print error and return False
4. Confirm deletion with user (yes/no)
5. If confirmed, remove task from list
6. Return True if deleted, False if cancelled

## Error Handling

| Error Condition | Handling |
|-----------------|----------|
| Task ID not found | Print error, return False |
| User cancels confirmation | Print "Delete cancelled.", return False |
| Invalid ID input | Print error, return False |

## Example

```python
tasks = [
    {"id": 1, "title": "Task 1", "completed": False},
    {"id": 2, "title": "Task 2", "completed": False}
]
success = delete_task(tasks)
# If user enters ID 1 and confirms "y":
# tasks = [{"id": 2, "title": "Task 2", "completed": False}]
# success = True
```
