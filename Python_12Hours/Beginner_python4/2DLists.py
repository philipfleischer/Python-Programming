fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]

# another way of visualizing nested lists:
groceries = [
    ["apple", "orange", "banana", "coconut"],
    ["celery", "carrots", "potatoes"],
    ["chicken", "fish", "turkey"]
]
print(groceries)
print(groceries[0][0])

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()

# nested tuples
groceries = (
    ("apple", "orange", "banana", "coconut"),
    ("celery", "carrots", "potatoes"),
    ("chicken", "fish", "turkey")
)
print(groceries)
print(groceries[0][0])

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()

# tuple made of sets
groceries = (
    {"apple", "orange", "banana", "coconut"},
    {"celery", "carrots", "potatoes"},
    {"chicken", "fish", "turkey"},
)
print(groceries)

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()
