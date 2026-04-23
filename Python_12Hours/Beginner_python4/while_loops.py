# while loop = execute some code WHILE some condition remains true

# Example 1
name = input("Name: ")

while name == "":
    print("Noting written")
    name = input("Name: ")

print(f"Hello {name}")

# Example 2
age = int(input("Enter age: "))

while age < 0:
    print("Age cannot be negative")
    age = int(input("Enter age: "))

print(f"You are {age} years old")

# Example 3
food = input("Enter food (q for quit): ")

while not food == "q":
    print(f"You like {food}")
    food = input("Enter food (q for quit): ")

print("bye, food")

# Example 4 - While with logical operato
num = int(input("Enter a # between 1-10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a # between 1-10: "))

print(f"Your number is {num}")
