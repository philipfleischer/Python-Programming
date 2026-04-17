# conditional expression = A one-line shortcut for the if-else statement (tenary operator)
#                           Print or assign one of the two values based on a condition
#                           Return X if condition else Y

num = 5
print("Positive" if num > 0 else "Negative")
num = -3
print("Positive" if num > 0 else "Negative")

result = "EVEN" if num % 2 == 0 else "ODD"
print(result)

a = 6
b = 7

max_num = a if a > b else b
print(max_num)
min_num = a if a < b else b
print(min_num)

age = 25
status = "Adult" if age >= 18 else "Child"
print(status)

temp = 30
weather = "HOT" if temp > 20 else "COLD"
print(weather)

user_role = "admin"
access_level = "Full Access" if user_role == "admin" else "Limited Access"
print(access_level)

# OUTPUT:
# Positive
# Negative
# ODD
# 7
# 6
# Adult
# HOT
# Full Access
