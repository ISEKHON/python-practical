# Python Practical Exam Revision Guide

**Student:** Jagdeep Singh  
**Roll Number:** 195  

---

## Table of Contents
1. [Python Basics](#python-basics)
2. [Data Types & Variables](#data-types--variables)
3. [Control Flow](#control-flow)
4. [Functions](#functions)
5. [Data Structures](#data-structures)
6. [File Handling](#file-handling)
7. [Object-Oriented Programming](#object-oriented-programming)
8. [Exception Handling](#exception-handling)
9. [Common Viva Questions](#common-viva-questions-detailed-explainations)
10. [Quick Tips for Implementation](#quick-tips-for-implementation)

---

## Python Basics

### What is Python?
- **Interpreted, high-level, general-purpose programming language**
- Created by Guido van Rossum (1991)
- Emphasizes code readability with significant whitespace
- Dynamically typed and garbage-collected

### Key Features
- Easy to learn and read
- Extensive standard library
- Cross-platform compatibility
- Supports multiple programming paradigms (procedural, OOP, functional)

---

## Data Types & Variables

### 1. Integer (int)
**Definition:** Whole numbers without decimal points (positive, negative, or zero)

**Characteristics:**
- No size limit (can be arbitrarily large)
- Immutable (cannot be changed in place)
- Supports all arithmetic operations

```python
# Integer examples
age = 25
negative = -10
large_number = 123456789012345678901234567890  # No limit!

# Arithmetic operations
a = 10
b = 3
print(a + b)    # Addition: 13
print(a - b)    # Subtraction: 7
print(a * b)    # Multiplication: 30
print(a / b)    # Division: 3.333... (returns float)
print(a // b)   # Floor division: 3 (returns int)
print(a % b)    # Modulus (remainder): 1
print(a ** b)   # Power: 1000

# Binary, Octal, Hexadecimal
binary = 0b1010     # Binary (prefix 0b) = 10
octal = 0o12        # Octal (prefix 0o) = 10
hexadecimal = 0xA   # Hexadecimal (prefix 0x) = 10

print(type(age))  # <class 'int'>
```

---

### 2. Float (float)
**Definition:** Numbers with decimal points or exponential notation

**Characteristics:**
- Used for decimal numbers
- Limited precision (~15-17 decimal places)
- Can represent very large/small numbers using scientific notation

```python
# Float examples
price = 99.99
pi = 3.14159
scientific = 1.5e3      # 1500.0 (1.5 × 10³)
small = 2.5e-4          # 0.00025 (2.5 × 10⁻⁴)

# Float operations
x = 5.5
y = 2.0
print(x + y)    # 7.5
print(x / y)    # 2.75
print(x // y)   # 2.0 (floor division, still returns float)
print(x ** y)   # 30.25

# Precision issues
print(0.1 + 0.2)  # 0.30000000000000004 (not exactly 0.3)

# Rounding
print(round(3.14159, 2))  # 3.14

print(type(price))  # <class 'float'>
```

---

### 3. String (str)
**Definition:** Sequence of characters enclosed in quotes (single, double, or triple)

**Characteristics:**
- Immutable (cannot change individual characters)
- Can be indexed and sliced
- Supports many built-in methods

```python
# String creation
name = "Jagdeep"              # Double quotes
message = 'Hello World'       # Single quotes
multiline = """This is
a multiline
string"""                     # Triple quotes
raw_string = r"C:\new\path"   # Raw string (ignores escape sequences)

# String indexing (0-based)
text = "Python"
print(text[0])      # 'P' (first character)
print(text[-1])     # 'n' (last character)
print(text[1:4])    # 'yth' (slicing: start to end-1)
print(text[:3])     # 'Pyt' (start to index 2)
print(text[3:])     # 'hon' (index 3 to end)
print(text[::-1])   # 'nohtyP' (reverse)

# String methods (returns new string, doesn't modify original)
text = "Python Programming"
print(text.upper())           # PYTHON PROGRAMMING
print(text.lower())           # python programming
print(text.capitalize())      # Python programming
print(text.title())           # Python Programming
print(text.swapcase())        # pYTHON pROGRAMMING

# Searching and replacing
print(text.find("Pro"))       # 7 (index of "Pro")
print(text.index("Pro"))      # 7 (raises error if not found)
print(text.count("o"))        # 2 (occurrences of 'o')
print(text.replace("Python", "Java"))  # Java Programming
print(text.startswith("Py"))  # True
print(text.endswith("ing"))   # True

# Splitting and joining
words = text.split()          # ['Python', 'Programming']
csv = "a,b,c,d"
items = csv.split(',')        # ['a', 'b', 'c', 'd']
joined = "-".join(words)      # Python-Programming

# Stripping whitespace
messy = "  hello  "
print(messy.strip())          # "hello" (removes leading/trailing spaces)
print(messy.lstrip())         # "hello  " (left strip)
print(messy.rstrip())         # "  hello" (right strip)

# Checking content
print("123".isdigit())        # True (all digits)
print("abc".isalpha())        # True (all alphabets)
print("abc123".isalnum())     # True (alphanumeric)
print("   ".isspace())        # True (all whitespace)

# String formatting
name = "Jagdeep"
age = 20
marks = 85.5

# Method 1: f-strings (Python 3.6+, recommended)
print(f"Name: {name}, Age: {age}, Marks: {marks:.1f}")

# Method 2: format()
print("Name: {}, Age: {}, Marks: {:.1f}".format(name, age, marks))

# Method 3: % formatting (old style)
print("Name: %s, Age: %d, Marks: %.1f" % (name, age, marks))

# String concatenation
first = "Hello"
last = "World"
combined = first + " " + last  # "Hello World"
repeated = "Hi" * 3            # "HiHiHi"

print(type(name))  # <class 'str'>
```

---

### 4. Boolean (bool)
**Definition:** Represents truth values: True or False

**Characteristics:**
- Only two values: True or False (capitalized)
- Result of comparisons and logical operations
- Internally: True = 1, False = 0

```python
# Boolean values
is_student = True
is_graduated = False

# Comparison operators (return boolean)
x = 10
y = 20
print(x == y)    # False (equal to)
print(x != y)    # True (not equal to)
print(x < y)     # True (less than)
print(x > y)     # False (greater than)
print(x <= y)    # True (less than or equal)
print(x >= y)    # False (greater than or equal)

# Logical operators
a = True
b = False
print(a and b)   # False (both must be True)
print(a or b)    # True (at least one must be True)
print(not a)     # False (negation)

# Truthy and Falsy values
# Falsy: False, 0, 0.0, "", [], {}, (), None
# Truthy: Everything else

print(bool(0))          # False
print(bool(1))          # True
print(bool(""))         # False (empty string)
print(bool("hello"))    # True (non-empty string)
print(bool([]))         # False (empty list)
print(bool([1, 2]))     # True (non-empty list)

# Using in conditions
if is_student:
    print("Enrolled")
else:
    print("Not enrolled")

# Boolean in arithmetic
print(True + True)   # 2 (True = 1)
print(True * 5)      # 5
print(False + 10)    # 10 (False = 0)

print(type(is_student))  # <class 'bool'>
```

---

### 5. NoneType (None)
**Definition:** Represents absence of value or null value

**Characteristics:**
- Only one value: None
- Often used as default value or to indicate "no value"
- Different from 0, False, or empty string

```python
# None examples
result = None
user_input = None

# Checking for None (use 'is', not '==')
if result is None:
    print("No result yet")

if result is not None:
    print("Result exists")

# Common use cases
def find_item(items, target):
    for item in items:
        if item == target:
            return item
    return None  # Not found

# Function with no return statement returns None
def greet():
    print("Hello")

result = greet()  # result = None

# None in comparisons
print(None == None)   # True
print(None is None)   # True (preferred)

print(type(result))  # <class 'NoneType'>
```

---

### Type Conversion (Casting)

**Definition:** Converting one data type to another

```python
# String to Integer
num_str = "123"
num_int = int(num_str)      # 123
print(type(num_int))        # <class 'int'>

# Invalid conversion raises ValueError
# int("abc")  # ERROR: ValueError

# String to Float
price_str = "99.99"
price_float = float(price_str)  # 99.99

# Integer to Float
x = 5
y = float(x)                # 5.0

# Float to Integer (truncates decimal)
pi = 3.14
pi_int = int(pi)            # 3 (not rounded, just truncated)

# Number to String
age = 20
age_str = str(age)          # "20"

# String to List
text = "hello"
char_list = list(text)      # ['h', 'e', 'l', 'l', 'o']

# String to Boolean
print(bool(""))             # False (empty string)
print(bool("False"))        # True (non-empty string, even "False"!)
print(bool("0"))            # True (non-empty string)

# List to Tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)   # (1, 2, 3)

# Tuple to List
my_tuple = (4, 5, 6)
my_list = list(my_tuple)    # [4, 5, 6]

# List to Set (removes duplicates)
numbers = [1, 2, 2, 3, 3, 4]
unique = set(numbers)       # {1, 2, 3, 4}

# Set to List
my_set = {5, 6, 7}
my_list = list(my_set)      # [5, 6, 7] (order not guaranteed)

# ASCII conversions
print(ord('A'))             # 65 (character to ASCII)
print(chr(65))              # 'A' (ASCII to character)
```

---

### Type Checking

```python
# Using type()
x = 10
print(type(x))              # <class 'int'>
print(type(x) == int)       # True

# Using isinstance() (preferred, handles inheritance)
print(isinstance(x, int))   # True
print(isinstance(x, (int, float)))  # True (check multiple types)

# Checking multiple types
value = "hello"
if isinstance(value, str):
    print("It's a string")

# Type checking examples
data = [10, "hello", 3.14, True, None]
for item in data:
    print(f"{item} is {type(item).__name__}")

# Output:
# 10 is int
# hello is str
# 3.14 is float
# True is bool
# None is NoneType
```

---

## Control Flow

### If-Elif-Else
```python
marks = 85

if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
else:
    print("Grade: C")
```

### Loops

#### For Loop
```python
# Iterate through range
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# Iterate through list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Enumerate for index and value
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

#### While Loop
```python
count = 0
while count < 5:
    print(count)
    count += 1

# While with break and continue
i = 0
while i < 10:
    i += 1
    if i == 3:
        continue  # Skip 3
    if i == 8:
        break     # Stop at 8
    print(i)
```

---

## Functions

### Basic Function
```python
def greet(name):
    """This is a docstring"""
    return f"Hello, {name}!"

# Function call
result = greet("Jagdeep")
```

### Default Arguments
```python
def power(base, exponent=2):
    return base ** exponent

print(power(5))      # 25 (default exponent=2)
print(power(5, 3))   # 125
```

### Variable Arguments
```python
# *args for variable positional arguments
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4, 5))  # 15

# **kwargs for variable keyword arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Jagdeep", age=20, city="Delhi")
```

### Lambda Functions
```python
# Anonymous functions
square = lambda x: x ** 2
add = lambda a, b: a + b

print(square(5))     # 25
print(add(3, 7))     # 10

# Common use with map, filter
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))
```

---

## Data Structures

### Comparison Table

| Feature | List | Tuple | Set | Dictionary |
|---------|------|-------|-----|------------|
| Syntax | `[]` | `()` | `{}` or `set()` | `{k:v}` |
| Ordered | ✓ Yes | ✓ Yes | ✗ No | ✓ Yes (3.7+) |
| Mutable | ✓ Yes | ✗ No | ✓ Yes | ✓ Yes |
| Duplicates | ✓ Allowed | ✓ Allowed | ✗ No | Keys: ✗ No |
| Indexed | ✓ Yes | ✓ Yes | ✗ No | By key |
| Use Case | Dynamic data | Fixed data | Unique items | Key-value mapping |

---

### 1. LISTS - Detailed

**Definition:** Mutable, ordered collection that allows duplicates

```python
# CREATING LISTS
empty = []
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True, [1, 2]]  # Can mix types
duplicate = [1, 2, 2, 3, 3, 3]  # Duplicates OK

# ACCESSING (0-indexed)
fruits = ["apple", "banana", "cherry", "date"]
print(fruits[0])       # 'apple' (first)
print(fruits[-1])      # 'date' (last)
print(fruits[1:3])     # ['banana', 'cherry'] (slicing)
print(fruits[::-1])    # Reverse order

# MODIFYING
fruits[1] = "blueberry"        # Change element
fruits[1:3] = ["mango"]        # Replace slice

# LIST METHODS - Complete

# 1. append(x) - Add single element to end
nums = [1, 2, 3]
nums.append(4)                 # [1, 2, 3, 4]
nums.append([5, 6])            # [1, 2, 3, 4, [5, 6]]

# 2. extend(iterable) - Add all elements from iterable
nums = [1, 2, 3]
nums.extend([4, 5])            # [1, 2, 3, 4, 5]
nums.extend("AB")              # [1, 2, 3, 4, 5, 'A', 'B']

# 3. insert(i, x) - Insert at index
fruits = ["apple", "cherry"]
fruits.insert(1, "banana")     # ['apple', 'banana', 'cherry']

# 4. remove(x) - Remove first occurrence
nums = [1, 2, 3, 2, 4]
nums.remove(2)                 # [1, 3, 2, 4] (first 2 removed)

# 5. pop([i]) - Remove and return at index (default: last)
nums = [10, 20, 30]
last = nums.pop()              # 30, list: [10, 20]
first = nums.pop(0)            # 10, list: [20]

# 6. clear() - Remove all
nums.clear()                   # []

# 7. index(x) - Find first index
fruits = ["apple", "banana", "cherry"]
idx = fruits.index("banana")   # 1

# 8. count(x) - Count occurrences
nums = [1, 2, 2, 3, 2]
count = nums.count(2)          # 3

# 9. sort() - Sort in place
nums = [3, 1, 4, 1, 5]
nums.sort()                    # [1, 1, 3, 4, 5]
nums.sort(reverse=True)        # [5, 4, 3, 1, 1]

# 10. reverse() - Reverse in place
nums = [1, 2, 3]
nums.reverse()                 # [3, 2, 1]

# 11. copy() - Shallow copy
original = [1, 2, 3]
copied = original.copy()

# LIST OPERATIONS
list1 + list2                  # Concatenation
list1 * 3                      # Repetition
x in list1                     # Membership
len(list1)                     # Length
min(nums), max(nums), sum(nums)  # Min, max, sum

# LIST COMPREHENSION
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
labels = ["Even" if x % 2 == 0 else "Odd" for x in range(5)]
```

---

### 2. TUPLES - Detailed

**Definition:** Immutable, ordered collection that allows duplicates

```python
# CREATING TUPLES
empty = ()
single = (5,)                  # Comma required!
numbers = (1, 2, 3, 4, 5)
mixed = (1, "hello", 3.14)
coordinates = 10, 20           # Parentheses optional

# ACCESSING (same as lists)
colors = ("red", "green", "blue")
print(colors[0])               # 'red'
print(colors[-1])              # 'blue'
print(colors[1:])              # ('green', 'blue')

# IMMUTABLE - Cannot modify
# colors[0] = "orange"         # ERROR!
# colors.append("yellow")      # ERROR!

# TUPLE METHODS (only 2!)
nums = (1, 2, 3, 2, 4, 2)
nums.count(2)                  # 3
nums.index(3)                  # 2

# TUPLE UNPACKING
coords = (10, 20, 30)
x, y, z = coords               # x=10, y=20, z=30

# Swap variables
a, b = 5, 10
a, b = b, a                    # a=10, b=5

# Extended unpacking
nums = (1, 2, 3, 4, 5)
first, *middle, last = nums    # first=1, middle=[2,3,4], last=5

# WHY TUPLES?
# - Faster than lists
# - Protect data from modification
# - Can be dict keys
# - Return multiple values from functions
```

---

### 3. SETS - Detailed

**Definition:** Mutable, unordered collection with no duplicates

```python
# CREATING SETS
empty = set()                  # Note: {} creates dict!
numbers = {1, 2, 3, 4, 5}
duplicates = {1, 2, 2, 3}      # {1, 2, 3} (auto-remove)

# From list (remove duplicates)
unique = set([1, 2, 2, 3, 3])  # {1, 2, 3}

# NO INDEXING
# print(numbers[0])            # ERROR! Unordered

# SET METHODS

# Adding
s = {1, 2, 3}
s.add(4)                       # {1, 2, 3, 4}
s.update([5, 6, 7])            # Add multiple

# Removing
s.remove(2)                    # ERROR if not found
s.discard(10)                  # No error if not found
s.pop()                        # Remove random element
s.clear()                      # Empty set

# SET OPERATIONS
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

a | b            # Union: {1, 2, 3, 4, 5, 6, 7, 8}
a & b            # Intersection: {4, 5}
a - b            # Difference: {1, 2, 3}
a ^ b            # Symmetric diff: {1, 2, 3, 6, 7, 8}

# Checking relationships
{1, 2} <= {1, 2, 3}           # Subset: True
{1, 2, 3} >= {1, 2}           # Superset: True
{1, 2}.isdisjoint({3, 4})    # No common: True

# SET COMPREHENSION
evens = {x for x in range(20) if x % 2 == 0}
```

---

### 4. DICTIONARIES - Detailed

**Definition:** Mutable collection of key-value pairs (ordered in Python 3.7+)

```python
# CREATING DICTIONARIES
empty = {}
student = {
    "name": "Jagdeep",
    "age": 20,
    "course": "Python",
    "marks": [85, 90, 78]
}

# Different ways to create
d = dict(name="Jagdeep", age=20)
d = dict([("name", "Jagdeep"), ("age", 20)])

# ACCESSING
student["name"]                # 'Jagdeep' (KeyError if not exists)
student.get("name")            # 'Jagdeep'
student.get("grade", "N/A")    # 'N/A' (default if not exists)

# MODIFYING
student["age"] = 21            # Update
student["grade"] = "A"         # Add new
student.update({"roll": "CS101", "age": 22})

# DICTIONARY METHODS

# Getting keys, values, items
student.keys()                 # dict_keys(['name', 'age', ...])
student.values()               # dict_values(['Jagdeep', 22, ...])
student.items()                # dict_items([('name', 'Jagdeep'), ...])

# Removing
age = student.pop("age")       # Remove and return (KeyError if not exists)
last = student.popitem()       # Remove last item
student.clear()                # Remove all

# Other useful methods
student.setdefault("age", 20)  # Get or set default
d = dict.fromkeys(["a", "b"], 0)  # {'a': 0, 'b': 0}

# ITERATING
for key in student:            # Iterate keys
    print(key)

for value in student.values(): # Iterate values
    print(value)

for key, value in student.items():  # Iterate pairs (most common)
    print(f"{key}: {value}")

# DICTIONARY COMPREHENSION
squares = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# NESTED DICTIONARIES
students = {
    "CS101": {"name": "Jagdeep", "marks": 85},
    "CS102": {"name": "Alice", "marks": 92}
}
print(students["CS101"]["name"])  # 'Jagdeep'

# SORTING DICTIONARY
marks = {"Alice": 85, "Bob": 92, "Charlie": 78}
sorted_by_key = dict(sorted(marks.items()))
sorted_by_value = dict(sorted(marks.items(), key=lambda x: x[1], reverse=True))
```

---

## File Handling

### Reading Files
```python
# Method 1: Using with statement (recommended)
with open("file.txt", "r") as file:
    content = file.read()  # Read entire file
    print(content)

# Read line by line
with open("file.txt", "r") as file:
    for line in file:
        print(line.strip())

# Read all lines into a list
with open("file.txt", "r") as file:
    lines = file.readlines()
```

### Writing Files
```python
# Write mode (overwrites)
with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("Python Programming\n")

# Append mode
with open("output.txt", "a") as file:
    file.write("Additional line\n")

# Writing multiple lines
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("output.txt", "w") as file:
    file.writelines(lines)
```

### File Modes
- `'r'` - Read (default)
- `'w'` - Write (creates new or overwrites)
- `'a'` - Append
- `'r+'` - Read and write
- `'b'` - Binary mode (e.g., `'rb'`, `'wb'`)

---

## Object-Oriented Programming

### Classes and Objects
```python
class Student:
    # Class variable
    school = "XYZ University"
    
    # Constructor
    def __init__(self, name, age, roll_no):
        # Instance variables
        self.name = name
        self.age = age
        self.roll_no = roll_no
        self.grades = []
    
    # Instance method
    def add_grade(self, grade):
        self.grades.append(grade)
    
    def get_average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Roll No: {self.roll_no}")
        print(f"Average: {self.get_average():.2f}")

# Creating objects
student1 = Student("Jagdeep", 20, "CS101")
student1.add_grade(85)
student1.add_grade(90)
student1.add_grade(78)
student1.display_info()
```

### Inheritance
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)  # Call parent constructor
        self.roll_no = roll_no
    
    def display(self):  # Method overriding
        super().display()
        print(f"Roll No: {self.roll_no}")

student = Student("Jagdeep", 20, "CS101")
student.display()
```

### Encapsulation
```python
class BankAccount:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.__balance = balance  # Private variable (name mangling)
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False
    
    def get_balance(self):
        return self.__balance

account = BankAccount("123456", 1000)
account.deposit(500)
print(account.get_balance())
```

---

## Exception Handling

### Try-Except
```python
try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print(f"Result: {result}")
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("Operation successful!")  # Runs if no exception
finally:
    print("This always executes")   # Always runs
```

### Raising Exceptions
```python
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age < 18:
        raise Exception("Must be 18 or older")
    return True

try:
    check_age(15)
except ValueError as e:
    print(f"ValueError: {e}")
except Exception as e:
    print(f"Error: {e}")
```

---

## Common Viva Questions Detailed Explainations

### 1. What is Python? What are its features?
**Answer:** 
Python is a **high-level, interpreted, object-oriented programming language** created by Guido van Rossum in 1991. 

**Detailed Features:**
- **Interpreted:** Code is executed line by line, no compilation needed
- **Dynamically Typed:** No need to declare variable types explicitly
- **Easy Syntax:** Readable and resembles English, uses indentation
- **Extensive Libraries:** Large standard library + third-party packages (NumPy, Pandas, etc.)
- **Cross-Platform:** Runs on Windows, Mac, Linux without modification
- **Multi-Paradigm:** Supports procedural, OOP, and functional programming
- **Automatic Memory Management:** Garbage collection handles memory automatically
- **Free and Open Source:** Community-driven development

**Example:**
```python
# No type declaration needed (dynamically typed)
name = "Jagdeep"  # String
age = 20          # Integer - type automatically determined
```

---

### 2. What is the difference between list and tuple?
**Answer:**

| Feature | List | Tuple |
|---------|------|-------|
| **Mutability** | Mutable (can be changed) | Immutable (cannot be changed) |
| **Syntax** | Square brackets `[]` | Parentheses `()` |
| **Speed** | Slower | Faster |
| **Memory** | More memory | Less memory |
| **Methods** | Many methods (append, remove, etc.) | Few methods (count, index) |
| **Use Case** | Dynamic data that changes | Fixed data that shouldn't change |

**Example:**
```python
# List - Mutable
my_list = [1, 2, 3]
my_list[0] = 10  # ✓ Works - can modify
my_list.append(4)  # ✓ Can add elements

# Tuple - Immutable
my_tuple = (1, 2, 3)
my_tuple[0] = 10  # ✗ ERROR - cannot modify
# my_tuple.append(4)  # ✗ ERROR - no append method
```

**When to use which?**
- **List:** Shopping cart items, student marks (data that changes)
- **Tuple:** Coordinates (x, y), database records (fixed data)

---

### 3. What is the difference between `==` and `is`?
**Answer:**

**`==` (Equality Operator):**
- Compares **values** of two objects
- Returns True if values are equal
- Checks "Are they equivalent?"

**`is` (Identity Operator):**
- Compares **memory locations** (object identity)
- Returns True if both variables point to same object
- Checks "Are they the same object?"

**Example:**
```python
# Values comparison (==)
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True (same values)
print(a is b)  # False (different objects in memory)

# Identity comparison (is)
c = a
print(a is c)  # True (both point to same object)

# Small integers (cached by Python)
x = 5
y = 5
print(x == y)  # True (same value)
print(x is y)  # True (Python caches small integers)
```

**Memory Visualization:**
```
a → [1, 2, 3] (Memory location: 0x1000)
b → [1, 2, 3] (Memory location: 0x2000)  # Different objects
c → points to same location as 'a' (0x1000)  # Same object
```

---

### 4. What are *args and **kwargs?
**Answer:**

**`*args` (Non-keyword Arguments):**
- Accepts **variable number of positional arguments**
- Arguments packed into a **tuple**
- Name "args" is convention (can be anything with *)

**`**kwargs` (Keyword Arguments):**
- Accepts **variable number of keyword arguments**
- Arguments packed into a **dictionary**
- Name "kwargs" is convention (can be anything with **)

**Detailed Example:**
```python
# *args example
def sum_numbers(*args):
    print(f"Received {len(args)} arguments")
    print(f"Type: {type(args)}")  # <class 'tuple'>
    print(f"Values: {args}")
    return sum(args)

result = sum_numbers(1, 2, 3, 4, 5)
# Output:
# Received 5 arguments
# Type: <class 'tuple'>
# Values: (1, 2, 3, 4, 5)
# Result: 15

# **kwargs example
def print_student_info(**kwargs):
    print(f"Type: {type(kwargs)}")  # <class 'dict'>
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_student_info(name="Jagdeep", age=20, course="Python", roll="CS101")
# Output:
# Type: <class 'dict'>
# name: Jagdeep
# age: 20
# course: Python
# roll: CS101

# Combining both
def combined_function(regular_arg, *args, **kwargs):
    print(f"Regular: {regular_arg}")
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

combined_function("Hello", 1, 2, 3, name="Jagdeep", age=20)
# Output:
# Regular: Hello
# Args: (1, 2, 3)
# Kwargs: {'name': 'Jagdeep', 'age': 20}
```

---

### 5. What is list comprehension?
**Answer:** 
List comprehension is a **concise way to create lists** in a single line using a compact syntax instead of traditional for loops.

**Syntax:** `[expression for item in iterable if condition]`

**Traditional vs Comprehension:**
```python
# Traditional approach
squares = []
for x in range(10):
    squares.append(x**2)

# List comprehension (same result, one line)
squares = [x**2 for x in range(10)]

# With condition
# Traditional
evens = []
for x in range(20):
    if x % 2 == 0:
        evens.append(x)

# Comprehension
evens = [x for x in range(20) if x % 2 == 0]
```

**More Examples:**
```python
# String manipulation
words = ["hello", "world", "python"]
uppercase = [word.upper() for word in words]
# Result: ['HELLO', 'WORLD', 'PYTHON']

# Nested comprehension
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
# Result: [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

# With if-else
numbers = [1, 2, 3, 4, 5]
result = ["Even" if x % 2 == 0 else "Odd" for x in numbers]
# Result: ['Odd', 'Even', 'Odd', 'Even', 'Odd']
```

---

### 6. What is the difference between `append()` and `extend()`?
**Answer:**

**`append()`:**
- Adds **single element** to end of list
- Element added as-is (even if it's a list)
- List length increases by 1

**`extend()`:**
- Adds **all elements from an iterable** to end of list
- Unpacks the iterable and adds each element
- List length increases by number of elements in iterable

**Detailed Example:**
```python
# append() - adds single element
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)  # ['apple', 'banana', 'cherry']

# append() with a list (adds the entire list as one element)
fruits.append(["mango", "orange"])
print(fruits)  # ['apple', 'banana', 'cherry', ['mango', 'orange']]
print(len(fruits))  # 4 (list within list)

# extend() - adds all elements from iterable
numbers = [1, 2, 3]
numbers.extend([4, 5, 6])
print(numbers)  # [1, 2, 3, 4, 5, 6]

numbers.extend("ABC")  # String is iterable
print(numbers)  # [1, 2, 3, 4, 5, 6, 'A', 'B', 'C']

# Visual comparison
list1 = [1, 2]
list1.append([3, 4])     # [1, 2, [3, 4]] - length 3
list2 = [1, 2]
list2.extend([3, 4])     # [1, 2, 3, 4] - length 4
```

---

### 7. What is inheritance?
**Answer:** 
Inheritance is an **OOP concept** where a new class (child/derived class) **inherits properties and methods** from an existing class (parent/base class), promoting **code reusability**.

**Types of Inheritance:**
1. **Single Inheritance:** One parent, one child
2. **Multiple Inheritance:** Multiple parents, one child
3. **Multilevel Inheritance:** Chain of inheritance (grandparent → parent → child)
4. **Hierarchical Inheritance:** One parent, multiple children

**Detailed Example:**
```python
# Base/Parent Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Derived/Child Class
class Student(Person):  # Inherits from Person
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)  # Call parent constructor
        self.roll_no = roll_no  # Additional attribute
    
    def display(self):  # Method overriding
        super().display()  # Call parent method
        print(f"Roll No: {self.roll_no}")

# Usage
student = Student("Jagdeep", 20, "CS101")
student.display()
# Output:
# Name: Jagdeep, Age: 20
# Roll No: CS101

# Student has access to Person's attributes and methods
# Plus its own additional features
```

**Benefits:**
- Code reusability (don't repeat common code)
- Logical hierarchy (represents real-world relationships)
- Easy maintenance (change parent, all children benefit)

---

### 8. What is encapsulation?
**Answer:** 
Encapsulation is **bundling data (attributes) and methods together** in a class and **restricting direct access** to some components to prevent accidental modification.

**Access Levels in Python:**
1. **Public:** Accessible everywhere (default)
2. **Protected:** Single underscore `_variable` (convention, not enforced)
3. **Private:** Double underscore `__variable` (name mangling)

**Detailed Example:**
```python
class BankAccount:
    def __init__(self, account_no, balance):
        self.account_no = account_no      # Public
        self._branch = "Main"             # Protected (convention)
        self.__balance = balance          # Private (name mangling)
    
    # Public method to access private data
    def get_balance(self):
        return self.__balance
    
    # Public method to modify private data (with validation)
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}")
        else:
            print("Invalid amount")
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn ${amount}")
        else:
            print("Insufficient funds or invalid amount")

# Usage
account = BankAccount("123456", 1000)

# Direct access to public attribute
print(account.account_no)  # 123456

# Direct access to private fails
# print(account.__balance)  # ERROR: AttributeError

# Access through public method (controlled access)
print(account.get_balance())  # 1000

# Modification through public method (with validation)
account.deposit(500)     # ✓ Allowed (positive amount)
account.withdraw(2000)   # ✗ Prevented (exceeds balance)
account.deposit(-100)    # ✗ Prevented (negative amount)
```

**Why Encapsulation?**
- **Data hiding:** Protect sensitive data
- **Validation:** Control how data is modified
- **Flexibility:** Change internal implementation without affecting outside code
- **Maintainability:** Centralized control of data access

---

### 9. What is polymorphism?
**Answer:** 
Polymorphism means **"many forms"** - the ability of different objects to respond to the **same method call in different ways**.

**Types:**
1. **Method Overriding:** Child class redefines parent's method
2. **Method Overloading:** Multiple methods with same name (not directly supported in Python)

**Detailed Example:**
```python
# Base class
class Shape:
    def area(self):
        pass  # To be implemented by child classes

# Different shapes implement area() differently
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):  # Specific implementation for Rectangle
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):  # Specific implementation for Circle
        return 3.14 * self.radius ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):  # Specific implementation for Triangle
        return 0.5 * self.base * self.height

# Polymorphism in action
shapes = [
    Rectangle(5, 3),
    Circle(7),
    Triangle(4, 6)
]

# Same method call, different behavior based on object type
for shape in shapes:
    print(f"{shape.__class__.__name__} area: {shape.area()}")

# Output:
# Rectangle area: 15
# Circle area: 153.86
# Triangle area: 12.0
```

**Benefits:**
- **Flexibility:** Same interface, different implementations
- **Code reusability:** Write generic code that works with multiple types
- **Extensibility:** Add new types without changing existing code

---

### 10. What is the difference between `remove()`, `del`, and `pop()`?
**Answer:**

| Method | Purpose | Returns | Raises Error If... |
|--------|---------|---------|-------------------|
| `remove(value)` | Remove first occurrence of value | Nothing (None) | Value not found |
| `del list[index]` | Delete element at index | Nothing | Index out of range |
| `pop(index)` | Remove and return element | Removed element | Index out of range |

**Detailed Examples:**
```python
# remove() - removes by VALUE
fruits = ["apple", "banana", "cherry", "banana"]
fruits.remove("banana")  # Removes FIRST occurrence
print(fruits)  # ['apple', 'cherry', 'banana']

fruits.remove("mango")  # ERROR: ValueError (not in list)

# del - removes by INDEX
numbers = [10, 20, 30, 40, 50]
del numbers[2]  # Removes element at index 2 (30)
print(numbers)  # [10, 20, 40, 50]

del numbers[10]  # ERROR: IndexError (index out of range)

# Can also delete slices or entire list
del numbers[1:3]  # Delete slice
del numbers       # Delete entire list

# pop() - removes by INDEX and RETURNS value
colors = ["red", "green", "blue", "yellow"]
removed = colors.pop(1)  # Removes index 1, returns "green"
print(removed)  # green
print(colors)   # ['red', 'blue', 'yellow']

last = colors.pop()  # No index = removes last element
print(last)     # yellow
print(colors)   # ['red', 'blue']

colors.pop(10)  # ERROR: IndexError
```

**When to use which?**
- **`remove()`:** When you know the value but not the position
- **`del`:** When you know the position and don't need the value
- **`pop()`:** When you need both remove AND get the value

---

### 11. What is the purpose of `__init__` method?
**Answer:** 
`__init__` is a **special method (constructor)** that is **automatically called** when an object is created. It **initializes the object's attributes**.

**Key Points:**
- Called automatically when you create an object
- First parameter must be `self` (refers to the instance)
- Used to set initial values for attributes
- Not required (Python creates default if not defined)
- Double underscores indicate "dunder" (magic) method

**Detailed Example:**
```python
class Student:
    # Constructor
    def __init__(self, name, age, roll_no):
        # Initialize instance variables
        self.name = name
        self.age = age
        self.roll_no = roll_no
        self.marks = []  # Default empty list
        print(f"Student object created for {name}")
    
    def add_marks(self, mark):
        self.marks.append(mark)

# When you create object, __init__ is called automatically
student1 = Student("Jagdeep", 20, "CS101")
# Output: Student object created for Jagdeep

# Each object has its own attributes
student2 = Student("Alice", 19, "CS102")
# Output: Student object created for Alice

print(student1.name)  # Jagdeep
print(student2.name)  # Alice
```

**With Default Values:**
```python
class BankAccount:
    def __init__(self, account_no, balance=0):  # Default balance
        self.account_no = account_no
        self.balance = balance

# Can create with or without balance
acc1 = BankAccount("123")       # balance defaults to 0
acc2 = BankAccount("456", 1000) # balance set to 1000
```

---

### 12. What is `self` in Python?
**Answer:** 
`self` is a **reference to the current instance** of the class. It's used to **access instance variables and methods** within the class.

**Key Points:**
- **Not a keyword** (just a convention, can use any name)
- **Must be first parameter** in instance methods
- **Automatically passed** by Python (you don't pass it when calling)
- **Refers to the specific object** calling the method

**Detailed Example:**
```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand    # Instance variable
        self.model = model    # Instance variable
        self.speed = 0        # Instance variable
    
    def accelerate(self, increase):
        self.speed += increase  # Access instance variable using self
        print(f"{self.brand} {self.model} speed: {self.speed} km/h")
    
    def display_info(self):
        # self refers to current object
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Speed: {self.speed}")

# Create two different objects
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")

# When you call car1.accelerate(50):
# Python automatically passes car1 as self
car1.accelerate(50)  # self = car1
# Output: Toyota Camry speed: 50 km/h

car2.accelerate(30)  # self = car2
# Output: Honda Civic speed: 30 km/h

# Each object maintains its own state
print(car1.speed)  # 50
print(car2.speed)  # 30
```

**Why "self"?**
```python
class Example:
    def method(self, value):
        self.value = value  # Stores in instance
        # Without self, would be local variable

obj1 = Example()
obj2 = Example()

obj1.method(10)
obj2.method(20)

print(obj1.value)  # 10 (each object has its own value)
print(obj2.value)  # 20
```

---

### 13. What are modules in Python?
**Answer:** 
A module is a **file containing Python code** (functions, classes, variables) that can be **imported and reused** in other programs.

**Types:**
1. **Built-in modules:** Part of Python (math, random, os, sys)
2. **User-defined modules:** Created by you
3. **Third-party modules:** Installed via pip (numpy, pandas)

**Detailed Example:**

**Creating a module (mymodule.py):**
```python
# mymodule.py
def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

PI = 3.14159

class Calculator:
    def multiply(self, a, b):
        return a * b
```

**Using the module:**
```python
# main.py
# Method 1: Import entire module
import mymodule
print(mymodule.greet("Jagdeep"))
print(mymodule.add(5, 3))
print(mymodule.PI)

# Method 2: Import specific items
from mymodule import greet, add
print(greet("Alice"))
print(add(10, 20))

# Method 3: Import with alias
import mymodule as mm
print(mm.greet("Bob"))

# Method 4: Import everything (not recommended)
from mymodule import *
print(PI)
```

**Built-in Module Examples:**
```python
import math
print(math.sqrt(16))    # 4.0
print(math.pi)          # 3.141592653589793

import random
print(random.randint(1, 10))  # Random number 1-10

import os
print(os.getcwd())  # Current directory
```

**Benefits:**
- **Code organization:** Break large programs into smaller files
- **Reusability:** Use same code in multiple programs
- **Namespace management:** Avoid name conflicts

---

### 14. What is the difference between `break` and `continue`?
**Answer:**

**`break`:**
- **Exits the loop completely**
- No more iterations execute
- Control goes to first statement after loop

**`continue`:**
- **Skips current iteration only**
- Jumps to next iteration
- Loop continues with next value

**Detailed Examples:**
```python
# break - exits loop completely
print("break example:")
for i in range(1, 11):
    if i == 5:
        print(f"Breaking at {i}")
        break  # Exit loop
    print(i)
# Output: 1, 2, 3, 4, Breaking at 5
# Loop stops completely at 5

print("\ncontinue example:")
for i in range(1, 11):
    if i == 5:
        print(f"Skipping {i}")
        continue  # Skip to next iteration
    print(i)
# Output: 1, 2, 3, 4, Skipping 5, 6, 7, 8, 9, 10
# Loop continues after skipping 5

# Practical example: break
print("\nFinding first even number:")
numbers = [1, 3, 7, 8, 9, 10, 11]
for num in numbers:
    if num % 2 == 0:
        print(f"Found first even: {num}")
        break  # Stop searching once found
# Output: Found first even: 8

# Practical example: continue
print("\nPrinting only odd numbers:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:
        continue  # Skip even numbers
    print(num)
# Output: 1, 3, 5, 7, 9
```

**With while loop:**
```python
# break with while
count = 0
while True:  # Infinite loop
    count += 1
    if count == 5:
        break  # Exit infinite loop
    print(count)
# Output: 1, 2, 3, 4

# continue with while
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue  # Skip even numbers
    print(count)
# Output: 1, 3, 5, 7, 9
```

---

### 15. What is exception handling?
**Answer:** 
Exception handling is a mechanism to **handle runtime errors gracefully** without crashing the program, using **try-except blocks**.

**Why needed?**
- Prevents program crash
- Provides user-friendly error messages
- Allows recovery from errors
- Separates error-handling code from normal code

**Structure:**
```python
try:
    # Code that might cause error
except ExceptionType:
    # Code to handle the error
else:
    # Executes if no exception (optional)
finally:
    # Always executes (optional)
```

**Detailed Examples:**
```python
# Without exception handling (program crashes)
num = int(input("Enter number: "))  # If user enters "abc" → CRASH!
result = 100 / num  # If user enters 0 → CRASH!

# With exception handling (graceful)
try:
    num = int(input("Enter number: "))
    result = 100 / num
    print(f"Result: {result}")
except ValueError:
    print("Please enter a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"Unexpected error: {e}")
else:
    print("Operation successful!")
finally:
    print("Thank you for using calculator")
```

**Common Exceptions:**
```python
# ValueError - invalid type conversion
try:
    int("abc")  # Cannot convert
except ValueError as e:
    print(f"ValueError: {e}")

# ZeroDivisionError - division by zero
try:
    10 / 0
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}")

# FileNotFoundError - file doesn't exist
try:
    open("nonexistent.txt")
except FileNotFoundError as e:
    print(f"FileNotFoundError: {e}")

# IndexError - invalid index
try:
    lst = [1, 2, 3]
    print(lst[10])
except IndexError as e:
    print(f"IndexError: {e}")

# KeyError - key not in dictionary
try:
    d = {"name": "Jagdeep"}
    print(d["age"])
except KeyError as e:
    print(f"KeyError: {e}")
```

**Raising Exceptions:**
```python
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age < 18:
        raise Exception("Must be 18 or older")
    return True

try:
    check_age(15)
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Error: {e}")
```

---

## Quick Tips for Implementation

### 1. Always Start Clean
```python
# Clear variable names
# Proper indentation (4 spaces)
# Comments where necessary
```

### 2. Test Your Code
```python
# Use print statements to debug
# Test edge cases (empty lists, zero, negative numbers)
# Verify output format
```

### 3. Common Patterns

#### Pattern 1: Reading Input
```python
# Single input
name = input("Enter your name: ")

# Multiple inputs in one line
a, b = map(int, input("Enter two numbers: ").split())

# List input
numbers = list(map(int, input("Enter numbers: ").split()))
```

#### Pattern 2: Prime Number Check
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

#### Pattern 3: Factorial
```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# Iterative version
def factorial_iter(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
```

#### Pattern 4: Fibonacci Series
```python
def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b
```

#### Pattern 5: Palindrome Check
```python
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]
```

#### Pattern 6: Sorting
```python
# List sorting
numbers.sort()              # In-place
sorted_nums = sorted(numbers)  # Returns new list

# Custom sorting
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
students.sort(key=lambda x: x[1], reverse=True)  # Sort by marks
```

### 4. Common Implementation Tasks

#### Task: Find largest element in list
```python
numbers = [45, 23, 78, 12, 90, 34]
largest = max(numbers)
# OR
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
```

#### Task: Count vowels in string
```python
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count
```

#### Task: Reverse a string
```python
text = "Python"
reversed_text = text[::-1]  # nohtyP
# OR
reversed_text = ''.join(reversed(text))
```

#### Task: Remove duplicates from list
```python
numbers = [1, 2, 3, 2, 4, 1, 5]
unique = list(set(numbers))  # Order not preserved
# OR (preserves order)
unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)
```

---

## Practice Problems

### Problem 1: Calculator
```python
def calculator():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Enter operation (+, -, *, /): ")
    
    if op == '+':
        print(f"Result: {num1 + num2}")
    elif op == '-':
        print(f"Result: {num1 - num2}")
    elif op == '*':
        print(f"Result: {num1 * num2}")
    elif op == '/':
        if num2 != 0:
            print(f"Result: {num1 / num2}")
        else:
            print("Error: Division by zero")
    else:
        print("Invalid operation")
```

### Problem 2: Student Grade System
```python
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.marks = {}
    
    def add_marks(self, subject, marks):
        self.marks[subject] = marks
    
    def calculate_percentage(self):
        if len(self.marks) == 0:
            return 0
        total = sum(self.marks.values())
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
        else:
            return 'F'
    
    def display(self):
        print(f"\nStudent Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print("Marks:")
        for subject, marks in self.marks.items():
            print(f"  {subject}: {marks}")
        print(f"Percentage: {self.calculate_percentage():.2f}%")
        print(f"Grade: {self.get_grade()}")
```

### Problem 3: File Operations - Word Counter
```python
def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        print(f"File '{filename}' not found")
        return 0
```

---

## Final Checklist Before Exam

- [ ] Understand basic syntax and indentation
- [ ] Know all data types and their methods
- [ ] Practice if-else, loops (for, while)
- [ ] Write functions with different types of arguments
- [ ] Work with lists, tuples, sets, dictionaries
- [ ] Understand file handling (read/write)
- [ ] Know OOP concepts (class, object, inheritance)
- [ ] Practice exception handling
- [ ] Review common algorithms (sorting, searching)
- [ ] Test code with different inputs

---

## Quick Reference Commands

```python
# Input/Output
input()                    # Get user input
print()                    # Display output

# Type conversion
int(), float(), str(), list(), tuple(), set(), dict()

# String methods
.upper(), .lower(), .strip(), .split(), .replace(), .find()

# List methods
.append(), .extend(), .insert(), .remove(), .pop(), .sort(), .reverse()

# Dictionary methods
.keys(), .values(), .items(), .get(), .update()

# Built-in functions
len(), max(), min(), sum(), range(), enumerate(), zip()
map(), filter(), sorted(), reversed()

# File operations
open(), .read(), .readline(), .readlines(), .write(), .close()
```

---

## Good Luck! 🎓

**Remember:**
- Read the question carefully
- Plan before coding
- Use meaningful variable names
- Comment your code
- Test with sample inputs
- Handle edge cases
- Stay calm and confident

**You've got this!**
