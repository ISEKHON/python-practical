"""
QUICK PRACTICE PROBLEMS
Common questions asked in Python practicals
"""

# ============================================
# PROBLEM 1: Prime Number Checker
# ============================================
def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print("=" * 50)
print("PROBLEM 1: PRIME NUMBER CHECKER")
print("=" * 50)
for num in [2, 7, 10, 17, 20, 29]:
    print(f"{num} is {'prime' if is_prime(num) else 'not prime'}")

# ============================================
# PROBLEM 2: Factorial (Recursive & Iterative)
# ============================================
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print("\n" + "=" * 50)
print("PROBLEM 2: FACTORIAL")
print("=" * 50)
for num in [5, 6, 7]:
    print(f"{num}! (recursive) = {factorial_recursive(num)}")
    print(f"{num}! (iterative) = {factorial_iterative(num)}")

# ============================================
# PROBLEM 3: Fibonacci Series
# ============================================
def fibonacci_series(n):
    """Generate first n Fibonacci numbers"""
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

print("\n" + "=" * 50)
print("PROBLEM 3: FIBONACCI SERIES")
print("=" * 50)
print(f"First 10 Fibonacci numbers: {fibonacci_series(10)}")

# ============================================
# PROBLEM 4: Palindrome Checker
# ============================================
def is_palindrome(s):
    """Check if string is palindrome"""
    s = s.lower().replace(" ", "")
    return s == s[::-1]

print("\n" + "=" * 50)
print("PROBLEM 4: PALINDROME CHECKER")
print("=" * 50)
test_strings = ["radar", "hello", "madam", "racecar", "python"]
for s in test_strings:
    print(f"'{s}' is {'a palindrome' if is_palindrome(s) else 'not a palindrome'}")

# ============================================
# PROBLEM 5: Count Vowels and Consonants
# ============================================
def count_vowels_consonants(text):
    """Count vowels and consonants in text"""
    vowels = "aeiouAEIOU"
    v_count = 0
    c_count = 0
    
    for char in text:
        if char.isalpha():
            if char in vowels:
                v_count += 1
            else:
                c_count += 1
    
    return v_count, c_count

print("\n" + "=" * 50)
print("PROBLEM 5: COUNT VOWELS AND CONSONANTS")
print("=" * 50)
text = "Python Programming"
vowels, consonants = count_vowels_consonants(text)
print(f"Text: '{text}'")
print(f"Vowels: {vowels}, Consonants: {consonants}")

# ============================================
# PROBLEM 6: Reverse a String
# ============================================
def reverse_string(s):
    return s[::-1]

def reverse_string_loop(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

print("\n" + "=" * 50)
print("PROBLEM 6: REVERSE STRING")
print("=" * 50)
text = "Python"
print(f"Original: {text}")
print(f"Reversed (slicing): {reverse_string(text)}")
print(f"Reversed (loop): {reverse_string_loop(text)}")

# ============================================
# PROBLEM 7: Find Largest & Smallest in List
# ============================================
def find_largest_smallest(numbers):
    if not numbers:
        return None, None
    return max(numbers), min(numbers)

print("\n" + "=" * 50)
print("PROBLEM 7: LARGEST & SMALLEST IN LIST")
print("=" * 50)
numbers = [45, 23, 78, 12, 90, 34]
largest, smallest = find_largest_smallest(numbers)
print(f"Numbers: {numbers}")
print(f"Largest: {largest}, Smallest: {smallest}")

# ============================================
# PROBLEM 8: Remove Duplicates from List
# ============================================
def remove_duplicates(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique

print("\n" + "=" * 50)
print("PROBLEM 8: REMOVE DUPLICATES")
print("=" * 50)
numbers = [1, 2, 3, 2, 4, 1, 5, 3]
print(f"Original: {numbers}")
print(f"Unique: {remove_duplicates(numbers)}")

# ============================================
# PROBLEM 9: Count Word Frequency
# ============================================
def word_frequency(text):
    words = text.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

print("\n" + "=" * 50)
print("PROBLEM 9: WORD FREQUENCY")
print("=" * 50)
text = "python is fun python is easy python is powerful"
freq = word_frequency(text)
print(f"Text: '{text}'")
print("Frequency:")
for word, count in freq.items():
    print(f"  '{word}': {count}")

# ============================================
# PROBLEM 10: Sum of Digits
# ============================================
def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

print("\n" + "=" * 50)
print("PROBLEM 10: SUM OF DIGITS")
print("=" * 50)
for num in [123, 456, 789]:
    print(f"Sum of digits of {num} = {sum_of_digits(num)}")

# ============================================
# PROBLEM 11: Armstrong Number
# ============================================
def is_armstrong(n):
    """Check if number is Armstrong number (sum of cubes of digits)"""
    digits = str(n)
    power = len(digits)
    total = sum(int(digit) ** power for digit in digits)
    return total == n

print("\n" + "=" * 50)
print("PROBLEM 11: ARMSTRONG NUMBER")
print("=" * 50)
for num in [153, 370, 371, 407, 123]:
    print(f"{num} is {'an Armstrong number' if is_armstrong(num) else 'not an Armstrong number'}")

# ============================================
# PROBLEM 12: Perfect Number
# ============================================
def is_perfect(n):
    """Check if number equals sum of its divisors (excluding itself)"""
    if n < 2:
        return False
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n

print("\n" + "=" * 50)
print("PROBLEM 12: PERFECT NUMBER")
print("=" * 50)
for num in [6, 28, 12, 496]:
    print(f"{num} is {'a perfect number' if is_perfect(num) else 'not a perfect number'}")

# ============================================
# PROBLEM 13: Swap Two Numbers
# ============================================
print("\n" + "=" * 50)
print("PROBLEM 13: SWAP TWO NUMBERS")
print("=" * 50)

a, b = 10, 20
print(f"Before swap: a = {a}, b = {b}")

# Method 1: Using tuple unpacking
a, b = b, a
print(f"After swap: a = {a}, b = {b}")

# Method 2: Using arithmetic
a, b = 20, 10
a = a + b
b = a - b
a = a - b
print(f"After swap (arithmetic): a = {a}, b = {b}")

# ============================================
# PROBLEM 14: Leap Year Checker
# ============================================
def is_leap_year(year):
    """Check if year is a leap year"""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print("\n" + "=" * 50)
print("PROBLEM 14: LEAP YEAR CHECKER")
print("=" * 50)
for year in [2020, 2021, 2024, 2000, 1900]:
    print(f"{year} is {'a leap year' if is_leap_year(year) else 'not a leap year'}")

# ============================================
# PROBLEM 15: Multiplication Table
# ============================================
def multiplication_table(n, limit=10):
    """Generate multiplication table"""
    for i in range(1, limit + 1):
        print(f"{n} x {i} = {n * i}")

print("\n" + "=" * 50)
print("PROBLEM 15: MULTIPLICATION TABLE OF 5")
print("=" * 50)
multiplication_table(5)

# ============================================
# PROBLEM 16: GCD (Greatest Common Divisor)
# ============================================
def gcd(a, b):
    """Calculate GCD using Euclidean algorithm"""
    while b:
        a, b = b, a % b
    return a

print("\n" + "=" * 50)
print("PROBLEM 16: GCD (GREATEST COMMON DIVISOR)")
print("=" * 50)
pairs = [(48, 18), (100, 50), (17, 19)]
for a, b in pairs:
    print(f"GCD of {a} and {b} = {gcd(a, b)}")

# ============================================
# PROBLEM 17: LCM (Least Common Multiple)
# ============================================
def lcm(a, b):
    """Calculate LCM using GCD"""
    return abs(a * b) // gcd(a, b)

print("\n" + "=" * 50)
print("PROBLEM 17: LCM (LEAST COMMON MULTIPLE)")
print("=" * 50)
for a, b in pairs:
    print(f"LCM of {a} and {b} = {lcm(a, b)}")

# ============================================
# PROBLEM 18: Second Largest in List
# ============================================
def second_largest(numbers):
    """Find second largest number"""
    if len(numbers) < 2:
        return None
    unique = list(set(numbers))
    unique.sort(reverse=True)
    return unique[1] if len(unique) > 1 else None

print("\n" + "=" * 50)
print("PROBLEM 18: SECOND LARGEST NUMBER")
print("=" * 50)
numbers = [45, 23, 78, 12, 90, 34, 78]
print(f"Numbers: {numbers}")
print(f"Second largest: {second_largest(numbers)}")

# ============================================
# PROBLEM 19: Matrix Addition
# ============================================
def add_matrices(mat1, mat2):
    """Add two matrices"""
    rows = len(mat1)
    cols = len(mat1[0])
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            result[i][j] = mat1[i][j] + mat2[i][j]
    
    return result

print("\n" + "=" * 50)
print("PROBLEM 19: MATRIX ADDITION")
print("=" * 50)
matrix1 = [[1, 2, 3], [4, 5, 6]]
matrix2 = [[7, 8, 9], [10, 11, 12]]
result = add_matrices(matrix1, matrix2)
print("Matrix 1:", matrix1)
print("Matrix 2:", matrix2)
print("Sum:", result)

# ============================================
# PROBLEM 20: Print Pattern
# ============================================
print("\n" + "=" * 50)
print("PROBLEM 20: STAR PATTERNS")
print("=" * 50)

print("Pattern 1: Right Triangle")
for i in range(1, 6):
    print("* " * i)

print("\nPattern 2: Pyramid")
for i in range(1, 6):
    print(" " * (5 - i) + "* " * i)

print("\nPattern 3: Number Triangle")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# ============================================
# SUMMARY
# ============================================
print("\n" + "=" * 60)
print("ALL PRACTICE PROBLEMS COMPLETE!")
print("=" * 60)
print("\nKEY TOPICS COVERED:")
print("1.  Prime Numbers")
print("2.  Factorial (Recursive & Iterative)")
print("3.  Fibonacci Series")
print("4.  Palindrome")
print("5.  Vowels & Consonants")
print("6.  String Reversal")
print("7.  List Operations (Max/Min)")
print("8.  Remove Duplicates")
print("9.  Word Frequency")
print("10. Sum of Digits")
print("11. Armstrong Number")
print("12. Perfect Number")
print("13. Swap Numbers")
print("14. Leap Year")
print("15. Multiplication Table")
print("16. GCD")
print("17. LCM")
print("18. Second Largest")
print("19. Matrix Addition")
print("20. Patterns")
print("=" * 60)
