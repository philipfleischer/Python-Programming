# Membership operators = used to test wether a value or
#                         variable is found in a sequence
#                       (string, list, tuple, set, or dictionary)
#                       1. in       2. not in

# ------------------ STRING -------------
word = "APPLE"
letter = input("Guess a letter in the secret word: ")

if letter in word:
    print(f"There is a {letter}")
else:
    print(f"{letter} was not found")
if letter not in word:
    print(f"{letter} was not found")
else:
    print(f"There is a {letter}")


# ---------------SET--------------
students = {"Spongebob", "Patrick", "Sandy"}
student = input("Enter name: ")
if student in students:
    print(f"{student} is a student")
else:
    print(f"{student} not found")



# ----------------- DICTIONARY -------------
grades = {"Sandy": "A", "Squidward": "B", "SOL": "C", "Pat": "D"}
student = input("Enter name: ")

if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} not found")

email = "fleischer1@live.no"

if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")
