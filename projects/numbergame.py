import random

secret_number = random.randint(1, 100)
guess = 0
attempts = 0

print("I'm thinking of a number between 1 and 100.")
while guess != secret_number:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1
        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
    except ValueError:
        print("Invalid input. Please enter a number.")

print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")