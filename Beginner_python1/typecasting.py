# Typecasting = the process of converting a viariable from one data type to another
    # str(), int(), float(), bool()

name = "BRO dosa"
age = 24
gpa = 3.2
is_student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

age = float(age)
print(f"Age = {age} of changed from type int to type: {type(age)}")

age = str(age)
age = age + "1"
print(f"MY AGE: {age}")
