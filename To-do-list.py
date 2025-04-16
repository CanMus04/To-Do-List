# To-Do List


tasks = []

def show_tasks():
    """Displays all tasks with index"""
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks):
            status = "✓" if task["completed"] else " "
            print(f"{i+1}. [{status}] {task['title']}")

def add_task(title):
    """Adds a new task"""
    tasks.append({"title": title, "completed": False})
    print(f"Task '{title}' has been added.")

def complete_task(index):
    """Marks a task as completed"""
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print(f"Task '{tasks[index]['title']}' marked as completed.")
    else:
        print("Invalid task number.")

def delete_task(index):
    """Deletes a task"""
    if 0 <= index < len(tasks):
        deleted_task = tasks.pop(index)
        print(f"Task '{deleted_task['title']}' has been deleted.")
    else:
        print("Invalid task number.")


print("Welcome to your To-Do List!")

while True:
    print("\nWhat would you like to do?")
    print("1. Show tasks")
    print("2. Add new task")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. Quit")
    
    choice = input("Your choice (1-5): ")
    
    if choice == "1":
        show_tasks()
    elif choice == "2":
        title = input("Title of the new task: ")
        add_task(title)
    elif choice == "3":
        show_tasks()
        try:
            index = int(input("Number of the completed task: ")) - 1
            complete_task(index)
        except ValueError:
            print("Please enter a valid number.")
    elif choice == "4":
        show_tasks()
        try:
            index = int(input("Number of the task to delete: ")) - 1
            delete_task(index)
        except ValueError:
            print("Please enter a valid number.")
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid input. Please choose 1-5.")
