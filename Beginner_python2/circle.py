import math

# Circumference
radius = float(input("Enter the radius of a circle: "))
circumference = 2 * math.pi * radius
print(f"The circumference is: {round(circumference, 2)}cm")

# Area
radius = float(input("Enter the radius: "))
area = math.pi * pow(radius, 2)
print(f"The area of the circle is: {round(area, 2)}cm^2")

# Hypotenus of right angle triangle
a = float(input("Enter side A: "))
b = float(input("Enter side B: "))
c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"Side C = {c}")
