"""
Functions - Practice Examples
Common function patterns for practical exams
"""

# ============================================
# 1. BASIC FUNCTIONS
# ============================================
print("=" * 50)
print("1. BASIC FUNCTIONS")
print("=" * 50)

def greet(name):
    """Simple function with parameter"""
    return f"Hello, {name}!"

def add(a, b):
    """Function with multiple parameters"""
    return a + b

print(greet("Jagdeep"))
print(f"5 + 3 = {add(5, 3)}")

# ============================================
# 2. DEFAULT ARGUMENTS
# ============================================
print("\n" + "=" * 50)
print("2. DEFAULT ARGUMENTS")
print("=" * 50)

def power(base, exponent=2):
    """Function with default parameter"""
    return base ** exponent

print(f"5^2 (default) = {power(5)}")
print(f"5^3 = {power(5, 3)}")

# ============================================
# 3. VARIABLE LENGTH ARGUMENTS
# ============================================
print("\n" + "=" * 50)
print("3. VARIABLE LENGTH ARGUMENTS")
print("=" * 50)

def sum_all(*args):
    """*args - accepts variable positional arguments"""
    total = 0
    for num in args:
        total += num
    return total

def print_info(**kwargs):
    """**kwargs - accepts variable keyword arguments"""
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print(f"Sum of 1, 2, 3, 4, 5 = {sum_all(1, 2, 3, 4, 5)}")
print("\nStudent Information:")
print_info(name="Jagdeep", age=20, course="Python", roll="CS101")

# ============================================
# 4. LAMBDA FUNCTIONS
# ============================================
print("\n" + "=" * 50)
print("4. LAMBDA FUNCTIONS")
print("=" * 50)

square = lambda x: x ** 2
add = lambda a, b: a + b
is_even = lambda x: x % 2 == 0

print(f"Square of 5: {square(5)}")
print(f"3 + 7 = {add(3, 7)}")
print(f"Is 4 even? {is_even(4)}")
print(f"Is 7 even? {is_even(7)}")

# ============================================
# 5. COMMON ALGORITHM FUNCTIONS
# ============================================
print("\n" + "=" * 50)
print("5. COMMON ALGORITHMS")
print("=" * 50)

def factorial(n):
    """Calculate factorial using recursion"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def factorial_iterative(n):
    """Calculate factorial using iteration"""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci(n):
    """Generate nth Fibonacci number"""
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b

def is_palindrome(s):
    """Check if string is palindrome"""
    s = s.lower().replace(" ", "")
    return s == s[::-1]

# Test algorithms
print(f"Factorial of 5 (recursive): {factorial(5)}")
print(f"Factorial of 5 (iterative): {factorial_iterative(5)}")
print(f"Is 17 prime? {is_prime(17)}")
print(f"Is 20 prime? {is_prime(20)}")
print(f"10th Fibonacci number: {fibonacci(10)}")
print(f"Is 'radar' palindrome? {is_palindrome('radar')}")
print(f"Is 'hello' palindrome? {is_palindrome('hello')}")

# ============================================
# 6. STRING MANIPULATION FUNCTIONS
# ============================================
print("\n" + "=" * 50)
print("6. STRING MANIPULATION")
print("=" * 50)

def count_vowels(text):
    """Count vowels in a string"""
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

def reverse_words(sentence):
    """Reverse each word in a sentence"""
    words = sentence.split()
    reversed_words = [word[::-1] for word in words]
    return " ".join(reversed_words)

def count_words(text):
    """Count words in text"""
    return len(text.split())

text = "Python Programming is Fun"
print(f"Text: '{text}'")
print(f"Vowel count: {count_vowels(text)}")
print(f"Word count: {count_words(text)}")
print(f"Reversed words: '{reverse_words(text)}'")

# ============================================
# 7. LIST MANIPULATION FUNCTIONS
# ============================================
print("\n" + "=" * 50)
print("7. LIST MANIPULATION")
print("=" * 50)

def find_largest(numbers):
    """Find largest number in list"""
    if not numbers:
        return None
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

def find_smallest(numbers):
    """Find smallest number in list"""
    if not numbers:
        return None
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest

def remove_duplicates(numbers):
    """Remove duplicates while preserving order"""
    unique = []
    for num in numbers:
        if num not in unique:
            unique.append(num)
    return unique

def list_sum(numbers):
    """Calculate sum of list"""
    total = 0
    for num in numbers:
        total += num
    return total

def list_average(numbers):
    """Calculate average of list"""
    if not numbers:
        return 0
    return list_sum(numbers) / len(numbers)

# Test list functions
numbers = [45, 23, 78, 12, 90, 34, 23, 45]
print(f"Numbers: {numbers}")
print(f"Largest: {find_largest(numbers)}")
print(f"Smallest: {find_smallest(numbers)}")
print(f"Sum: {list_sum(numbers)}")
print(f"Average: {list_average(numbers):.2f}")
print(f"Without duplicates: {remove_duplicates(numbers)}")

print("\n" + "=" * 50)
print("FUNCTIONS COMPLETE!")
print("=" * 50)
