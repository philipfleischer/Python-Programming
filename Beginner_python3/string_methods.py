name = input("Name: ")

# Returns length of string
name_len = len(name)
print(name_len)

# Returns the first occurrence of search
index = name.find("i")
print(f"The char 'i' was found at index: {index} in the string, which is at place {index + 1}")

# Returns the last occurrence, r=reverse
index = name.rfind("i")
print(f"The char 'i' was found at index: {index} in the string, which is at place {index + 1}")

# .capitalize() makes the first character in capital letters
name = name.lower()
print(".lower() name: ", name)
print("Capitalized name:", name.capitalize())
print("Name in .upper():", name.upper())

# Boolean return for if the statement is digits only:
print("Is my name digits? = ", name.isdigit())

# Boolean return for if the statement is alphabetical chars only:
# If we use " " -> space, then it returns False, since it is not
# a alphabetical character.
print("Is my name.isalpha()? = ", name.isalpha())

# ---------- COUNT -------------------

# The count method counts all the occurrences of the character
phone_number = input("Phone-Number: ")
result = phone_number.count("-")
print(result)

print("'-' count:", phone_number.count("-"))
print("' ' count:", phone_number.count(" "))
print("'(' count:", phone_number.count("("))
print("')' count:", phone_number.count(")"))

# Count flere tegn samlet
chars_to_count = ["-", " ", "(", ")"]
total = sum(phone_number.count(char) for char in chars_to_count)
print(f"Total count = {total}")

# count for hvert element i en liste:
for char in chars_to_count:
    print(f"{char!r}: {phone_number.count(char)}")

# Lagre i en dictionary:
counts = {char: phone_number.count(char) for char in chars_to_count}
print(counts)

# Telle alle tegn i hele strengen, ikke bare utvalgte:
counts = {}
for char in phone_number:
    counts[char] = counts.get(char, 0) + 1
print(counts)

# Enkleste måten er ofte dette:
phone_number = input("Phone-number: ")
chars_to_count = ["-", " ", "(", ")"]
counts = {char: phone_number.count(char) for char in chars_to_count}
toatl = sum(counts.values())

print("Counts per character:", counts)
print("Total:", total)

phone_number = phone_number.replace("-", " ")
print(f"Replaced '-' with ' ' using .replaced() = {phone_number}")


# OUTPUT:
# Name: Philip Elias Fleischer
# 22

# The char 'i' was found at index: 2 in the string, which is at place 3
# The char 'i' was found at index: 16 in the string, which is at place 17

# .lower() name:  philip elias fleischer
# Capitalized name: Philip elias fleischer
# Name in .upper(): PHILIP ELIAS FLEISCHER
# Is my name digits? =  False
# Is my name.isalpha()? =  False

# Phone-Number: 123-4567-8910
# 2
# '-' count: 2
# ' ' count: 0
# '(' count: 0
# ')' count: 0

# Total count = 2

# '-': 2
# ' ': 0
# '(': 0
# ')': 0

# {'-': 2, ' ': 0, '(': 0, ')': 0}

# {'1': 2, '2': 1, '3': 1, '-': 2, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1, '0': 1}

# Phone-number: 123-4567-8910
# Counts per character: {'-': 2, ' ': 0, '(': 0, ')': 0}
# Total: 2

# Replaced '-' with ' ' using .replaced() = 23 2 31 3
