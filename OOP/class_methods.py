# Class methods = Allow operations related to the class itself
#               Take (cls) as the first parameter, which represents the class itself

class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    # INSTANCE METHOD
    def get_info(self):
        return f"{self.name} {self.gpa}"

    # CLASS METHOD
    @classmethod
    def get_count(cls):
        return f"Total number og students: {cls.count}"

    @classmethod
    def get_avg_gpa(cls):
        if cls.count == 0:
            return 0
        return f"Average GPA for the students -> {round(cls.total_gpa / cls.count, 1)}"

def main():
    print(Student.get_count())
    student1 = Student("HEI", 3.2)
    student2 = Student("OLA", 3.4)
    student3 = Student("GINA", 4.9)
    print(Student.get_count())
    print(Student.get_avg_gpa())

if __name__ == "__main__":
    main()
