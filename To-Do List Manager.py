# Function to add task
def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added successfully!")


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