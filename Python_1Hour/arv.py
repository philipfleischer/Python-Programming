# Inheritance - Two similar classes
# Dog and Cat

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I do not what I am")


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color} color")


class Dog(Animal):

    def speak(self):
        print("Bark")


class Fish(Animal):
    pass

def main():
    animal = Animal("Tim", 19)
    animal.show()
    # So even though Class Cat does not have an __init__ method, we can still make the instance of a 'cat'!
    cat = Cat("Bill", 42, "Black")
    # Even though cat does not have a .show() method, it can still use it since it inherits from Class Animal
    cat.show()
    dog = Dog("Jill", 25)
    dog.show()

    cat.speak()
    dog.speak()
    animal.speak()

    fish = Fish("OLLA", 90)
    fish.speak()

if __name__ == "__main__":
    main()
