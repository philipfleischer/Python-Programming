unit = input("Is this temp in C or F: ")
temp = float(input("Enter temp: "))

if unit.lower() == "c":
    temp = round((9*temp) / 5 + 32, 1)
    print(f"The temp in F is: {temp} F")
elif unit.lower() == "f":
    temp = round((temp -32) * 5 / 9, 1)
    print(f"The temp in C is: {temp} C")
else:
    print(f"{unit} is an invalid unit")
