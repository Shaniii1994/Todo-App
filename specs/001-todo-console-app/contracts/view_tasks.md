# Contract: view_tasks

**Type**: Function
**Module**: todo.py

## Signature

```python
def view_tasks(tasks: List[Dict]) -> None:
```

## Inputs

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `tasks` | List[Dict] | Yes | Current task list |

## Outputs

| Output | Type | Description |
|--------|------|-------------|
| None | None | Prints to stdout |

## Behavior

1. Check if tasks list is empty
2. If empty, print "No tasks yet."
3. If not empty, iterate and display each task:
   - Format: `[X] ID. Title` (X = space for incomplete, X for complete)
4. No return value

## Output Format

```
Tasks:
[X] 1. Buy groceries
[ ] 2. Pay bills
```

Or for empty list:

```
No tasks yet.
```

## Example

```python
tasks = [
    {"id": 1, "title": "Buy groceries", "completed": True},
    {"id": 2, "title": "Pay bills", "completed": False}
]
view_tasks(tasks)
# Output:
# Tasks:
# [X] 1. Buy groceries
# [ ] 2. Pay bills
```
