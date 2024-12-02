def todo_list():
    print("***** TODO LIST *****")

    print("1. View all tasks")
    print("2. Create new task")
    print("3. Update task")
    print("4. Remove task")
    print("5. Exit program")

    tasks = {
        0: {
            "title": "Do homeworks",
            "description": "After school I will finish all my homework, before I play outside.",
            "status": False,
        }
    }

    while True:
        user_input = input("Choose you want to do today: ")
        print(user_input)

        if user_input == "1":
            print(tasks)


todo_list()
