# Research: Phase-I In-Memory Todo Console App

**Date**: 2025-12-29
**Feature**: 001-todo-console-app

## Decisions Resolved

### Decision 1: Task Storage Structure

**Chosen**: List of dictionaries with consistent key structure

**Rationale**:
- Python-native data structure with no dependencies
- Dictionary provides clear key-value mapping for task attributes
- List allows easy iteration for view operations
- O(1) append operation for adding tasks
- Simple to serialize if persistence is added in future phases

**Implementation**:
```python
tasks: List[Dict[str, Any]] = []
# Each task: {"id": int, "title": str, "completed": bool}
```

**Alternatives Considered**:
- Custom class: Adds boilerplate, no functional benefit for simple Phase-I
- Named tuple: Immutable, makes updates verbose (requires copy)
- Database: Violates in-memory constraint

---

### Decision 2: Task ID Generation Strategy

**Chosen**: Auto-increment counter

**Rationale**:
- Simple, deterministic, human-readable IDs
- Guarantees uniqueness without collision checks
- Linear growth, predictable next ID

**Implementation**:
```python
next_task_id = 1
# On add: task_id = next_task_id; next_task_id += 1
```

**Alternatives Considered**:
- UUID: Overkill, not human-friendly
- Timestamp: Unnecessary complexity
- Random: Risk of collision, non-deterministic

---

### Decision 3: Input Validation Approach

**Chosen**: Defensive input functions with try/except

**Rationale**:
- Graceful error handling per spec requirement
- Clear user feedback with specific error messages
- Loop until valid input for robust interaction

**Pattern**:
```python
def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")
```

---

### Decision 4: Menu Loop Architecture

**Chosen**: While True loop with match-case (Python 3.10+) or if/elif

**Rationale**:
- Clear control flow
- Easy to debug and modify
- Matches spec requirement for menu-driven interaction

**Implementation**:
```python
while True:
    display_menu()
    choice = get_menu_choice()
    if choice == 1:
        add_task()
    elif choice == 2:
        view_tasks()
    # ... etc
    elif choice == 6:
        break
```

---

## Best Practices Applied

1. **Separation of Concerns**: Each menu option maps to a dedicated function
2. **Fail Fast**: Validate inputs before operations
3. **User Feedback**: Clear messages for success and error states
4. **Idempotency**: Operations produce consistent results
5. **Single Responsibility**: Each function does one thing

## References

- Python Official Documentation: https://docs.python.org/3/
- Input validation patterns from Python tutorials
- Console application best practices
