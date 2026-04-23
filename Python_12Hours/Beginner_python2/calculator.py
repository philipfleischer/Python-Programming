# Python calculator

operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))
print(num1 + num2)

if operator == "+":
    result = num1 + num2
    print(f"Reusult of add {num1} and {num2} = {round(result, 2)}")
elif operator == "-":
    result = num1 - num2
    print(f"Reusult of sub {num1} and {num2} = {round(result, 2)}")
elif operator == "*":
    result = num1 * num2
    print(f"Reusult of multiply {num1} and {num2} = {round(result, 2)}")
elif operator == "/":
    result = num1 / num2
    print(f"Reusult of divide {num1} and {num2} = {round(result, 2)}")
else:
    print(f"The operator {operator} is not valid")
