import random

def choose_difficulty():
    print("Choose a difficulty level:")
    print("1. Easy (1-10)")
    print("2. Medium (1-50)")
    print("3. Hard (1-100)")

    while True:
        difficulty = input("Enter the difficulty level (1, 2, or 3): ")
        if difficulty == '1':
            return 10
        elif difficulty == '2':
            return 50
        elif difficulty == '3':
            return 100
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    # Call the function to choose a difficulty and define max_number
    max_number = choose_difficulty()
    print(f"Difficulty selected: {max_number}")

    number_to_guess = random.randint(1, max_number)
    attempts = 0

    while True:
        try:
            user_guess = int(input(f"Guess a number between 1 and {max_number}: "))
            attempts += 1

            if user_guess < 1 or user_guess > max_number:
                print(f"Please guess a number within the range of 1 to {max_number}!")
            elif user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input! Please enter an integer.")

if __name__ == "__main__":
    number_guessing_game()

