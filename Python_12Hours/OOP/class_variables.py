# class variables = Shared ammong all instances of a class
#                   Defined outside the constructor
#                   Allow you to share data among all objects created from that class

class Student:

    class_year = 2026
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

def main():
    student1 = Student("Philip Elias Fleischer", 24)
    student2 = Student("John Wick", 54)

    print(f"student1.name = {student1.name}")
    print(f"student1.age = {student1.age}")
    # We can access the class variable like this:
    print(f"student1.class_year = {student1.class_year}")
    # But it is best practice to access class variables like this:
    print(f"Student.class_year = {Student.class_year}")
    print(f"Student.num_students = {Student.num_students}")
    print()

    print(f"student2.name = {student2.name}")
    print(f"student2.age = {student2.age}")
    print(f"Student.class_year = {Student.class_year}")
    print(f"Student.num_students = {Student.num_students}")
    print()

    student3 = Student("Hollay", 12)
    print(f"student2.name = {student3.name}")
    print(f"student2.age = {student3.age}")
    print(f"Student.class_year = {Student.class_year}")
    print(f"Student.num_students = {Student.num_students}")
    print()

    print(f"My graduating class of {Student.class_year} has {Student.num_students} students")
    print(student1.name)
    print(student2.name)
    print(student3.name)

if __name__ == "__main__":
    main()
