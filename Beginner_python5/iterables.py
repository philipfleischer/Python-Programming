# Iterables = An object/collection that can return its elements one at a time,
#               allowing it to be iterated over in a loop.

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number, end=" ")
# OUT -> 1 2 3 4 5

numbers = (1, 2, 3, 4, 5)
print()

for item in reversed(numbers):
    print(item, end=" - ")
print()
# OUT -> 5 - 4 - 3 - 2 - 1 -

fruits = {"apple", "orange", "banana", "cocounut"}
# Ikke lov å reversere en mengde/SET
# for fruit in reversed(fruits):
#     print(fruit)
print()

name = "Philip Elias Fleischer"
for char in name:
    print(char, end=" ")
# OUT -> P h i l i p   E l i a s   F l e i s c h e r

print()
print()

my_dictionary = {"A": 1, "B": 2, "C": 3}
for key in my_dictionary:
    print(key, end=" ")
# OUT -> A B C

print()
print()

for value in my_dictionary.values():
    print(value, end=" ")
# OUT -> 1 2 3
print()
print()

for key, value in my_dictionary.items():
    print(f"{key} : {value}")
# OUT:
# A: 1
# B: 2
# C: 3

print()
