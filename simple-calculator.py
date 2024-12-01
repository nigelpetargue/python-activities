def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def simple_calculator():
    print("********* SIMPLE CALCULATOR *********")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Remainder")
    print("6. Exponentiation")
    print("0. Exit")

    while True:
        operator = input("Select operator you want to use: ")

        if operator == "0":
            print("Exiting calculator. Goodbye!")
            break

        if operator not in ["1", "2", "3", "4", "5", "6"]:
            print("Invalid input. Please try again.")
            continue

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        if operator == "4" and num2 == 0:
            print("Division by zero is not allowed!")
            continue

        operations = {
            "1": ("sum", num1 + num2),
            "2": ("difference", num1 - num2),
            "3": ("product", num1 * num2),
            "4": ("quotient", num1 / num2),
            "5": ("remainder", num1 % num2),
            "6": ("result", num1**num2),
        }

        operation_name, result = operations[operator]
        print(f"The {operation_name} is: {result}")

        closing_choice = input("Do you want to calculate again? (y/n): ").lower()
        if closing_choice != "y":
            print("Thank you for using SIMPLE CALCULATOR. Goodbye!")
            break


simple_calculator()
