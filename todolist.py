todo_list = []

def show_menu():
    print("\n=== TO-DO LIST MENU ===")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")

def view_tasks():
    if not todo_list:
        print("\nNo tasks in your list.")
        return
    print("\nYour Tasks:")
    for idx, task in enumerate(todo_list, 1):
        status = "✔" if task["done"] else "!"
        print(f"{idx}. [{status}] {task['title']}")

def add_task():
    title = input("Enter task title: ").strip()
    if title:
        todo_list.append({"title": title, "done": False})
        print("Task added!")
    else:
        print("Task title cannot be empty.")

def mark_done():
    view_tasks()
    try:
        task_no = int(input("Enter task number to mark as done: "))
        if 1 <= task_no <= len(todo_list):
            todo_list[task_no - 1]["done"] = True
            print("Task marked as done!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        task_no = int(input("Enter task number to delete: "))
        if 1 <= task_no <= len(todo_list):
            removed = todo_list.pop(task_no - 1)
            print(f"Deleted task: {removed['title']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    print("Welcome to the Command-Line To-Do List App!")
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()
        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            mark_done()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting... Stay productive!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
