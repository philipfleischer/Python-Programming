# multiple inheritance = inherit from more than one parent class
#                           C(A, B)
# multilevel inheritance = inherit from a parent which inherits from another parent
#                           C(B) <- B(A) <- A

class Animal:
    def __init__(self, name):
        self.name = name


    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

def main():
    rabbito = Rabbit("Buggy")
    hawkino = Hawk("Tony")
    fisher = Fish("Nemonimo")

    print()
    print("rabbito.flee() = ", end=" ")
    rabbito.flee()
    print("hawkino.hunt() = ", end=" ")
    hawkino.hunt()
    print("fisher.flee() = ", end=" ")
    fisher.flee()
    print("fisher.hunt() = ", end=" ")
    fisher.hunt()
    print()

    print("rabbito.eat() = ", end=" ")
    rabbito.eat()
    print("rabbito.sleep() = ", end=" ")
    rabbito.sleep()
    print("hawkino.eat() = ", end=" ")
    hawkino.eat()
    print("hawkino.sleep() = ", end=" ")
    hawkino.sleep()
    print("fisher.eat() = ", end=" ")
    fisher.eat()
    print("fisher.sleep() = ", end=" ")
    fisher.sleep()
    print()


if __name__ == "__main__":
    main()

# OUTPUT:
# rabbito.flee() =  Buggy is fleeing
# hawkino.hunt() =  Tony is hunting
# fisher.flee() =  Nemonimo is fleeing
# fisher.hunt() =  Nemonimo is hunting

# rabbito.eat() =  Buggy is eating
# rabbito.sleep() =  Buggy is sleeping
# hawkino.eat() =  Tony is eating
# hawkino.sleep() =  Tony is sleeping
# fisher.eat() =  Nemonimo is eating
# fisher.sleep() =  Nemonimo is sleeping
