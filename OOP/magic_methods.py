# Magic methods = Dunder methods (double underscore) __init__, __str__, __eq__
#                 They are automatically called by many of Python's built-in operations.
#                 They allow developers to define or customize the behavior of objects.


class Student:

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def __str__(self):
        return f"name: {self.name} gpa: {self.gpa}"

    def __eq__(self, other):
        return self.name == other.name

    def __gt__(self, other):
        return self.gpa > other.gpa


def run_student():
    student1 = Student("Spongebob", 3.2)
    student2 = Student("Patrick", 2.0)

    print(student1)
    print(student1 == student2)
    print(student1 > student2)


class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __eq__(self, other_book):
        return self.title == other_book.title and self.author == other_book.author

    def __lt__(self, other_book):
        return self.num_pages < other_book.num_pages

    def __gt__(self, other_book):
        return self.num_pages > other_book.num_pages

    def __add__(self, other_book):
        return self.num_pages + other_book.num_pages

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key '{key}' was not found"

    def __iter__(self):
        return iter([self.title, self.author, self.num_pages])


def run_book():
    book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
    book2 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 223)
    book3 = Book("The Lion, the Witch and the Wardrobe", "C.S. Lewis", 173)
    book4 = Book("The Hobbit", "J.R.R. Tolkien", 130)

    print("******** Print using __str__ automatically: *******")
    print(book1)
    print(book2)
    print(book3)

    print("******** Print equal boolean using __eq__ ******")
    print(f"book1 == book2 -> {book1 == book2}")
    print(f"book1 == book4 -> {book1 == book4}")

    print("******** Print LESS THAN using __lt__ ******")
    print(f"book2 < book3 -> {book2 < book3}")

    print("******** Print GREATER THAN using __gt__ ******")
    print(f"book2 > book3 -> {book2 > book3}")

    print("******** Print total num pages using __add__ ******")
    print(
        f"book1 ({book1.num_pages}) + book3 ({book3.num_pages}) -> {book1 + book3} pages"
    )

    print("******** Print boolean for keyword in title using __contains__ ******")
    print("Lion" in book3)
    print("Lewis" in book3)
    print("Lewis" in book2)

    print("******** Print item at index in Book() using __getitem__ ******")
    print(" Book titles:")
    print(book1["title"])
    print(book2["title"])
    print(book3["title"])

    print(" Book Authors: ")
    print(book1["author"])
    print(book2["author"])
    print(book3["author"])

    print(" Book number of pages:")
    print(book1["num_pages"])
    print(book2["num_pages"])
    print(book3["num_pages"])

    print(" Item non-existing scenario:")
    print(book3["motorcycle"])

    print("******** Print values using __iter__ ******")
    for value in book1:
        print(value)


def main():
    run_student()
    run_book()


if __name__ == "__main__":
    main()

# OUTPUT:
# name: Spongebob gpa: 3.2
# False
# True
# ******** Print using __str__ automatically: *******
# 'The Hobbit' by J.R.R. Tolkien
# 'Harry Potter and the Philosopher's Stone' by J.K. Rowling
# 'The Lion, the Witch and the Wardrobe' by C.S. Lewis
# ******** Print equal boolean using __eq__ ******
# book1 == book2 -> False
# book1 == book4 -> True
# ******** Print LESS THAN using __lt__ ******
# book2 < book3 -> False
# ******** Print GREATER THAN using __gt__ ******
# book2 > book3 -> True
# ******** Print total num pages using __add__ ******
# book1 (310) + book3 (173) -> 483 pages
# ******** Print boolean for keyword in title using __contains__ ******
# True
# True
# False
# ******** Print item at index in Book() using __getitem__ ******
#  Book titles:
# The Hobbit
# Harry Potter and the Philosopher's Stone
# The Lion, the Witch and the Wardrobe
#  Book Authors:
# J.R.R. Tolkien
# J.K. Rowling
# C.S. Lewis
#  Book number of pages:
# 310
# 223
# 173
#  Item non-existing scenario:
# Key 'motorcycle' was not found
# ******** Print values using __iter__ ******
# The Hobbit
# J.R.R. Tolkien
# 310
