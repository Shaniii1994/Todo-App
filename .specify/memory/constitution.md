<!--
Sync Impact Report:
- Version change: N/A → 1.0.0 (initial creation)
- Added principles: 6 core principles defined
- Added sections: Additional Constraints, Development Workflow, Governance
- Templates requiring updates: None (templates align with constitution)
- Follow-up TODOs: None
-->

# Todo App Constitution

## Core Principles

### I. Spec-Driven Development

Follow STRICT Spec-Driven Development - Generate code ONLY from the provided Specification.
Do NOT assume or add features. Do NOT write code outside the Spec.
If Spec is unclear, ask for clarification. Output MUST strictly follow the Spec.
Rationale: Ensures alignment with user intent and prevents feature creep.

### II. Console-Based Python Application

Build console-based Python 3 program only with in-memory storage (no files, no DB).
No external libraries. Single runnable Python file.
Menu-driven terminal interaction.
Rationale: Minimal dependencies ensure portability and simplicity for Phase-I.

### III. Core Features (Phase-I)

Allowed features: Add task, View tasks, Update task, Delete task,
Mark task complete/incomplete, Exit application.
No priorities, tags, dates, AI, web, or persistence.
Rationale: Scope isolation prevents feature bloat in initial phase.

### IV. Task Model

Task model: id (unique integer), title (string), completed (boolean).
Rationale: Minimal data structure sufficient for core functionality.

### V. Interaction Rules

Display numeric menu, handle invalid input gracefully, loop until user exits.
Rationale: Predictable UX with clear error recovery ensures usability.

### VI. Code Standards

Clean, readable, modular functions. Clear naming and comments.
Deterministic and error-free.
Rationale: Maintainable code enables future evolution of the application.

## Additional Constraints

- Python 3 only - no version-specific features that reduce compatibility
- Single file architecture - all code in one runnable Python file
- In-memory storage - data lost on exit (intentional for Phase-I)
- No external dependencies - stdlib only for maximum portability

## Development Workflow

1. Specification first - never implement without clear requirements
2. Clarification required - ask when specs are ambiguous
3. Minimal implementation - only what spec explicitly allows
4. Error handling - graceful degradation for invalid inputs
5. Clean code - modular, readable, commented implementation

## Governance

This constitution supersedes all other development practices for this project.
Amendments require documentation of rationale and alignment with project goals.
All changes must maintain backward compatibility within the same phase.

**Version**: 1.0.0 | **Ratified**: 2025-12-29 | **Last Amended**: 2025-12-29
