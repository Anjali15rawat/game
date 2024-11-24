import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess it?")

    # Generate a random number
    secret_number = random.randint(1, 100)
    attempts = 0
    guessed = False

    while not guessed:
        try:
            # Get user input
            guess = int(input("\nEnter your guess: "))
            attempts += 1

            # Check the guess
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
                guessed = True
        except ValueError:
            print("Please enter a valid number.")

    print("\nThanks for playing!")

if _name_ == "_main_":
    number_guessing_game()