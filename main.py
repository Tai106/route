# Load existing items
# 1. create a new item
# 2. list items
# 3. mark item as complete
# 4. save items

import json
{"task": [
    {"task": "task is this", "complete": True}
]}

file_name = "todo_list.json"


def load_tasks():
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except:
        return {"tasks": []}

def save_tasks(tasks):
    try:
        with open(file_name, "w") as file:
            json.dump(tasks, file)
    except:
        return {"Failed to save."}

    

def view_tasks(tasks):
    task_list = tasks["tasks"]
    if len(task_list) == 0:
        print("No tasks to display.")
    else:
        print("Your To-Do List: ")
        for idx, task in enumerate(task_list):
            status = "[Completed]" if task["complete"] else "[pending]"
            print(f"{idx + 1}. {task['description']} | {status}")
        
        
def create_task(tasks):
    description = input("Enter the task description: ").strip()
    if description:
        tasks["tasks"].append({"description": description, "complete": False})
        save_tasks(tasks)
        print("Task added!")
    else:
        print("Description cannot be empty.")

def mark_task_complete():
    pass

def main():
    save_tasks({"tasks": ["saved task"]})
    tasks = load_tasks()
    print(tasks)
    
    
    while True:
        print("\nTo-Do List Manager")
        print("1. View Tasks")
        print('2. Add Task')
        print("3. Complete Task")
        print("4. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            view_tasks()
        elif choice == "2":
            create_task(tasks)
        elif choice == "3":
            mark_task_complete()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()