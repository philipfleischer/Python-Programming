class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        #Person.number_of_people += 1
        Person.add_person()

    # Class methods
    @classmethod
    def number_of_peopleo(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1


def main():
    p1 = Person("Tim")
    print(p1.number_of_people)
    p2 = Person("Jim")
    print(Person.number_of_people)
    Person.number_of_people = 8
    print(p2.number_of_people)
    print(p1.number_of_people)

    # Class methods
    print(Person.number_of_peopleo())

if __name__ == "__main__":
    main()
