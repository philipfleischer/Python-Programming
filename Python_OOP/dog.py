def somet():
    name = "Danny"
    age = 29

    print(type(name))   # <class 'str'>
    print(type(age))  # <class 'int'>
    print(name.upper()) # DANNY

class Dog:
    def __init__(self, name, breed, owner):
        self._name = name
        self._breed = breed
        self._owner = owner

    def bark(self):
        print("Whoof whoof")

class Owner:
    def __init__(self, name, address, contact_number):
        self._name = name
        self._address = address
        self._phone_number = contact_number

def main():
    own1 = Owner("Danny", "122 Spring", "09471209470129")
    dog1 = Dog("Bruce", "Scott Terr", own1)
    print(dog1._name)
    print(dog1._breed)
    dog1.bark()
    print(own1._name)
    print(own1._address)
    print(own1._phone_number)

    own2 = Owner("Sally", "23 dsadg", "9999999")
    dog2 = Dog("Freya", "Greyhound", own2)
    print(dog2._name)
    print(dog2._breed)
    dog2.bark()
    print(own2._name)
    print(own2._address)
    print(own2._phone_number)

if __name__ == "__main__":
    main()
