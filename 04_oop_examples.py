"""
Object-Oriented Programming (OOP)
Classes, Objects, Inheritance, Encapsulation
"""

# ============================================
# 1. BASIC CLASS AND OBJECT
# ============================================
print("=" * 50)
print("1. BASIC CLASS AND OBJECT")
print("=" * 50)

class Student:
    # Class variable (shared by all instances)
    school = "XYZ University"
    
    def __init__(self, name, age, roll_no):
        # Instance variables (unique to each instance)
        self.name = name
        self.age = age
        self.roll_no = roll_no
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Roll No: {self.roll_no}")
        print(f"School: {Student.school}")

# Creating objects
student1 = Student("Jagdeep", 20, "CS101")
student2 = Student("Alice", 19, "CS102")

print("Student 1:")
student1.display_info()

print("\nStudent 2:")
student2.display_info()

# ============================================
# 2. CLASS WITH METHODS
# ============================================
print("\n" + "=" * 50)
print("2. CLASS WITH METHODS")
print("=" * 50)

class Calculator:
    def __init__(self):
        self.result = 0
    
    def add(self, a, b):
        self.result = a + b
        return self.result
    
    def subtract(self, a, b):
        self.result = a - b
        return self.result
    
    def multiply(self, a, b):
        self.result = a * b
        return self.result
    
    def divide(self, a, b):
        if b != 0:
            self.result = a / b
            return self.result
        else:
            return "Error: Division by zero"
    
    def get_result(self):
        return self.result

calc = Calculator()
print(f"5 + 3 = {calc.add(5, 3)}")
print(f"10 - 4 = {calc.subtract(10, 4)}")
print(f"6 * 7 = {calc.multiply(6, 7)}")
print(f"15 / 3 = {calc.divide(15, 3)}")
print(f"Last result: {calc.get_result()}")

# ============================================
# 3. INHERITANCE
# ============================================
print("\n" + "=" * 50)
print("3. INHERITANCE")
print("=" * 50)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Student2(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)  # Call parent constructor
        self.roll_no = roll_no
        self.course = course
    
    def display(self):  # Method overriding
        super().display()  # Call parent method
        print(f"Roll No: {self.roll_no}")
        print(f"Course: {self.course}")

class Teacher(Person):
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)
        self.subject = subject
        self.salary = salary
    
    def display(self):
        super().display()
        print(f"Subject: {self.subject}")
        print(f"Salary: ${self.salary}")

print("Student Information:")
student = Student2("Jagdeep", 20, "CS101", "Python")
student.display()

print("\nTeacher Information:")
teacher = Teacher("Dr. Smith", 45, "Computer Science", 75000)
teacher.display()

# ============================================
# 4. ENCAPSULATION (Public, Private)
# ============================================
print("\n" + "=" * 50)
print("4. ENCAPSULATION")
print("=" * 50)

class BankAccount:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.__balance = balance  # Private variable (name mangling)
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Invalid amount")
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: ${amount}")
            return True
        else:
            print("Insufficient balance or invalid amount")
            return False
    
    def get_balance(self):
        return self.__balance
    
    def display(self):
        print(f"Account No: {self.account_no}")
        print(f"Balance: ${self.__balance}")

account = BankAccount("123456789", 1000)
account.display()

print("\nTransactions:")
account.deposit(500)
account.withdraw(300)
account.withdraw(2000)  # Should fail
print(f"Current Balance: ${account.get_balance()}")

# ============================================
# 5. STUDENT GRADE MANAGEMENT SYSTEM
# ============================================
print("\n" + "=" * 50)
print("5. STUDENT GRADE MANAGEMENT SYSTEM")
print("=" * 50)

class GradeSystem:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.marks = {}
    
    def add_marks(self, subject, marks):
        if 0 <= marks <= 100:
            self.marks[subject] = marks
            print(f"Added {subject}: {marks}")
        else:
            print("Invalid marks (must be 0-100)")
    
    def calculate_total(self):
        return sum(self.marks.values())
    
    def calculate_percentage(self):
        if len(self.marks) == 0:
            return 0
        total = self.calculate_total()
        return (total / (len(self.marks) * 100)) * 100
    
    def get_grade(self):
        percentage = self.calculate_percentage()
        if percentage >= 90:
            return 'A+'
        elif percentage >= 80:
            return 'A'
        elif percentage >= 70:
            return 'B'
        elif percentage >= 60:
            return 'C'
        elif percentage >= 50:
            return 'D'
        else:
            return 'F'
    
    def display_report(self):
        print(f"\n{'='*40}")
        print(f"STUDENT REPORT CARD")
        print(f"{'='*40}")
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"\nSubject-wise Marks:")
        for subject, marks in self.marks.items():
            print(f"  {subject:15s}: {marks:3d}/100")
        print(f"{'-'*40}")
        print(f"Total Marks: {self.calculate_total()}/{len(self.marks) * 100}")
        print(f"Percentage: {self.calculate_percentage():.2f}%")
        print(f"Grade: {self.get_grade()}")
        print(f"{'='*40}")

# Create student and add marks
student = GradeSystem("Jagdeep", "CS101")
student.add_marks("Mathematics", 85)
student.add_marks("Physics", 90)
student.add_marks("Chemistry", 78)
student.add_marks("Computer Science", 95)
student.add_marks("English", 82)

student.display_report()

# ============================================
# 6. LIBRARY MANAGEMENT SYSTEM
# ============================================
print("\n" + "=" * 50)
print("6. LIBRARY MANAGEMENT SYSTEM")
print("=" * 50)

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = False
    
    def display(self):
        status = "Issued" if self.is_issued else "Available"
        print(f"ID: {self.book_id}, Title: '{self.title}', Author: {self.author}, Status: {status}")

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to library")
    
    def display_books(self):
        print(f"\nBooks in {self.name}:")
        if not self.books:
            print("  No books available")
        for book in self.books:
            print(f"  ", end="")
            book.display()
    
    def issue_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.is_issued:
                    book.is_issued = True
                    print(f"Book '{book.title}' issued successfully")
                    return True
                else:
                    print(f"Book '{book.title}' is already issued")
                    return False
        print(f"Book with ID {book_id} not found")
        return False
    
    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.is_issued:
                    book.is_issued = False
                    print(f"Book '{book.title}' returned successfully")
                    return True
                else:
                    print(f"Book '{book.title}' was not issued")
                    return False
        print(f"Book with ID {book_id} not found")
        return False

# Create library and add books
library = Library("City Library")

book1 = Book(101, "Python Programming", "John Doe")
book2 = Book(102, "Data Structures", "Jane Smith")
book3 = Book(103, "Algorithms", "Bob Johnson")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.display_books()

print("\nIssuing books:")
library.issue_book(101)
library.issue_book(102)

library.display_books()

print("\nReturning book:")
library.return_book(101)

library.display_books()

print("\n" + "=" * 50)
print("OOP EXAMPLES COMPLETE!")
print("=" * 50)
