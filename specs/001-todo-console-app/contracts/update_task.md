# Contract: update_task

**Type**: Function
**Module**: todo.py

## Signature

```python
def update_task(tasks: List[Dict]) -> bool:
```

## Inputs

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `tasks` | List[Dict] | Yes | Current task list |

## Outputs

| Output | Type | Description |
|--------|------|-------------|
| success | bool | True if updated, False otherwise |

## Behavior

1. Prompt user for task ID
2. Find task with matching ID
3. If not found, print error and return False
4. Prompt user for new title
5. Validate title (not empty after strip)
6. Update task title
7. Return True

## Error Handling

| Error Condition | Handling |
|-----------------|----------|
| Task ID not found | Print error, return False |
| Empty title | Print error, keep original, return False |
| Invalid ID input | Print error, return False |

## Example

```python
tasks = [{"id": 1, "title": "Old title", "completed": False}]
success = update_task(tasks)
# If user enters ID 1 and "New title":
# tasks = [{"id": 1, "title": "New title", "completed": False}]
# success = True
```
