# 📚 Library Management System

A simple **Library Management System** built using Python to demonstrate core Object-Oriented Programming (OOP) concepts such as encapsulation, object relationships, and interaction between multiple classes.

---

## 🚀 Features

* ➕ Add Books
* 👨‍🎓 Add Students
* 📖 Issue Books to Students
* 🔄 Return Books
* 📚 View Available Books
* 📊 Track Issued Books

---

## 🧠 Concepts Used

* **Encapsulation** – Data and methods are wrapped inside classes
* **Object Relationships** – Students can have multiple issued books
* **Multiple Classes Interaction** – `Library`, `Book`, and `Student` work together

---

## 📁 Project Structure

```
library_management/
│
├── book.py        # Book class
├── student.py     # Student class
├── library.py     # Library logic (core functionality)
└── main.py        # Main program (entry point)
```

---

## 🏗️ Classes Overview

### 📘 Book

* Stores book details: ID, title, author
* Tracks whether the book is issued or available

### 👨‍🎓 Student

* Stores student details: ID and name
* Maintains a list of issued books

### 🏫 Library

* Manages books and students
* Handles issuing and returning of books
* Provides tracking and display functionality

---

## ▶️ How to Run

1. Clone the repository:

```
git clone https://github.com/your-username/library-management-system.git
```

2. Navigate to the project folder:

```
cd library-management-system
```

3. Run the program:

```
python main.py
```

---

## 💡 Example Usage

```
📚 Library Management System
1. Add Book
2. Add Student
3. View Books
4. Issue Book
5. Return Book
6. Track Issued Books
7. Exit
```

---

## 📌 Future Improvements

* ✅ Prevent duplicate book/student entries
* ✅ Add input validation
* ✅ Store data using JSON or a database
* ✅ Implement logging system
* ✅ Add GUI using Tkinter or Web Interface

---

## 🤝 Contributing

Feel free to fork this repository and improve the project. Contributions are always welcome!

---

## 📄 License

This project is open-source and free to use for educational purposes.

---

## 🙌 Author

**Palak Chandel**

---
