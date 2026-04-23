# Python weight converter

weight = float(input("Enter weigth: "))
unit = input("kg or lbs? (K or L): ")

if unit.lower() == "k":
    weight *= 2.205
    unit = "Lbs."
    print(f"Your weight is: {round(weight, 2)} {unit}")
elif unit.lower() == "l":
    weight /= 2.205
    unit = "Kgs."
    print(f"Your weight is: {round(weight, 2)} {unit}")
else:
    print(f"{unit} was not valid")
