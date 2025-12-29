# Implementation Plan: Phase-I In-Memory Todo Console App

**Branch**: `001-todo-console-app` | **Date**: 2025-12-29 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/001-todo-console-app/spec.md`

## Summary

Implement a Python 3 console-based Todo application with in-memory task storage. The application provides a menu-driven interface for managing tasks (add, view, update, delete, toggle completion). All data is stored in a Python list structure with auto-incrementing task IDs. No external libraries or persistence - data is lost on exit.

## Technical Context

**Language/Version**: Python 3 (stdlib only, no version-specific features)
**Primary Dependencies**: None (stdlib only)
**Storage**: In-memory Python list (list of dicts or custom structure)
**Testing**: Manual console-based testing, inline assertions
**Target Platform**: Any system with Python 3 installed (terminal/console)
**Project Type**: Single file console application
**Performance Goals**: Immediate response for all operations (<1 second per action)
**Constraints**: Single .py file, in-memory only, no external libs, menu-driven UI
**Scale/Scope**: Small (<100 tasks expected), single-user session

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Requirement | Status |
|-----------|-------------|--------|
| I. Spec-Driven Development | Code ONLY from Spec | PASS |
| II. Console-Based Python | Python 3, single file, in-memory | PASS |
| III. Core Features Phase-I | Only 6 features, no extras | PASS |
| IV. Task Model | id, title, completed only | PASS |
| V. Interaction Rules | Numeric menu, error handling | PASS |
| VI. Code Standards | Clean, modular, documented | PASS |

**Result**: All gates pass - spec-aligned design required

## Project Structure

### Documentation (this feature)

```text
specs/001-todo-console-app/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (research findings)
├── data-model.md        # Phase 1 output (data structure design)
├── quickstart.md        # Phase 1 output (usage guide)
├── contracts/           # Phase 1 output (function contracts)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
todo.py                 # Single runnable Python file (root of repo)
```

**Structure Decision**: Single Python file at repository root as per constitution requirement for single runnable file.

## Architecture Decisions

### Decision 1: Task Storage Structure

**Chosen**: List of dictionaries with consistent key structure

**Rationale**: Simple, Python-native, no external dependencies, easy to extend
- Each task: `{"id": int, "title": str, "completed": bool}`
- List provides O(1) append for new tasks
- Linear search acceptable for small task lists

**Alternatives Considered**:
- Custom class: Adds complexity, no functional benefit for Phase-I
- Named tuple: Immutable, harder to update

### Decision 2: Task ID Generation

**Chosen**: Auto-increment counter stored as module-level variable

**Rationale**: Deterministic, simple, guarantees uniqueness
- Counter initialized to 1
- Each new task: `current_id`, then `current_id += 1`
- Deleted tasks do not reclaim IDs (preserves referential integrity)

**Alternatives Considered**:
- UUID: Overkill, not human-readable
- Timestamp-based: Unnecessary complexity

### Decision 3: Menu Loop Architecture

**Chosen**: While True loop with input() and match/if statements

**Rationale**: Clear flow, easy to follow, matches spec requirements
- Main loop: `while True: display_menu(), choice = input(), handle_choice()`
- Exit condition: choice == 6 breaks loop
- Invalid input: print error, continue loop

### Decision 4: Input Validation Strategy

**Chosen**: Try/except with explicit checks before operations

**Rationale**: Graceful error handling as required by spec
- Menu choice: `int()` conversion with ValueError catch
- Task ID: existence check in tasks list before operation
- Title: empty/whitespace check after strip

## High-Level Program Flow

```
+------------------+
|     START        |
+------------------+
         |
         v
+------------------+
| Initialize State |
| (tasks=[],       |
|  next_id=1)      |
+------------------+
         |
         v
+------------------+
| Display Menu     |<------+
+------------------+       |
         |                |
         v                |
+------------------+       |
| Get User Input   |       |
+------------------+       |
         |                |
         v                |
+------------------+       |
| Validate Input   |-------+
+------------------+
         |
    +----+----+----+----+----+----+
    |    |    |    |    |    |    |
    v    v    v    v    v    v    |
  Add  View Update Delete Toggle Exit
    |    |    |    |    |    |
    +----+----+----+----+----+
         |                |
         v                |
+------------------+       |
| Process Result   |-------+
+------------------+
         |
    +----+----+
    |    |    |
    v    v    v
Error Success
    |    |
    v    v
Display Message Return to Menu
```

## Function-Level Structure

### Core Functions

| Function | Purpose | Returns |
|----------|---------|---------|
| `main()` | Entry point, menu loop | None |
| `display_menu()` | Print menu options | None |
| `get_menu_choice()` | Get and validate user input | int (1-6) |

### Task Operations

| Function | Purpose | Parameters | Returns |
|----------|---------|------------|---------|
| `add_task(tasks, next_id)` | Create new task | tasks list, current id | (task, new_next_id) |
| `view_tasks(tasks)` | Display all tasks | tasks list | None |
| `update_task(tasks)` | Update task title | tasks list | bool (success) |
| `delete_task(tasks)` | Remove task by ID | tasks list | bool (success) |
| `toggle_task(tasks)` | Toggle completion | tasks list | bool (success) |

### Helper Functions

| Function | Purpose | Parameters | Returns |
|----------|---------|------------|---------|
| `find_task(tasks, task_id)` | Locate task by ID | tasks, id | task dict or None |
| `validate_task_id(tasks, task_id)` | Check if ID exists | tasks, id | bool |
| `display_task(task)` | Format single task | task dict | None |
| `display_tasks(tasks)` | Format all tasks | tasks list | None |
| `get_string_input(prompt)` | Safe string input | prompt | str (stripped) |
| `get_int_input(prompt)` | Safe integer input | prompt | int or None |

## Data Model Design

### Task Structure

```python
task = {
    "id": int,          # Unique identifier, auto-incremented
    "title": str,       # Task description, non-empty after strip
    "completed": bool   # Completion status, default False
}
```

### State Management

```python
# Module-level variables
tasks: List[dict] = []      # In-memory task storage
next_task_id: int = 1       # ID counter for new tasks
```

### Validation Rules

| Field | Rule | Error Message |
|-------|------|---------------|
| title | After strip, length > 0 | "Task title cannot be empty." |
| task_id | Must exist in tasks list | "Task with ID X not found." |
| menu_choice | Must be int 1-6 | "Invalid choice. Please enter 1-6." |

## Input Validation & Error Handling Strategy

### Error Categories

1. **Menu Input Errors**
   - Non-numeric input → "Invalid choice. Please enter a number."
   - Out of range (0 or >6) → "Please enter a number between 1 and 6."

2. **Task ID Errors**
   - Non-numeric → "Please enter a valid task ID number."
   - Not found → "Task with ID X not found."

3. **Title Validation Errors**
   - Empty after strip → "Task title cannot be empty."

4. **Operation Confirmation**
   - Delete requires confirmation (yes/no prompt)

### Error Handling Pattern

```python
def get_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number.")

def find_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None
```

## Testing Strategy

### Manual Console Testing Matrix

| Feature | Test Case | Expected Result |
|---------|-----------|-----------------|
| Add | Empty title entered | Error message, no task added |
| Add | Valid title entered | Task appears in list with correct ID |
| View | Empty list | "No tasks yet." message |
| View | Multiple tasks | All tasks displayed with status |
| Update | Invalid ID | "Task not found" error |
| Update | Valid ID, empty title | Error, original preserved |
| Update | Valid ID, new title | Title updated |
| Delete | Invalid ID | "Task not found" error |
| Delete | Valid ID | Task removed, others unchanged |
| Toggle | Invalid ID | "Task not found" error |
| Toggle | Valid ID | Completion status flipped |
| Menu | Invalid input (text) | Error, menu redisplayed |
| Menu | Valid input (1-6) | Feature executes |
| Exit | Select option 6 | Program terminates cleanly |

### Edge Cases to Test

- Adding 100+ tasks (verify ID increment)
- Rapid menu navigation
- Deleting all tasks then adding new one
- Toggling completion multiple times
- Invalid menu input (negative numbers, floats)

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| None | N/A | N/A |

No constitution violations - implementation follows all principles.
