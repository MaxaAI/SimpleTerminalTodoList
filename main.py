def main():
    todo_list = []
    while True:
        print("\nTodo List:")
        for i, task in enumerate(todo_list):
            print(f"{i+1}. {task}")

        print("\nMenu:")
        print("1. Add task")
        print("2. Delete task")
        print("3. Quit")

        option = input("Choose an option: ")
        if option == '1':
            task = input("Enter a task: ")
            todo_list.append(task)
        elif option == '2':
            task_number = int(input("Enter the task number to delete: "))
            if task_number > 0 and task_number <= len(todo_list):
                del todo_list[task_number - 1]
            else:
                print("Invalid task number!")
        elif option == '3':
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()
