class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.issued_books = []

    def __str__(self):
        return f"{self.student_id} - {self.name}"