"""
Python Basics - Practice Examples
Run each section to understand the concepts
"""

# ============================================
# 1. VARIABLES AND DATA TYPES
# ============================================
print("=" * 50)
print("1. VARIABLES AND DATA TYPES")
print("=" * 50)

name = "Jagdeep"
age = 20
height = 5.9
is_student = True

print(f"Name: {name} (type: {type(name).__name__})")
print(f"Age: {age} (type: {type(age).__name__})")
print(f"Height: {height} (type: {type(height).__name__})")
print(f"Is Student: {is_student} (type: {type(is_student).__name__})")

# ============================================
# 2. STRING OPERATIONS
# ============================================
print("\n" + "=" * 50)
print("2. STRING OPERATIONS")
print("=" * 50)

text = "Python Programming"
print(f"Original: {text}")
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
print(f"Length: {len(text)}")
print(f"First 6 chars: {text[:6]}")
print(f"Reversed: {text[::-1]}")
print(f"Split: {text.split()}")

# ============================================
# 3. ARITHMETIC OPERATIONS
# ============================================
print("\n" + "=" * 50)
print("3. ARITHMETIC OPERATIONS")
print("=" * 50)

a, b = 10, 3
print(f"a = {a}, b = {b}")
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Floor Division: {a} // {b} = {a // b}")
print(f"Modulus: {a} % {b} = {a % b}")
print(f"Power: {a} ** {b} = {a ** b}")

# ============================================
# 4. CONDITIONAL STATEMENTS
# ============================================
print("\n" + "=" * 50)
print("4. CONDITIONAL STATEMENTS")
print("=" * 50)

marks = 85
if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "F"

print(f"Marks: {marks} -> Grade: {grade}")

# ============================================
# 5. LOOPS
# ============================================
print("\n" + "=" * 50)
print("5. LOOPS")
print("=" * 50)

# For loop
print("For loop (0 to 4):")
for i in range(5):
    print(i, end=" ")
print()

# While loop
print("\nWhile loop (countdown from 5):")
count = 5
while count > 0:
    print(count, end=" ")
    count -= 1
print()

# Loop with list
print("\nIterating through list:")
fruits = ["Apple", "Banana", "Cherry"]
for fruit in fruits:
    print(f"- {fruit}")

# ============================================
# 6. TYPE CONVERSION
# ============================================
print("\n" + "=" * 50)
print("6. TYPE CONVERSION")
print("=" * 50)

num_str = "123"
num_int = int(num_str)
num_float = float(num_str)

print(f"String: '{num_str}' -> Int: {num_int}, Float: {num_float}")
print(f"Int to String: {str(456)}")
print(f"Float to Int: {int(3.14)}")

# ============================================
# 7. INPUT HANDLING
# ============================================
print("\n" + "=" * 50)
print("7. INPUT EXAMPLE (commented - uncomment to test)")
print("=" * 50)

# Uncomment below to test input
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# print(f"Hello {name}! You are {age} years old.")

print("Input examples are commented out.")
print("Uncomment the lines above to test interactive input.")

print("\n" + "=" * 50)
print("BASICS COMPLETE!")
print("=" * 50)
