number = input("Enter a number: ")

try:
    number = int(number)
    if number % 2 == 0:
        print("even number")
    else:
        print("odd number")
except ValueError:
    print("Please enter a valid whole number.")
