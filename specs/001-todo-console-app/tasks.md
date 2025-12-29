# Tasks: Phase-I In-Memory Todo Console App

**Input**: Design documents from `/specs/001-todo-console-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: This feature uses manual console-based testing as specified in plan.md.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `todo.py` at repository root

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create todo.py at repository root with module docstring
- [x] T002 Define global state variables (tasks list, next_task_id)

---

## Phase 2: Helper Functions

**Purpose**: Reusable utility functions used across all operations

- [x] T003 [P] Implement get_string_input() for safe string input with strip
- [x] T004 [P] Implement get_int_input() for safe integer input
- [x] T005 [P] Implement find_task() to locate task by ID
- [x] T006 [P] Implement validate_task_id() to check ID exists

---

## Phase 3: Display Functions

**Purpose**: Output formatting for tasks

- [x] T007 [P] Implement display_task() for single task format
- [x] T008 [P] Implement display_tasks() for task list format

---

## Phase 4: User Story 1 - Add Task (Priority: P1) MVP

**Goal**: Users can create new tasks

**Independent Test**: Run add flow, verify task appears with correct data

### Implementation for User Story 1

- [x] T009 [US1] Implement add_task() function per contract
- [x] T010 [US1] Connect to main module and test

**Checkpoint**: At this point, Add Task should be fully functional

---

## Phase 5: User Story 2 - View Tasks (Priority: P1)

**Goal**: Users can see all tasks

**Independent Test**: Add tasks, view them to verify display

### Implementation for User Story 2

- [x] T011 [US2] Implement view_tasks() function per contract
- [x] T012 [US2] Connect to main module and test

**Checkpoint**: At this point, View Tasks should be fully functional

---

## Phase 6: User Story 3 - Update Task (Priority: P2)

**Goal**: Users can modify task titles

**Independent Test**: Update title, verify change persists

### Implementation for User Story 3

- [x] T013 [US3] Implement update_task() function per contract
- [x] T014 [US3] Connect to main module and test

**Checkpoint**: At this point, Update Task should be fully functional

---

## Phase 7: User Story 4 - Delete Task (Priority: P2)

**Goal**: Users can remove tasks

**Independent Test**: Delete task, verify removal

### Implementation for User Story 4

- [x] T015 [US4] Implement delete_task() function per contract
- [x] T016 [US4] Connect to main module and test

**Checkpoint**: At this point, Delete Task should be fully functional

---

## Phase 8: User Story 5 - Toggle Complete (Priority: P2)

**Goal**: Users can mark tasks complete/incomplete

**Independent Test**: Toggle status, verify change

### Implementation for User Story 5

- [x] T017 [US5] Implement toggle_task() function per contract
- [x] T018 [US5] Connect to main module and test

**Checkpoint**: At this point, Toggle Complete should be fully functional

---

## Phase 9: User Story 6 - Menu Navigation (Priority: P1)

**Goal**: Main menu enables access to all features

**Independent Test**: All menu options work correctly

### Implementation for User Story 6

- [x] T019 [US6] Implement display_menu() function
- [x] T020 [US6] Implement get_menu_choice() function
- [x] T021 [US6] Implement main() with menu loop
- [x] T022 [US6] Wire all functions together

**Checkpoint**: All user stories should now be independently functional

---

## Phase 10: Integration Testing

**Purpose**: Verify complete application works end-to-end

- [x] T023 Test Add -> View flow
- [x] T024 Test Add -> Update -> View flow
- [x] T025 Test Add -> Delete -> View flow
- [x] T026 Test Add -> Toggle -> View flow
- [x] T027 Test error handling (invalid ID, empty title)
- [x] T028 Test exit functionality

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Helpers (Phase 2)**: Depends on Setup completion - BLOCKS display functions
- **Display (Phase 3)**: Depends on Helpers completion - BLOCKS task operations
- **User Stories (Phases 4-8)**: Can proceed in parallel (each story independent)
- **Menu (Phase 9)**: Depends on all User Story functions complete - INTEGRATION
- **Testing (Phase 10)**: Depends on Menu complete - FINAL VALIDATION

### Within Each User Story

- Helper functions before display functions
- Display functions before task operations
- Each story complete before integration

### Parallel Opportunities

- All Helper functions (T003-T006) marked [P] can run in parallel
- All Display functions (T007-T008) marked [P] can run in parallel
- User Stories 1-5 (T009-T018) can proceed in parallel once dependencies met

---

## Implementation Strategy

### MVP First (User Story 1 + Menu)

1. Complete Phase 1: Setup
2. Complete Phase 2: Helpers
3. Complete Phase 3: Display
4. Complete User Story 1: Add Task
5. Complete Menu Navigation (partial)
6. **STOP and VALIDATE**: Can add and view tasks

### Incremental Delivery

1. Add Task -> Test -> (MVP ready)
2. View Tasks -> Test -> (Can add and view)
3. Update Task -> Test -> (Can modify tasks)
4. Delete Task -> Test -> (Can remove tasks)
5. Toggle Complete -> Test -> (Can track progress)
6. Menu Navigation -> Test -> (Full application)

### Parallel Team Strategy

With multiple developers:
1. Developer A: Setup + Helpers + Display
2. Developer B: Add + View (parallel with A)
3. Developer C: Update + Delete (parallel)
4. Developer D: Toggle + Menu (parallel)
5. Integrate and test together

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
