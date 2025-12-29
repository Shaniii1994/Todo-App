# Contract: toggle_task

**Type**: Function
**Module**: todo.py

## Signature

```python
def toggle_task(tasks: List[Dict]) -> bool:
```

## Inputs

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `tasks` | List[Dict] | Yes | Current task list |

## Outputs

| Output | Type | Description |
|--------|------|-------------|
| success | bool | True if toggled, False otherwise |

## Behavior

1. Prompt user for task ID
2. Find task with matching ID
3. If not found, print error and return False
4. Flip task["completed"] (True → False, False → True)
5. Print confirmation message
6. Return True

## Error Handling

| Error Condition | Handling |
|-----------------|----------|
| Task ID not found | Print error, return False |
| Invalid ID input | Print error, return False |

## Example

```python
tasks = [{"id": 1, "title": "Task", "completed": False}]
success = toggle_task(tasks)
# tasks = [{"id": 1, "title": "Task", "completed": True}]
# success = True
```
