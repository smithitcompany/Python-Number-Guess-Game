import random


def guess_the_number():
    # Generate a random number between 1 and 100
    secret = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I've chosen a number between 1 and 100. Try to guess it. ")

    while True:
        try:
            # Get the player's guess
            guess = int(input("Enter your guess:"))
            attempts += 1

            # Check if the guess is correct
            if guess == secret:
                print(f"Congratulations! You guessed the number {secret} in {attempts} attempts. ")
                break

            elif guess < secret:
                print("Too low. Try again.")

            else:
                print("Too high, Try again. ")

        except ValueError:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    guess_the_number()
