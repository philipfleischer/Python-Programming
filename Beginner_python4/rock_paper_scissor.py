import random

options = ("rock", "paper", "scissors")
running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"Copmuter: {computer}")

    if player == computer:
        print("TIE!")
    elif player == "rock" and computer == "scissors":
        print("YOUWIN!")
    elif player == "paper" and computer == "paper":
        print("YOUWIN!")
    elif player == "scissors" and computer == "paper":
        print("YOUWIN!")
    else:
        print("YOULOOOOOOSE!")

    if not input("Play again? (Y/N): ").lower() == "y":
        running = False

print("Thanks for playing!")


# OUTPUT:
# Enter a choice (rock, paper, scissors): rock
# Player: rock
# Copmuter: scissors
# YOUWIN!
# Play again? (Y/N): y
# Enter a choice (rock, paper, scissors): paper
# Player: paper
# Copmuter: scissors
# YOULOOOOOOSE!
# Play again? (Y/N): y
# Enter a choice (rock, paper, scissors): scissors
# Player: scissors
# Copmuter: scissors
# TIE!
# Play again? (Y/N): n
# Thanks for playing!
