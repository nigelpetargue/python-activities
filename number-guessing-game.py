import random

def number_guesssing():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    random_number = random.randint(1, 100)
    attempts = 0

    while True:
        attempts += 1

        try: 
            guess = int(input("Take a guesss: "))
            
            if guess > random_number: 
                print("Too high!")
            elif guess < random_number:
                print("Too low!")
            else:
                print(f"Congratulations! You guessed the number {random_number} in {attempts} {"attempt!" if attempts == 1 else "attempts!"}")
                break  
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    pass

number_guesssing()