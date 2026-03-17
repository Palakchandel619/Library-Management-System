class Library:
    def __init__(self):
        self.books = {}
        self.students = {}

    # Add Book
    def add_book(self, book):
        if book.book_id in self.books:
            print("Book ID already exists!")
        else:
            self.books[book.book_id] = book
            print("Book added successfully.")

    # Add Student
    def add_student(self, student):
        if student.student_id in self.students:
            print("Student ID already exists!")
        else:
            self.students[student.student_id] = student
            print("Student added successfully.")

    # Issue Book
    def issue_book(self, book_id, student_id):
        if book_id not in self.books:
            print("Book not found!")
            return
        if student_id not in self.students:
            print("Student not found!")
            return

        book = self.books[book_id]
        student = self.students[student_id]

        if book.is_issued:
            print("Book already issued!")
        else:
            book.is_issued = True
            student.issued_books.append(book)
            print("Book issued successfully.")

    # Return Book
    def return_book(self, book_id, student_id):
        if book_id not in self.books or student_id not in self.students:
            print("Invalid ID!")
            return

        book = self.books[book_id]
        student = self.students[student_id]

        if book in student.issued_books:
            book.is_issued = False
            student.issued_books.remove(book)
            print("Book returned successfully.")
        else:
            print("This student didn't issue this book.")

    # View Available Books
    def view_available_books(self):
        print("\nAvailable Books:")
        for book in self.books.values():
            if not book.is_issued:
                print(book)

    # View Issued Books
    def view_issued_books(self):
        print("\nIssued Books:")
        for student in self.students.values():
            if student.issued_books:
                print(f"\n{student.name} has:")
                for book in student.issued_books:
                    print(book)