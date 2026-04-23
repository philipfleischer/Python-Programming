# "Duck typing" = Another way to achieve polymorphism besides Inheritance
#                   Object must have the minimum necessary attributes/methods
#                   "If it looks like a duck and quacks like a duck, it must be a duck."

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

# A Car looks like an animal and speaks like an animal
# Therefore A car is an animal
class Car:
    alive = False

    def speak(self):
        print("HONK!")

def main():
    animals = [Dog(), Cat(), Car()]

    for animal in animals:
        animal.speak()
        print(animal.alive)


if __name__ == "__main__":
    main()
