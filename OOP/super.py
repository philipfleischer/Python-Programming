# super() = Function used in a child class to call methods from a parent class (supercalss).
#           Allows you to extend functionality of the inherited methods

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'Not filled'}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        super().describe()
        print(f"It is a circle with an area of {round(3.14 * self.radius * self.radius, 4)} cm^2")


class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width


class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        print(f"It is a circle with an area of {self.width * self.height / 2} cm^2")
        super().describe()


def main():
    circle = Circle(color="Brown", is_filled=True, radius=10.98)
    print()
    print(f"circle.color = {circle.color}")
    print(f"circle.is_filled = {circle.is_filled}")
    print(f"circle.radius = {circle.radius}")
    print("circle.describe():")
    circle.describe()
    print()

    square = Square(color="Blue", is_filled=True, width=89)
    print()
    print(f"square.color = {square.color}")
    print(f"square.is_filled = {square.is_filled}")
    print(f"square.width = {square.width}")
    print("square.describe():")
    square.describe()
    print()

    triangle = Triangle(color="Orange", is_filled=False, width=9980, height=1)
    print()
    print(f"triangle.color = {triangle.color}")
    print(f"triangle.is_filled = {triangle.is_filled}")
    print(f"triangle.width = {triangle.width}")
    print(f"triangle.height = {triangle.height}")
    print("triangle.describe():")
    triangle.describe()
    print()

if __name__ == "__main__":
    main()
