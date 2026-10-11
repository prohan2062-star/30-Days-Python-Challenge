# Day 05 - Number Guessing Game

import random

secret_number = random.randint(1, 10)
attempts = 0

while True:
    guess = int(input("Guess a number between 1 and 10: "))
    attempts += 1

    if guess < 1 or guess > 10:
        print("Please enter a number between 1 and 10.")
        continue

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed it!")
        print("Attempts:", attempts)
        break
