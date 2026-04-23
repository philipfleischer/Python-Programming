# *args     = allows you to pass multiple non-key arguments
# **kwargs  = allows you to pass multiple keyword-arguments
#             * unpacking operator
#             1. positional, 2. default, 3. keyword, 4. ARBITRARY

# -------------------------- *args -----------------------------
def add1(a, b):
    return a + b

print(f"print add1(1, 2) = {add1(1, 2)}")

def add2(*args):
    print(type(args))   # <class 'tuple'>

    total = 0
    for arg in args:
        total += arg
    return total

print(f"add2(1, 2, 3, 4, 5) = {add2(1, 2, 3, 4, 5)}")
# OUT:
# <class 'tuple'>
# add2(1, 2, 3, 4, 5) = 15

# the '*' (unpacking operator) is important! not the name:
def add3(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(f"add3(1, 2, 3, 10) = {add3(1, 2, 3, 10)}")

def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Philip", "Elias", "Fleischer")
print()

# OUTPUT:
# print add1(1, 2) = 3
# <class 'tuple'>
# add2(1, 2, 3, 4, 5) = 15
# add3(1, 2, 3, 10) = 16
# Philip Elias Fleischer


# ------------------------ **kwargs ---------------------------
print()
def print_all_address(**kwargs):
    print(type(kwargs)) # <class 'dict'>

    print("VALUES (which is the keywords!):")
    for key in kwargs.keys():
        print(key)
    print()
    print("KEYS (which is the arguments passed!):")
    for value in kwargs.values():
        print(value)
    print()
    print("-----KEYS : VALUES------")
    for key, value in kwargs.items():
        print(f"{key} : {value}")

print_all_address(street="Eddaveien 13L", city="Moss", state="Østfold", zip="1513")

#OUTPUT:
# <class 'dict'>
# VALUES (which is the keywords!):
# street
# city
# state
# zip

# KEYS (which is the arguments passed!):
# Eddaveien 13L
# Moss
# Østfold
# 1513

# -----KEYS : VALUES------
# street : Eddaveien 13L
# city : Moss
# state : Østfold
# zip : 1513

print()
def print_address(**kwargs):
    print()
    print("-----KEYS : VALUES------")
    for key, value in kwargs.items():
        print(f"{key} : {value}")

print_address(street="Eddaveien 13L", city="Moss", state="Østfold", zip="1513")
# OUTPUT:
# -----KEYS : VALUES------
# street : Eddaveien 13L
# city : Moss
# state : Østfold
# zip : 1513

print_address(world="Earth", street="Eddaveien 13L", city="Moss", state="Østfold", zip="1513")
# OUTPUT:
# -----KEYS : VALUES------
# world : Earth
# street : Eddaveien 13L
# city : Moss
# state : Østfold
# zip : 1513

print_address(galaxy="MilkyWay", world="Earth", street="Eddaveien 13L", city="Moss", state="Østfold", zip="1513")
# OUTPUT:
# -----KEYS : VALUES------
# galaxy : MilkyWay
# world : Earth
# street : Eddaveien 13L
# city : Moss
# state : Østfold
# zip : 1513
