class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def greet(self):
        print(f"Hello my name is {self._name} and i am {self._age} years old")

def main():
    p1 = Person("Philip", 24)
    p1.greet()
    p2 = Person("Bob", 32)
    p2.greet()

if __name__ == "__main__":
    main()
