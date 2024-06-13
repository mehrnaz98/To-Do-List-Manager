# Function to add task
def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added successfully!")

# Function to view tasks
def view_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty!")
    else:
        print("Your to-do list:")
        for index, task in enumerate(tasks, start=1):
            status = " (Completed)" if task["completed"] else ""
            print(f"{index}. {task['task']}{status}")

# Function to mark task as completed
def mark_completed(tasks):
    view_tasks(tasks)
    index = int(input("Enter the task number to mark as completed: ")) - 1
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print("Task marked as completed!")
    else:
        print("Invalid task number!")

# Function to remove task
def remove_task(tasks):
    view_tasks(tasks)
    index = int(input("Enter the task number to remove: ")) - 1


# Main function
def main():
    tasks = []
    print("Welcome to the To-Do List Manager!")
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Mark Task as Completed\n4. Remove Task\n5. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_completed(tasks)
        elif choice == '4':
            remove_task(tasks)
        elif choice == '5':
            print("Thank you for using the To-Do List Manager!")
            break
        else:
            print("Invalid choice! Please try again.")

   
if __name__ == "__main__":
    main()