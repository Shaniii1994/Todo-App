#!/usr/bin/env python3
"""
Phase-I In-Memory Todo Console Application

A simple console-based Todo application that manages tasks in memory.
No external libraries, single file implementation, menu-driven interface.
"""

# Module-level state
tasks = []  # In-memory task storage
next_task_id = 1  # ID counter for new tasks


# =============================================================================
# Helper Functions
# =============================================================================

def get_string_input(prompt):
    """
    Get string input from user with whitespace stripped.

    Args:
        prompt: The prompt message to display

    Returns:
        str: User input with leading/trailing whitespace removed
    """
    return input(prompt).strip()


def get_int_input(prompt):
    """
    Get integer input from user with validation.

    Args:
        prompt: The prompt message to display

    Returns:
        int: Valid integer input, or None if invalid
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def find_task(tasks_list, task_id):
    """
    Find a task by its ID.

    Args:
        tasks_list: List of task dictionaries
        task_id: The ID to search for

    Returns:
        dict or None: Task dictionary if found, None otherwise
    """
    for task in tasks_list:
        if task["id"] == task_id:
            return task
    return None


def validate_task_id(tasks_list, task_id):
    """
    Check if a task ID exists in the task list.

    Args:
        tasks_list: List of task dictionaries
        task_id: The ID to validate

    Returns:
        bool: True if task exists, False otherwise
    """
    return any(task["id"] == task_id for task in tasks_list)


# =============================================================================
# Display Functions
# =============================================================================

def display_task(task):
    """
    Display a single task in formatted form.

    Args:
        task: Task dictionary with id, title, completed
    """
    status = "[X]" if task["completed"] else "[ ]"
    print(f"{status} {task['id']}. {task['title']}")


def display_tasks(tasks_list):
    """
    Display all tasks in the list.

    Args:
        tasks_list: List of task dictionaries
    """
    if not tasks_list:
        print("No tasks yet.")
    else:
        print("Tasks:")
        for task in tasks_list:
            display_task(task)


# =============================================================================
# Task Operations
# =============================================================================

def add_task(tasks_list, current_id):
    """
    Add a new task to the list.

    Args:
        tasks_list: List of task dictionaries (modified in place)
        current_id: The next available ID for the new task

    Returns:
        tuple: (new_task_dict, next_id) where next_id is current_id + 1
    """
    title = get_string_input("Enter task title: ")
    if not title:
        print("Task title cannot be empty.")
        return None, current_id

    new_task = {
        "id": current_id,
        "title": title,
        "completed": False
    }
    tasks_list.append(new_task)
    print("Task added!")
    return new_task, current_id + 1


def view_tasks(tasks_list):
    """
    Display all tasks.

    Args:
        tasks_list: List of task dictionaries
    """
    display_tasks(tasks_list)


def update_task(tasks_list):
    """
    Update a task's title.

    Args:
        tasks_list: List of task dictionaries

    Returns:
        bool: True if updated successfully, False otherwise
    """
    task_id = get_int_input("Enter task ID: ")
    if task_id is None:
        return False

    task = find_task(tasks_list, task_id)
    if task is None:
        print(f"Task with ID {task_id} not found.")
        return False

    new_title = get_string_input("Enter new title: ")
    if not new_title:
        print("Task title cannot be empty.")
        return False

    task["title"] = new_title
    print("Task updated!")
    return True


def delete_task(tasks_list):
    """
    Delete a task by ID.

    Args:
        tasks_list: List of task dictionaries (modified in place)

    Returns:
        bool: True if deleted successfully, False otherwise
    """
    task_id = get_int_input("Enter task ID: ")
    if task_id is None:
        return False

    task = find_task(tasks_list, task_id)
    if task is None:
        print(f"Task with ID {task_id} not found.")
        return False

    confirm = get_string_input("Delete this task? (yes/no): ").lower()
    if confirm != "yes":
        print("Delete cancelled.")
        return False

    tasks_list.remove(task)
    print("Task deleted!")
    return True


def toggle_task(tasks_list):
    """
    Toggle a task's completion status.

    Args:
        tasks_list: List of task dictionaries

    Returns:
        bool: True if toggled successfully, False otherwise
    """
    task_id = get_int_input("Enter task ID: ")
    if task_id is None:
        return False

    task = find_task(tasks_list, task_id)
    if task is None:
        print(f"Task with ID {task_id} not found.")
        return False

    task["completed"] = not task["completed"]
    status = "complete" if task["completed"] else "incomplete"
    print(f"Task marked as {status}!")
    return True


# =============================================================================
# Menu Functions
# =============================================================================

def display_menu():
    """Display the main menu options."""
    print("\n=== Todo Application ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Toggle Complete")
    print("6. Exit")


def get_menu_choice():
    """
    Get and validate menu choice from user.

    Returns:
        int: Valid menu choice (1-6), or None if invalid
    """
    choice = get_int_input("> ")
    if choice is None:
        return None
    if choice < 1 or choice > 6:
        print("Please enter a number between 1 and 6.")
        return None
    return choice


def handle_menu_choice(choice):
    """
    Execute the selected menu option.

    Args:
        choice: The menu choice number (1-6)
    """
    global tasks, next_task_id

    if choice == 1:
        result = add_task(tasks, next_task_id)
        if result[1] > next_task_id:
            next_task_id = result[1]
    elif choice == 2:
        view_tasks(tasks)
    elif choice == 3:
        update_task(tasks)
    elif choice == 4:
        delete_task(tasks)
    elif choice == 5:
        toggle_task(tasks)
    elif choice == 6:
        print("Goodbye!")
        return True  # Signal to exit
    return False  # Continue running


# =============================================================================
# Main Application
# =============================================================================

def main():
    """Main application entry point."""
    global tasks, next_task_id

    # Initialize state (already done at module level, but ensure consistency)
    tasks = []
    next_task_id = 1

    while True:
        display_menu()
        choice = get_menu_choice()

        if choice is None:
            continue

        should_exit = handle_menu_choice(choice)
        if should_exit:
            break


if __name__ == "__main__":
    main()
