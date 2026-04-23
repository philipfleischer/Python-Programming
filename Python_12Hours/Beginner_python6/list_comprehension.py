# List comprehension = A concise way to create lists in Python
#                       Compact and easier to read than traditional loops
#                       [expression for vvalue in iterable if condition]

# Ordinary way, without list comprehension
doubles = []
for i in range(1, 11):
    doubles.append(i * 2)

print(doubles)
# OUT -> [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# With list-comprehension
# doubles = [expression for vvalue in iterable if condition]
doubles = [i * 2 for i in range(1, 11)]
print(f"Doubles: {doubles}")
# OUT -> Doubles: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

triples = [i * 3 for i in range(1, 11)]
print(f"Triples: {triples}")
# OUT -> Triples: [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

squares = [i**2 for i in range(1, 11)]
print(f"Squares: {squares}")
# OUT -> Squares: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# -----------STRINGS -------
fruits = ["apple", "orange", "banana", "coconut"]
fruits = [fruit.upper() for fruit in fruits]
print(fruits)
# OUT -> ['APPLE', 'ORANGE', 'BANANA', 'COCONUT']

fruits = ["apple", "orange", "banana", "coconut"]
fruits_chars = [fruit[0] for fruit in fruits]
print(fruits_chars)
# OUT -> ['a', 'o', 'b', 'c']

# ---------NUMBERS ----------
numbers = [1, -2, 3, -4, 5, -6, 8, -7]
positive_nums = [num for num in numbers if num >= 0]
negative_nums = [num for num in numbers if num <= 0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 == 1]
print(positive_nums)  # OUT -> [1, 3, 5, 8]
print(negative_nums)  # OUT -> [-2, -4, -6, -7]
print(even_nums)  # OUT -> [-2, -4, -6, 8]
print(odd_nums)  # OUT -> [1, 3, 5, -7]

grades = [85, 42, 79, 90, 56, 61, 30]
passing_grades = [grade for grade in grades if grade >= 60]
print(passing_grades)  # OUT -> [85, 79, 90, 61]
