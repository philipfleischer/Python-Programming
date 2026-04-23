# Object Oriented Programming in Python

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(name)

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def add_one(self, x):
        return x+1

    def bark(self):
        print("bark")

def main():
    d = Dog("Svennskoi", 21)
    d.bark()
    d.get_age()
    print(type(d))  # -> <class '__main__.Dog'>
    print(type(Dog("DS", 22)))  # -> <class '__main__.Dog'>
    print(d.add_one(6))
    print(d.get_name())

    d2 = Dog("BOLLI", 83)
    print(d2.get_name())
    print(d2.get_age())
    d2.set_age(90)
    print(d2.get_age())



if __name__ == "__main__":
    main()
