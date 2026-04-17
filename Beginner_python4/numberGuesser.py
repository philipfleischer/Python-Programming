# Python number guessing game
import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Python Number Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("That number is out of range")
            print(f"Please select a number between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("Too low! Try again")
        elif guess > answer:
            print("Too high! Try again!")
        else:
            print(f"CORRECT! The answer was {answer}")
            print(f"Number of guesses: {guesses}")
            is_running = False
    else:
        print("Invalid guess")
        print(f"Please select a number between {lowest_num} and {highest_num}")

# OUTPUT for one particular run:
# Python Number Guessing Game
# Select a number between 1 and 100
# Enter your guess: 50
# Too low! Try again
# Enter your guess: 75
# Too high! Try again!
# Enter your guess: 63
# Too low! Try again
# Enter your guess: 69
# Too low! Try again
# Enter your guess: 72
# Too low! Try again
# Enter your guess: 74
# CORRECT! The answer was 74
# Number of guesses: 6
