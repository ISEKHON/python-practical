"""
Data Structures - Lists, Tuples, Sets, Dictionaries
Practice Examples for Practical Exam
"""

# ============================================
# 1. LISTS
# ============================================
print("=" * 50)
print("1. LISTS (Mutable)")
print("=" * 50)

# Creating lists
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True]

print(f"Numbers: {numbers}")
print(f"Fruits: {fruits}")
print(f"Mixed: {mixed}")

# List operations
print("\nList Operations:")
fruits.append("orange")
print(f"After append: {fruits}")

fruits.insert(1, "mango")
print(f"After insert at index 1: {fruits}")

fruits.remove("banana")
print(f"After remove 'banana': {fruits}")

last = fruits.pop()
print(f"Popped: {last}, List: {fruits}")

# List methods
numbers = [5, 2, 8, 1, 9, 3]
print(f"\nOriginal: {numbers}")
numbers.sort()
print(f"Sorted: {numbers}")
numbers.reverse()
print(f"Reversed: {numbers}")

# List slicing
print(f"\nFirst 3 elements: {numbers[:3]}")
print(f"Last 3 elements: {numbers[-3:]}")
print(f"Every 2nd element: {numbers[::2]}")

# List comprehension
squares = [x**2 for x in range(1, 6)]
evens = [x for x in range(20) if x % 2 == 0]
print(f"\nSquares (1-5): {squares}")
print(f"Even numbers (0-19): {evens}")

# ============================================
# 2. TUPLES
# ============================================
print("\n" + "=" * 50)
print("2. TUPLES (Immutable)")
print("=" * 50)

# Creating tuples
coordinates = (10, 20)
person = ("Jagdeep", 20, "Student")
single = (5,)  # Note the comma

print(f"Coordinates: {coordinates}")
print(f"Person: {person}")
print(f"Single element tuple: {single}")

# Tuple unpacking
x, y = coordinates
name, age, role = person
print(f"\nUnpacked - x: {x}, y: {y}")
print(f"Name: {name}, Age: {age}, Role: {role}")

# Tuple operations
numbers = (1, 2, 3, 2, 4, 2, 5)
print(f"\nTuple: {numbers}")
print(f"Count of 2: {numbers.count(2)}")
print(f"Index of 3: {numbers.index(3)}")
print(f"Length: {len(numbers)}")

# ============================================
# 3. SETS
# ============================================
print("\n" + "=" * 50)
print("3. SETS (Unordered, Unique)")
print("=" * 50)

# Creating sets
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 5}
duplicates = {1, 2, 2, 3, 3, 4}  # Automatically removes duplicates

print(f"Fruits: {fruits}")
print(f"Numbers: {numbers}")
print(f"Duplicates removed: {duplicates}")

# Set operations
fruits.add("orange")
print(f"\nAfter add: {fruits}")

fruits.remove("banana")
print(f"After remove: {fruits}")

fruits.discard("mango")  # Won't error if not present
print(f"After discard (non-existent): {fruits}")

# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(f"\nSet A: {a}")
print(f"Set B: {b}")
print(f"Union (A | B): {a | b}")
print(f"Intersection (A & B): {a & b}")
print(f"Difference (A - B): {a - b}")
print(f"Symmetric Difference (A ^ B): {a ^ b}")

# ============================================
# 4. DICTIONARIES
# ============================================
print("\n" + "=" * 50)
print("4. DICTIONARIES (Key-Value Pairs)")
print("=" * 50)

# Creating dictionaries
student = {
    "name": "Jagdeep",
    "age": 20,
    "course": "Python",
    "roll_no": "CS101"
}

print("Student Dictionary:")
for key, value in student.items():
    print(f"  {key}: {value}")

# Accessing values
print(f"\nName: {student['name']}")
print(f"Age: {student.get('age')}")
print(f"Grade (default): {student.get('grade', 'N/A')}")

# Modifying dictionary
student["age"] = 21
student["grade"] = "A"
print(f"\nAfter modification: {student}")

# Dictionary methods
print(f"\nKeys: {list(student.keys())}")
print(f"Values: {list(student.values())}")
print(f"Items: {list(student.items())}")

# Dictionary comprehension
squares = {x: x**2 for x in range(1, 6)}
print(f"\nSquares dict: {squares}")

# ============================================
# 5. NESTED STRUCTURES
# ============================================
print("\n" + "=" * 50)
print("5. NESTED STRUCTURES")
print("=" * 50)

# List of dictionaries
students = [
    {"name": "Alice", "marks": 85},
    {"name": "Bob", "marks": 92},
    {"name": "Charlie", "marks": 78}
]

print("Students:")
for student in students:
    print(f"  {student['name']}: {student['marks']}")

# Dictionary of lists
courses = {
    "Math": [85, 90, 78],
    "Physics": [88, 92, 80],
    "Chemistry": [90, 85, 95]
}

print("\nCourse Marks:")
for course, marks in courses.items():
    avg = sum(marks) / len(marks)
    print(f"  {course}: {marks} (Avg: {avg:.2f})")

# ============================================
# 6. COMMON OPERATIONS
# ============================================
print("\n" + "=" * 50)
print("6. COMMON OPERATIONS")
print("=" * 50)

# List to Set (remove duplicates)
numbers = [1, 2, 2, 3, 3, 4, 5, 5]
unique = list(set(numbers))
print(f"Original: {numbers}")
print(f"Unique: {unique}")

# Sorting dictionary by value
student_marks = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 88}
sorted_students = sorted(student_marks.items(), key=lambda x: x[1], reverse=True)
print(f"\nStudents sorted by marks:")
for name, marks in sorted_students:
    print(f"  {name}: {marks}")

# Count frequency
text = "hello world"
frequency = {}
for char in text:
    if char != ' ':
        frequency[char] = frequency.get(char, 0) + 1
print(f"\nCharacter frequency in '{text}':")
for char, count in sorted(frequency.items()):
    print(f"  '{char}': {count}")

# ============================================
# 7. PRACTICAL EXAMPLES
# ============================================
print("\n" + "=" * 50)
print("7. PRACTICAL EXAMPLES")
print("=" * 50)

# Example 1: Find second largest
def find_second_largest(numbers):
    if len(numbers) < 2:
        return None
    unique = list(set(numbers))
    unique.sort(reverse=True)
    return unique[1] if len(unique) > 1 else None

numbers = [45, 23, 78, 12, 90, 34, 78]
print(f"Numbers: {numbers}")
print(f"Second largest: {find_second_largest(numbers)}")

# Example 2: Merge two dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = {**dict1, **dict2}
print(f"\nDict1: {dict1}")
print(f"Dict2: {dict2}")
print(f"Merged: {merged}")

# Example 3: List of even and odd numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in numbers if x % 2 == 0]
odds = [x for x in numbers if x % 2 != 0]
print(f"\nNumbers: {numbers}")
print(f"Evens: {evens}")
print(f"Odds: {odds}")

print("\n" + "=" * 50)
print("DATA STRUCTURES COMPLETE!")
print("=" * 50)
