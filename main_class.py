class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = False

    def __str__(self):
        status = "Issued" if self.is_issued else "Available"
        return f"[{self.book_id}] {self.title} by {self.author} - {status}"


class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.issued_books = []

    def __str__(self):
        return f"{self.student_id} - {self.name}"


class Library:
    def __init__(self):
        self.books = {}
        self.students = {}

    def add_book(self, book):
        self.books[book.book_id] = book
        print("Book added successfully!")

    def add_student(self, student):
        self.students[student.student_id] = student
        print("Student added successfully!")

    def issue_book(self, book_id, student_id):
        if book_id in self.books and student_id in self.students:
            book = self.books[book_id]
            student = self.students[student_id]

            if not book.is_issued:
                book.is_issued = True
                student.issued_books.append(book)
                print("Book issued successfully!")
            else:
                print("Book already issued!")
        else:
            print("Invalid book or student ID!")

    def return_book(self, book_id, student_id):
        if book_id in self.books and student_id in self.students:
            book = self.books[book_id]
            student = self.students[student_id]

            if book in student.issued_books:
                book.is_issued = False
                student.issued_books.remove(book)
                print("Book returned successfully!")
            else:
                print("Book was not issued to this student!")
        else:
            print("Invalid book or student ID!")

    def view_available_books(self):
        print("\nAvailable Books:")
        for book in self.books.values():
            if not book.is_issued:
                print(book)

    def view_issued_books(self):
        print("\nIssued Books:")
        for student in self.students.values():
            if student.issued_books:
                print(f"{student.name}:")
                for book in student.issued_books:
                    print(book)


def main():
    library = Library()

    while True:
        print("\n===== Library Management System =====")
        print("1. Add Book")
        print("2. Add Student")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. View Available Books")
        print("6. View Issued Books")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Enter Book ID: ")
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            library.add_book(Book(book_id, title, author))

        elif choice == "2":
            student_id = input("Enter Student ID: ")
            name = input("Enter Name: ")
            library.add_student(Student(student_id, name))

        elif choice == "3":
            book_id = input("Enter Book ID: ")
            student_id = input("Enter Student ID: ")
            library.issue_book(book_id, student_id)

        elif choice == "4":
            book_id = input("Enter Book ID: ")
            student_id = input("Enter Student ID: ")
            library.return_book(book_id, student_id)

        elif choice == "5":
            library.view_available_books()

        elif choice == "6":
            library.view_issued_books()

        elif choice == "7":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()