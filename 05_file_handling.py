"""
File Handling Examples
Reading, Writing, and Processing Files
"""

import os

# ============================================
# 1. WRITING TO FILES
# ============================================
print("=" * 50)
print("1. WRITING TO FILES")
print("=" * 50)

# Write mode (overwrites file)
print("Creating sample.txt...")
with open("sample.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a sample file.\n")
    file.write("Python File Handling\n")
print("File created successfully!")

# Append mode
print("\nAppending to sample.txt...")
with open("sample.txt", "a") as file:
    file.write("This line was appended.\n")
    file.write("Another appended line.\n")
print("Content appended successfully!")

# ============================================
# 2. READING FILES
# ============================================
print("\n" + "=" * 50)
print("2. READING FILES")
print("=" * 50)

# Read entire file
print("Reading entire file:")
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

# Read line by line
print("\nReading line by line:")
with open("sample.txt", "r") as file:
    line_number = 1
    for line in file:
        print(f"Line {line_number}: {line.strip()}")
        line_number += 1

# Read all lines into a list
print("\nReading into list:")
with open("sample.txt", "r") as file:
    lines = file.readlines()
    print(f"Total lines: {len(lines)}")
    for i, line in enumerate(lines, 1):
        print(f"{i}: {line.strip()}")

# ============================================
# 3. FILE OPERATIONS
# ============================================
print("\n" + "=" * 50)
print("3. FILE OPERATIONS")
print("=" * 50)

# Count words in file
def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        return 0

word_count = count_words_in_file("sample.txt")
print(f"Word count in sample.txt: {word_count}")

# Count lines in file
def count_lines_in_file(filename):
    try:
        with open(filename, 'r') as file:
            return len(file.readlines())
    except FileNotFoundError:
        return 0

line_count = count_lines_in_file("sample.txt")
print(f"Line count in sample.txt: {line_count}")

# Count characters
def count_characters_in_file(filename):
    try:
        with open(filename, 'r') as file:
            return len(file.read())
    except FileNotFoundError:
        return 0

char_count = count_characters_in_file("sample.txt")
print(f"Character count in sample.txt: {char_count}")

# ============================================
# 4. STUDENT DATA FILE EXAMPLE
# ============================================
print("\n" + "=" * 50)
print("4. STUDENT DATA MANAGEMENT")
print("=" * 50)

# Write student data
print("Creating students.txt...")
with open("students.txt", "w") as file:
    file.write("Name,Roll No,Marks\n")
    file.write("Jagdeep,CS101,85\n")
    file.write("Alice,CS102,92\n")
    file.write("Bob,CS103,78\n")
    file.write("Charlie,CS104,88\n")
    file.write("David,CS105,95\n")
print("Student data written!")

# Read and display student data
print("\nReading student data:")
with open("students.txt", "r") as file:
    header = file.readline().strip()
    print(f"{header}")
    print("-" * 30)
    for line in file:
        print(line.strip())

# Calculate average marks
print("\nCalculating average marks:")
total_marks = 0
student_count = 0

with open("students.txt", "r") as file:
    file.readline()  # Skip header
    for line in file:
        parts = line.strip().split(',')
        marks = int(parts[2])
        total_marks += marks
        student_count += 1

average = total_marks / student_count if student_count > 0 else 0
print(f"Average marks: {average:.2f}")

# ============================================
# 5. SEARCH IN FILE
# ============================================
print("\n" + "=" * 50)
print("5. SEARCH IN FILE")
print("=" * 50)

def search_in_file(filename, search_term):
    """Search for a term in file and return matching lines"""
    matches = []
    try:
        with open(filename, 'r') as file:
            for line_num, line in enumerate(file, 1):
                if search_term.lower() in line.lower():
                    matches.append((line_num, line.strip()))
    except FileNotFoundError:
        print(f"File '{filename}' not found")
    return matches

# Search for "Alice" in students file
search_term = "Alice"
matches = search_in_file("students.txt", search_term)
print(f"Searching for '{search_term}':")
if matches:
    for line_num, line in matches:
        print(f"  Line {line_num}: {line}")
else:
    print(f"  No matches found")

# ============================================
# 6. COPY FILE CONTENT
# ============================================
print("\n" + "=" * 50)
print("6. COPY FILE")
print("=" * 50)

def copy_file(source, destination):
    """Copy content from source to destination file"""
    try:
        with open(source, 'r') as src:
            content = src.read()
        
        with open(destination, 'w') as dest:
            dest.write(content)
        
        print(f"Copied '{source}' to '{destination}'")
        return True
    except FileNotFoundError:
        print(f"Source file '{source}' not found")
        return False

copy_file("sample.txt", "sample_copy.txt")

# ============================================
# 7. FILE WITH EXCEPTION HANDLING
# ============================================
print("\n" + "=" * 50)
print("7. EXCEPTION HANDLING IN FILE OPERATIONS")
print("=" * 50)

def safe_read_file(filename):
    """Read file with proper exception handling"""
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return None
    except PermissionError:
        print(f"Error: No permission to read '{filename}'")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

# Try reading existing file
print("Reading sample.txt:")
content = safe_read_file("sample.txt")
if content:
    print(f"Successfully read {len(content)} characters")

# Try reading non-existent file
print("\nReading non_existent.txt:")
content = safe_read_file("non_existent.txt")

# ============================================
# 8. WORKING WITH NUMBERS FILE
# ============================================
print("\n" + "=" * 50)
print("8. NUMBERS FILE OPERATIONS")
print("=" * 50)

# Write numbers to file
print("Creating numbers.txt...")
with open("numbers.txt", "w") as file:
    numbers = [45, 23, 78, 12, 90, 34, 56, 89, 67, 41]
    for num in numbers:
        file.write(f"{num}\n")
print("Numbers written!")

# Read and process numbers
print("\nReading and processing numbers:")
numbers = []
with open("numbers.txt", "r") as file:
    for line in file:
        numbers.append(int(line.strip()))

print(f"Numbers: {numbers}")
print(f"Sum: {sum(numbers)}")
print(f"Average: {sum(numbers) / len(numbers):.2f}")
print(f"Maximum: {max(numbers)}")
print(f"Minimum: {min(numbers)}")

# Write even numbers to separate file
print("\nWriting even numbers to even_numbers.txt...")
with open("even_numbers.txt", "w") as file:
    for num in numbers:
        if num % 2 == 0:
            file.write(f"{num}\n")
print("Even numbers written!")

# ============================================
# 9. FILE STATISTICS
# ============================================
print("\n" + "=" * 50)
print("9. FILE STATISTICS")
print("=" * 50)

def get_file_statistics(filename):
    """Get detailed statistics about a file"""
    try:
        with open(filename, 'r') as file:
            content = file.read()
            lines = content.split('\n')
            words = content.split()
            
            stats = {
                'characters': len(content),
                'lines': len(lines),
                'words': len(words),
                'non_empty_lines': len([line for line in lines if line.strip()]),
            }
            return stats
    except FileNotFoundError:
        return None

stats = get_file_statistics("sample.txt")
if stats:
    print("Statistics for sample.txt:")
    print(f"  Characters: {stats['characters']}")
    print(f"  Lines: {stats['lines']}")
    print(f"  Words: {stats['words']}")
    print(f"  Non-empty lines: {stats['non_empty_lines']}")

print("\n" + "=" * 50)
print("FILE HANDLING COMPLETE!")
print("=" * 50)

# Clean up (optional - uncomment to delete created files)
# print("\nCleaning up created files...")
# for filename in ["sample.txt", "sample_copy.txt", "students.txt", "numbers.txt", "even_numbers.txt"]:
#     if os.path.exists(filename):
#         os.remove(filename)
#         print(f"Deleted {filename}")
