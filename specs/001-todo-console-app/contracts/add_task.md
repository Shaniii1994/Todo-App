# Contract: add_task

**Type**: Function
**Module**: todo.py

## Signature

```python
def add_task(tasks: List[Dict], next_id: int) -> Tuple[Dict, int]:
```

## Inputs

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `tasks` | List[Dict] | Yes | Current task list (modified in place) |
| `next_id` | int | Yes | Next available ID for new task |

## Outputs

| Output | Type | Description |
|--------|------|-------------|
| (task, next_id+1) | Tuple | Created task dict and incremented ID |
| tasks modified in-place | List[Dict] | New task appended to list |

## Behavior

1. Prompt user for task title via `input()`
2. Strip whitespace from title
3. Validate title is not empty
4. Create task dict with new ID and title
5. Append to tasks list
6. Return (task, next_id + 1)

## Error Handling

| Error Condition | Handling |
|-----------------|----------|
| Empty title after strip | Print error, return None |
| User interrupts (Ctrl+C) | Propagate exception |

## Example

```python
tasks = [{"id": 1, "title": "Task 1", "completed": False}]
new_task, next_id = add_task(tasks, 2)
# new_task = {"id": 2, "title": "New Task", "completed": False}
# next_id = 3
```
