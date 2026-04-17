# indexing = accessing elements of a sequence using [] (indexing operator)
#               [start : end : step]

credit_number = "1234-5678-9012-3456"

print(f"credit card number at index 0: {credit_number[0]}")

# REMEMBER to count from indexes, not numbers
# Printing the 4 first chars using [0:4]
print(f"CC nums from idx 0-4 = {credit_number[0:4]}") # 1234
print(f"CC nums from idx 0-4 = {credit_number[0:6]}") # 1234-5
print(f"CC nums from idx 5-10 = {credit_number[5:10]}") # 5678-
print(f"CC nums from idx 5-11 = {credit_number[5:11]}") # 5678-9

# Give me everything after an index:
print(f"CC nums from idx 5 = {credit_number[5:]}")  # 5678-9012-3456

# Give me the last element in the string!
print(f"CC nums from idx -1 = {credit_number[-1]}")  # 6
print(f"CC nums from idx -1 = {credit_number[-3]}")  # 4

# Step 2, printer annenhver tall!
print(f"CC nums from idx 0-4 = {credit_number[0:6:2]}") # 13-
print(f"CC nums from idx 0-4 = {credit_number[0:7:2]}") # 13-6

# Step 2, print annenhert element:
print(credit_number[::2])  # 13-6891-46
# Step 3, print thirds element:
print(credit_number[::3])  # 146-136

# Get the last 4 digits from a credit card number:
last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")

# Reverse the string!
credit_number = credit_number[::-1]
print(f"Reversed credit number: {credit_number}")


# Output:
# credit card number at index 0: 1
# CC nums from idx 0-4 = 1234
# CC nums from idx 0-4 = 1234-5
# CC nums from idx 5-10 = 5678-
# CC nums from idx 5-11 = 5678-9
# CC nums from idx 5 = 5678-9012-3456
# CC nums from idx -1 = 6
# CC nums from idx -1 = 4
# CC nums from idx 0-4 = 13-
# CC nums from idx 0-4 = 13-6
# 13-6891-46
# 146-136
# XXXX-XXXX-XXXX-3456
# Reversed credit number: 6543-2109-8765-4321
