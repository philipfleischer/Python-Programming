# This is my first Python program
print("I like pizza!")

# A variable = A container for a value (String, Int, Float, Boolean)
# A variable behaves as if it was the value it contains

first_name = "Bro"
food = "pizza"
email = "som@live.no"

print(f"Hello {first_name}")
print(f"You like {food}")
print(f"You are {email}")

# Integers
age = 24
quantity = 3.5
num_stud = 123

print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Number of student: {num_stud}")

# FLoat
price = 10.99
gpa = 3.2
distance = 5.5

print(f"The price is ${price}")
print(f"The gpa is ${gpa}")
print(f"The dist is ${distance}")

# Boolean

is_student = True
for_sale = False

print(f"Are you a student? {is_student}")
if (is_student):
    print("YOu are stud")
else:
    print("YOu are NOT stud")

if for_sale:
    print("NO SALE")
else:
    print("IS SLAE")
