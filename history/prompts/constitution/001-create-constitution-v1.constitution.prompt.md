---
id: "001"
title: "Create Constitution v1"
stage: "constitution"
date: "2025-12-29"
surface: "agent"
model: "claude-sonnet-4-5-20250929"
feature: "none"
branch: "main"
user: "Hackathon Participant"
command: "/sp.constitution"
labels: ["constitution","governance","project-setup"]
links:
  spec: "null"
  ticket: "null"
  adr: "null"
  pr: "null"
files:
  - ".specify/memory/constitution.md"
tests:
  - "null"
---

## Prompt

# Constitution: Phase-I In-Memory Todo Console App

## Role
You are an expert AI Software Engineer following STRICT Spec-Driven Development.
You MUST generate code ONLY from the provided Specification.

## Project Scope
Phase-I of "Evolution of Todo" Hackathon.
Build a Python-based, console Todo application with in-memory data storage.

## Constraints
- Console-based Python 3 program only
- In-memory storage (no files, no DB)
- No external libraries
- Single runnable Python file
- Menu-driven terminal interaction

## Spec-Driven Rules (STRICT)
- Do NOT assume or add features
- Do NOT write code outside the Spec
- If Spec is unclear, ask for clarification
- Output MUST strictly follow the Spec

## Allowed Features (Phase-I Only)
1. Add task
2. View tasks
3. Update task
4. Delete task
5. Mark task complete/incomplete
6. Exit application

No priorities, tags, dates, AI, web, or persistence

## Task Model
- id (unique integer)
- title (string)
- completed (boolean)

## Interaction Rules
- Display numeric menu
- Handle invalid input gracefully
- Loop until user exits

## Code Standards
- Clean, readable, modular functions
- Clear naming and comments
- Deterministic and error-free

## Output
- Generate Python code only
- No explanations unless asked

Acknowledge this Constitution and wait for the Specification.

## Response snapshot

Created project constitution at `.specify/memory/constitution.md` with 6 core principles:
- Spec-Driven Development (strict adherence to specs)
- Console-Based Python Application (Python 3, in-memory, single file)
- Core Features Phase-I (6 allowed features, no extras)
- Task Model (id, title, completed)
- Interaction Rules (numeric menu, error handling)
- Code Standards (clean, modular, deterministic)

Added Additional Constraints and Development Workflow sections. Constitution v1.0.0 ratified 2025-12-29.

## Outcome

- ✅ Impact: Established project governance rules and development principles for Phase-I
- 📁 Files: .specify/memory/constitution.md created
- 🔁 Next prompts: Awaiting feature specification for implementation
- 🧠 Reflection: Constitution successfully captures all constraints from user input

## Evaluation notes (flywheel)

- Failure modes observed: "null"
- Graders run and results (PASS/FAIL): "null"
- Prompt variant (if applicable): "null"
- Next experiment (smallest change to try): "null"
