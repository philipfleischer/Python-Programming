# object = A "bundle" of related attributes (variables) and methods (functions)
#           Ex. phone, cup, book
#           You need a "class" to create many objects
# class = (blueprint) used to design the structure and layout of an object

class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.color} {self.model}!")

    def stop(self):
        print(f"You stopped the {self.color} {self.model}!")

    def describe(self):
        print(f"{self.year} {self.color} {self.model}")


def main():
    car1 = Car("BMW", 1998, "Blue", True)

    print(car1.model)  # OUT -> BMW
    print(car1.year)  # OUT -> 1998
    print(car1.color)  # OUT -> Blue
    print(car1.for_sale)  # OUT -> True
    car1.drive()  # OUT -> You drive the Blue BMW!
    car1.describe()  # OUT -> 1998 Blue BMW
    print()

    car2 = Car("Corvette", 2026, "Yellow", False)
    print(car2.model)  # OUT -> Corvette
    print(car2.year)  # OUT -> 2026
    print(car2.color)  # OUT -> Yellow
    print(car2.for_sale)  # OUT -> False
    car2.stop()  # OUT -> You stopped the Yellow Corvette!
    car2.describe()  # OUT -> 2026 Yellow Corvette
    print()

if __name__ == "__main__":
    main()
