# Load existing items
# 1. create a new item
# 2. list items
# 3. mark item as complete
# 4. save items
# 5. Mark a task as incomplete
# 6. Delete a task 

import json

file_name = "todo_list.json"

{"task": [
    {"task": "task is this", "complete": True}
]}

def load_tasks():
    try:
        with open(file_name, "r") as file:
            data = json.load(file)
            # Ensure the data is always a dictionary
            if not isinstance(data, dict) or "tasks" not in data:
                return {"tasks": []}
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return {"tasks": []}


def save_tasks(tasks):
    try:
        with open(file_name, "w") as file:
            json.dump(tasks, file, indent=4)
    except Exception as e:
        print("Failed to save, Please try again.")
  
def view_tasks(tasks):
    print()
    task_list = tasks.get("tasks", [])  # Ensure 'tasks' exists

    if not isinstance(task_list, list):  # Ensure it is a list
        print("Error: Task data is corrupted.")
        return

    if len(task_list) == 0:
        print("No tasks to display.")
    else:
        print("Your To-Do List:")
        for idx, task in enumerate(task_list):
            if not isinstance(task, dict):  # Ensure each task is a dictionary
                print(f"Error: Task {idx + 1} is corrupted.")
                continue
            status = "[Completed]" if task.get("complete", False) else "[Pending]"
            print(f"{idx + 1}. {task.get('task', task)} | {status}")

              
def create_task(tasks):
    description = input("Enter the task description: ").strip()
    if description:
        tasks["tasks"].append({"description": description, "complete": False})
        save_tasks(tasks)
        print("Task added!")
    else:
        print("Description cannot be empty.")

def mark_task_complete(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to mark as complete: ").strip())
        if 1 <= task_number <= len(tasks["tasks"]):
            tasks["tasks"][task_number - 1]["complete"] = True
            save_tasks(tasks)
            print("Task marked as complete.")
        else:
            print("Invalid task number.")
    except:
        print("Enter a valid number.")
        
def main():
    tasks = load_tasks()
    
    while True:
        print("\nTo-Do List Manager")
        print("1. View Tasks")
        print('2. Add Task')
        print("3. Complete Task")
        print("4. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            create_task(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()