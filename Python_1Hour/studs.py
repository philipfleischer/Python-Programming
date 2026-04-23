# Object Oriented Programming in Python

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade

    def get_name(self):
        return self.name


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        total = 0
        for student in self.students:
            total += student.get_grade()
        return total / len(self.students)


def main():
    s1 = Student("Tim", 19, 95)
    s2 = Student("Bill", 19, 75)
    s3 = Student("Jill", 19, 65)

    course = Course("Science", 2)
    course.add_student(s1)
    course.add_student(s2)
    print(course.students)
    print(course.students[0].name)
    print(course.students[1].name)
    print(course.students[0].get_name())
    print(course.students[1].get_name())
    print(course.get_average_grade())
    print(course.add_student(s3))

if __name__ == "__main__":
    main()
