import json
import os
from datetime import datetime

TODO_FILE = "todo.json"

def load_tasks():
    with open(TODO_FILE, "r") as f:
        return json.load(f)

def toggle_task(tasks, task_id):
    task_list = tasks["tasks"]
    for task in task_list:
        if task["id"] == task_id:
            task["completed"] = not task["completed"]
            with open(TODO_FILE, "w") as f:
                json.dump(tasks, f, indent=4)
            status = "completed" if task["completed"] else "incomplete"
            print(f"Task {task_id} marked as {status}.")
            return
    print(f"No task found with id: {task_id}")

def list_tasks(tasks):
    task_list = tasks["tasks"]
    if not task_list:
        print("No tasks yet.")
    else:
        print("\nTasks:")
        for task in task_list:
            status = "✓" if task["completed"] else "✗"
            print(f"[{status}] {task['id']}: {task['description']}")

def add_task(tasks, description):
    task_list = tasks["tasks"]
    if not task_list:
        new_id = 1
    else:
        task_ids = [task["id"] for task in task_list]
        new_id = max(task_ids) + 1

    new_task = {
        "id": new_id,
        "description": description.strip(),
        "completed": False
    }

    task_list.append(new_task)

    with open(TODO_FILE, "w") as f:
        json.dump(tasks, f, indent=4)
    print(f"Added task: {new_id} - {description.strip()}")

def delete_task(tasks, task_id):
    task_list = tasks["tasks"]
    for i, task in enumerate(task_list):
        if task["id"] == task_id:
            removed_task = task_list.pop(i)
            with open(TODO_FILE, "w") as f:
                json.dump(tasks, f, indent=4)
            print(f"Deleted task: {removed_task['id']} - {removed_task['description']}")
            return
    print(f"No task found with id: {task_id}")

def main():
    tasks = load_tasks()
    print("✅ To-Do List Manager (Type 'help' for commands)")
    
    while True:
        command = input("\n> ").strip().lower()
        
        if command == "help":
            print("\nCommands:")
            print("add <task> - Add a new task")
            print("list - Show all tasks")
            print("toggle <id> - Mark task as complete/incomplete")
            print("delete <id> - Delete a task")
            print("exit - Quit the program")
        
        elif command.startswith("add"):
            description = command[4:].strip()
            if description:
                add_task(tasks, description)
            else:
                print("Please provide a task description.")
        
        elif command == "list":
            list_tasks(tasks)

        elif command.startswith("toggle"):
            parts = command.split()
            if len(parts) == 2 and parts[1].isdigit():
                task_id = int(parts[1])
                toggle_task(tasks, task_id)
            else:
                print("Usage: toggle <id>")
        
        elif command.startswith("delete"):
            parts = command.split()
            if len(parts) == 2 and parts[1].isdigit():
                task_id = int(parts[1])
                delete_task(tasks, task_id)
            else:
                print("Usage: delete <id>")
        
        elif command == "exit":
            print("👋 Saving tasks and exiting...")
            break
        
        else:
            print("❌ Unknown command. Type 'help' for options.")

if __name__ == "__main__":
    main()
