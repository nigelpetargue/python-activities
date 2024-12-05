def todo_list():
    print("***** TODO LIST *****")

    print("1. View all tasks")
    print("2. Create new task")
    print("3. Complete task")
    print("4. Remove task")
    print("5. Exit program")

    tasks = {
        0: {
            "title": "Do homeworks",
            "description": "After school I will finish all my homework, before I play outside.",
            "status": False,
        },
        1: {
            "title": "Walk the dog",
            "description": "Walk the dog on park.",
            "status": False,
        },
    }

    while True:
        user_input = input("Choose you want to do today: ")

        if user_input == "5":
            print("Existing program...")
            break

        match user_input:
            case "1":
                for item in tasks.items():
                    print(item)
            case "2":
                task_title = input("Enter task title: ")
                task_details = input("Enter task details: ")
                task = {
                    "title": task_title,
                    "description": task_details,
                    "status": False,
                }

                random_id = max(tasks.keys()) + 1
                tasks[random_id] = task
                print("Successfuly inserted new task.")
            case "3":
                task_id = int(input("Enter task id: "))
                tasks[task_id]["status"] = True
                print("Task completed.")
            case "4":
                task_id = int(input("Enter task id: "))
                del tasks[task_id]
                print("Successfuly removed task on task list.")
            case "5":
                print("Invalid user input.")


todo_list()
