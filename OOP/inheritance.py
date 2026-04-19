# Inheritance = Allows a class to inherit attributes and methods from another class
#               Helps with code reusability and extensibility
#               class Child(Parent)

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True
    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("Meow?")

class Mouse(Animal):
    def speak(self):
        print("Squeak!?")

def main():
    dog = Dog("Scooby")
    cat = Cat("Garfield")
    mouse = Mouse("Mickey")

    print()
    print("--------- DOG -----------")
    print(f"Dogs name, dog.name = {dog.name}")
    print(f"Dog is alive?, dog.is_alive = {dog.is_alive}")
    dog.eat()
    dog.sleep()
    dog.speak()

    print()
    print("--------- CAT -----------")
    print(f"Cats name, cat.name = {cat.name}")
    print(f"Cat is alive?, cat.is_alive = {cat.is_alive}")
    cat.eat()
    cat.sleep()
    cat.speak()

    print()
    print("--------- MOUSE -----------")
    print(f"Mouses name, mouse.name = {mouse.name}")
    print(f"Mouse is alive?, mouse.is_alive = {mouse.is_alive}")
    mouse.eat()
    mouse.sleep()
    mouse.speak()


if __name__ == "__main__":
    main()
