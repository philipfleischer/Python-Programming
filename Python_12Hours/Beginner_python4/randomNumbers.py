import random

# six sided dice needs random numbers 1-6:
number = random.randint(1, 6)
print(f"random.randint(1, 6) = {number}")
print()

low = 1
high = 100

number = random.randint(low, high)
print(f"random.randint(low, high) = {number}")
print()

# return random float number between 0 and 1
number = random.random()
print(f"random.random() = {number}")
print()

options = ("rock", "paper", "scissors")
option = random.choice(options)
# This can print either rock, paper or scissors
print(f"random.choice(options) = {option}")

cards = ["2", "3", "4", "5", "6", "7", "8",
         "9", "10", "J", "Q", "K", "A"]

random.shuffle(cards)

print(cards)

# OUTPUT:
# random.randint(1, 6) = 1

# random.randint(low, high) = 2

# random.random() = 0.3511351654536682

# random.choice(options) = paper
# ['8', '9', 'K', '6', 'A', '10', '2', '4', '7', '5', '3', 'J', 'Q']
