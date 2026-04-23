# Static methods = A method that belong to a class rather than any object from that class (instance)
#                   Usually used for general utility functions

# Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility functions that do not need access to class data

class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions

def main():
    is_valid = Employee.is_valid_position("Project leader")
    print(f"Employee.is_valid_position('Project leader') = {is_valid}")
    is_valid = Employee.is_valid_position("Janitor")
    print(f"Employee.is_valid_position('Janitor') = {is_valid}")

    employee1 = Employee("Eugene", "Manager")
    employee2 = Employee("Squidward", "Cashier")
    employee3 = Employee("Spongebob", "Cook")

    print(f"employee1.get_info()-> {employee1.get_info()}")
    print(f"employee2.get_info()-> {employee2.get_info()}")
    print(f"employee3.get_info()-> {employee3.get_info()}")

if __name__ == "__main__":
    main()

#  OUTPUT:
# Employee.is_valid_position('Project leader') = False
# Employee.is_valid_position('Janitor') = True
# employee1.get_info()-> Eugene = Manager
# employee2.get_info()-> Squidward = Cashier
# employee3.get_info()-> Spongebob = Cook
