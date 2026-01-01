todo_list = []

while True:
    command = input("Enter command (add/list/exit): ")

    if command == "add":
        item = input("Enter task: ")
        todo_list.append(item)
        print("Task added.")

    elif command == "list":
        print("Your Tasks:", todo_list)

    elif command == "clear":
        todo_list.clear()
        print("All tasks deleted.")

    elif command == "exit":
        break

    else:
        print("Unknown command.")
