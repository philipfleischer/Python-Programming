# collection = single "variable" used to store multiple values
#   List = [] ordered changeable. Duplicates OK
#   Set = {} unordered and immutable, but Add/Remove OK. NO Duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER

# ----------- LIST part 1/3 ------------
print("----------- LIST part 1/3 ------------")
fruit = "apple"
print(f"Print fruit string: {fruit}")
print()

fruit = ["apple"]
print(f"Print fruit list: {fruit}")
print()


fruits = ["apple", "orange", "banana", "coconut"]
print(f"Print fruits list: {fruits}")
print(f"Print fruits[3] element: {fruits[3]}")
print(f"Print fruits[0:3] elements: {fruits[0:3]}")
print(f"Print fruits[::2] elements: {fruits[::2]}")
print()


for fruit in fruits:
    print(fruit)
print()


print("Apple is in fruits list" if "apple" in fruits else "Apple is not in fruits.")
print()


fruits[0] = "pineapple"
for fruit in fruits:
    print(fruit)
print()

fruits.append("kiwi")
print(fruits)
print()
fruits.remove("kiwi")
print(fruits)
print()
fruits.insert(0, "kiwi")
print(fruits)
print()
fruits.sort()
print(fruits)
print()
# To print in reverse we need to first sort them, then reverse them!
fruits.reverse()
print(fruits)
print()
fruits.clear()
print(fruits)
print()

fruits = ["apple", "orange", "banana", "coconut"]
print(fruits)
print(f"fruits.index('apple') = {fruits.index('apple')}")
print(f"fruits.index('coconut') = {fruits.index('coconut')}")
print()
print(f"fruits.count('banana') = {fruits.count('banana')}")

# OUTPUT:
# Print fruit string: apple

# Print fruit list: ['apple']

# Print fruits list: ['apple', 'orange', 'banana', 'coconut']
# Print fruits[3] element: coconut
# Print fruits[0:3] elements: ['apple', 'orange', 'banana']
# Print fruits[::2] elements: ['apple', 'banana']

# apple
# orange
# banana
# coconut

# Apple is in fruits list

# pineapple
# orange
# banana
# coconut

# ['pineapple', 'orange', 'banana', 'coconut', 'kiwi']

# ['pineapple', 'orange', 'banana', 'coconut']

# ['kiwi', 'pineapple', 'orange', 'banana', 'coconut']

# ['banana', 'coconut', 'kiwi', 'orange', 'pineapple']

# ['pineapple', 'orange', 'kiwi', 'coconut', 'banana']

# []

# ['apple', 'orange', 'banana', 'coconut']
# fruits.index('apple') = 0
# fruits.index('coconut') = 3

# fruits.count('banana') = 1


# ----------- SET part 2/3 ------------
print("----------- SET part 2/3 ------------")
fruitss = {"apple", "orange", "banana", "coconut"}
print(fruitss) # Will be in different order many times, unordered
# cannot use indexing since it is unordered
fruitss.add("pineapple")
print(fruitss)
print()
fruitss.remove("apple")
print(fruitss)
print()
fruitss.pop() # Remove first element (random, since unordered)
print(fruitss)
print()
fruitss.clear()
print(fruitss)
print()

# OUTPUT:
# {"orange", "apple", "banana", "coconut"}
# {"coconut", "orange", "apple", "pineapple", "banana"}

# {"coconut", "orange", "pineapple", "banana"}

# {"orange", "pineapple", "banana"}

# set()

# ----------- TUPLES part 3/3 ------------
print("----------- TUPLES part 3/3 ------------")
fruitsss = ("apple", "orange", "banana", "coconut")
print(len(fruitsss))
print("pineaplle" in fruitsss)

print(fruitsss.index("apple"))
print(fruits.count("coconut"))

for fruit in fruitsss:
    print(fruit)

# OUTPUT:
# 4
# False
# 0
# 1
# apple
# orange
# banana
# coconut
