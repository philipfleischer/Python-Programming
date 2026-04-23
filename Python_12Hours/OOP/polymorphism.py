# Polymorphism = Greek word that means to "have many forms or faces"
#               Poly = many, Morphe = Form
#      TWO WAYS TO ACHIEVE POLYMORPHISM
#       1. Inheritance = An object could be treated of the same type as a parent class
#       2. "Duck typing" = Object must have necessary attributes/methods
from abc import ABC, abstractmethod

class Shape:

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5

class Pizza(Circle):
    def __init__(self, topping, radius):
        super().__init__(radius=radius)
        self.topping = topping

def main():
    shapes = [Circle(radius=4), Square(side=5), Triangle(base=6, height=7), Pizza(topping="Pepperoni", radius=15)]

    for shape in shapes:
        print(f"{shape.area()}cm^2")

if __name__ == "__main__":
    main()

# OUTPUT:
# 50.24cm^2
# 25cm^2
# 21.0cm^2
# 706.5cm^2
