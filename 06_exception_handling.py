"""
Exception Handling Examples
Try-Except-Else-Finally, Raising Exceptions
"""

# ============================================
# 1. BASIC EXCEPTION HANDLING
# ============================================
print("=" * 50)
print("1. BASIC EXCEPTION HANDLING")
print("=" * 50)

# Division by zero
print("Example: Division")
try:
    num1 = 10
    num2 = 0
    result = num1 / num2
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# ValueError
print("\nExample: Invalid type conversion")
try:
    number = int("hello")
    print(number)
except ValueError:
    print("Error: Cannot convert 'hello' to integer!")

# ============================================
# 2. MULTIPLE EXCEPT BLOCKS
# ============================================
print("\n" + "=" * 50)
print("2. MULTIPLE EXCEPT BLOCKS")
print("=" * 50)

def safe_division(a, b):
    try:
        result = a / b
        print(f"{a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        print("Error: Division by zero!")
        return None
    except TypeError:
        print("Error: Invalid types for division!")
        return None

print("Test 1: Normal division")
safe_division(10, 2)

print("\nTest 2: Division by zero")
safe_division(10, 0)

print("\nTest 3: Invalid types")
safe_division("10", 2)

# ============================================
# 3. TRY-EXCEPT-ELSE-FINALLY
# ============================================
print("\n" + "=" * 50)
print("3. TRY-EXCEPT-ELSE-FINALLY")
print("=" * 50)

def read_number():
    try:
        # Simulating input
        num = int("25")  # Change to "abc" to see error
        print(f"Number entered: {num}")
    except ValueError:
        print("Error: Invalid input!")
    else:
        print("Else block: No exception occurred")
    finally:
        print("Finally block: This always executes")

print("Reading valid number:")
read_number()

# ============================================
# 4. CATCHING GENERIC EXCEPTIONS
# ============================================
print("\n" + "=" * 50)
print("4. CATCHING GENERIC EXCEPTIONS")
print("=" * 50)

def process_data(data):
    try:
        # Multiple operations that might fail
        result = int(data) * 2
        value = result / 10
        output = str(value)
        return output
    except ValueError as e:
        print(f"ValueError: {e}")
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return None

print("Test 1: Valid data")
result = process_data("50")
print(f"Result: {result}")

print("\nTest 2: Invalid data")
result = process_data("abc")
print(f"Result: {result}")

# ============================================
# 5. RAISING EXCEPTIONS
# ============================================
print("\n" + "=" * 50)
print("5. RAISING EXCEPTIONS")
print("=" * 50)

def check_age(age):
    """Validate age and raise exceptions"""
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age < 18:
        raise Exception("Must be 18 or older")
    return True

def test_age(age):
    try:
        check_age(age)
        print(f"Age {age} is valid")
    except ValueError as e:
        print(f"ValueError: {e}")
    except Exception as e:
        print(f"Error: {e}")

print("Test 1: Valid age (25)")
test_age(25)

print("\nTest 2: Underage (15)")
test_age(15)

print("\nTest 3: Negative age (-5)")
test_age(-5)

# ============================================
# 6. FILE HANDLING WITH EXCEPTIONS
# ============================================
print("\n" + "=" * 50)
print("6. FILE HANDLING WITH EXCEPTIONS")
print("=" * 50)

def read_file_safe(filename):
    """Read file with comprehensive error handling"""
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"Successfully read {len(content)} characters")
            return content
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
    except PermissionError:
        print(f"Error: No permission to read '{filename}'")
    except IOError as e:
        print(f"IO Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return None

print("Attempting to read non-existent file:")
read_file_safe("nonexistent.txt")

# ============================================
# 7. CUSTOM EXCEPTION
# ============================================
print("\n" + "=" * 50)
print("7. CUSTOM EXCEPTIONS")
print("=" * 50)

class InsufficientBalanceError(Exception):
    """Custom exception for insufficient balance"""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Insufficient balance: ${balance} < ${amount}")

class InvalidAmountError(Exception):
    """Custom exception for invalid amount"""
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def withdraw(self, amount):
        try:
            if amount <= 0:
                raise InvalidAmountError("Amount must be positive")
            if amount > self.balance:
                raise InsufficientBalanceError(self.balance, amount)
            
            self.balance -= amount
            print(f"Withdrawn ${amount}. New balance: ${self.balance}")
            return True
            
        except InvalidAmountError as e:
            print(f"Invalid Amount Error: {e}")
            return False
        except InsufficientBalanceError as e:
            print(f"Insufficient Balance: {e}")
            return False

account = BankAccount(1000)

print("Test 1: Valid withdrawal")
account.withdraw(300)

print("\nTest 2: Insufficient balance")
account.withdraw(1500)

print("\nTest 3: Invalid amount (negative)")
account.withdraw(-100)

print("\nTest 4: Invalid amount (zero)")
account.withdraw(0)

# ============================================
# 8. CALCULATOR WITH EXCEPTION HANDLING
# ============================================
print("\n" + "=" * 50)
print("8. CALCULATOR WITH EXCEPTION HANDLING")
print("=" * 50)

class Calculator:
    @staticmethod
    def divide(a, b):
        try:
            if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
                raise TypeError("Both arguments must be numbers")
            if b == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return a / b
        except TypeError as e:
            print(f"Type Error: {e}")
            return None
        except ZeroDivisionError as e:
            print(f"Division Error: {e}")
            return None
    
    @staticmethod
    def power(base, exponent):
        try:
            if not isinstance(base, (int, float)) or not isinstance(exponent, (int, float)):
                raise TypeError("Both arguments must be numbers")
            result = base ** exponent
            if result == float('inf'):
                raise OverflowError("Result is too large")
            return result
        except TypeError as e:
            print(f"Type Error: {e}")
            return None
        except OverflowError as e:
            print(f"Overflow Error: {e}")
            return None

print("Division tests:")
print(f"10 / 2 = {Calculator.divide(10, 2)}")
print(f"10 / 0 = {Calculator.divide(10, 0)}")
print(f"'10' / 2 = {Calculator.divide('10', 2)}")

print("\nPower tests:")
print(f"2 ^ 3 = {Calculator.power(2, 3)}")
print(f"10 ^ 1000 = {Calculator.power(10, 1000)}")

# ============================================
# 9. INPUT VALIDATION WITH EXCEPTIONS
# ============================================
print("\n" + "=" * 50)
print("9. INPUT VALIDATION")
print("=" * 50)

def get_positive_integer(value):
    """Validate and return positive integer"""
    try:
        num = int(value)
        if num <= 0:
            raise ValueError("Number must be positive")
        return num
    except ValueError as e:
        print(f"Validation Error: {e}")
        return None

def get_valid_grade(value):
    """Validate grade (0-100)"""
    try:
        grade = float(value)
        if grade < 0 or grade > 100:
            raise ValueError("Grade must be between 0 and 100")
        return grade
    except ValueError as e:
        print(f"Validation Error: {e}")
        return None

print("Integer validation:")
print(f"Value '25': {get_positive_integer('25')}")
print(f"Value '-5': {get_positive_integer('-5')}")
print(f"Value 'abc': {get_positive_integer('abc')}")

print("\nGrade validation:")
print(f"Grade '85': {get_valid_grade('85')}")
print(f"Grade '105': {get_valid_grade('105')}")
print(f"Grade 'A+': {get_valid_grade('A+')}")

# ============================================
# 10. COMPREHENSIVE EXAMPLE
# ============================================
print("\n" + "=" * 50)
print("10. STUDENT MANAGEMENT WITH EXCEPTIONS")
print("=" * 50)

class Student:
    def __init__(self, name, roll_no):
        if not name or not isinstance(name, str):
            raise ValueError("Name must be a non-empty string")
        if not roll_no or not isinstance(roll_no, str):
            raise ValueError("Roll number must be a non-empty string")
        
        self.name = name
        self.roll_no = roll_no
        self.grades = {}
    
    def add_grade(self, subject, grade):
        try:
            if not isinstance(subject, str):
                raise TypeError("Subject must be a string")
            if not isinstance(grade, (int, float)):
                raise TypeError("Grade must be a number")
            if grade < 0 or grade > 100:
                raise ValueError("Grade must be between 0 and 100")
            
            self.grades[subject] = grade
            print(f"Added {subject}: {grade}")
            return True
            
        except (TypeError, ValueError) as e:
            print(f"Error adding grade: {e}")
            return False
    
    def get_average(self):
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)

# Test student management
try:
    student = Student("Jagdeep", "CS101")
    student.add_grade("Math", 85)
    student.add_grade("Physics", 90)
    student.add_grade("Chemistry", 105)  # Invalid
    student.add_grade("English", "A")     # Invalid
    
    print(f"\nAverage grade: {student.get_average():.2f}")
    
except ValueError as e:
    print(f"Student creation error: {e}")

print("\n" + "=" * 50)
print("EXCEPTION HANDLING COMPLETE!")
print("=" * 50)
