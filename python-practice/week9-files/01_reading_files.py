# Week 9: Reading Files
# Run: python3 week9-files/01_reading_files.py

# First, let's create a sample file to read
with open("sample.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is line 2.\n")
    file.write("This is line 3.\n")

print("Created sample.txt\n")

# Reading entire file
print("Method 1: Read entire file")
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

# Reading line by line
print("\nMethod 2: Read line by line")
with open("sample.txt", "r") as file:
    for line in file:
        print(line.strip())  # strip() removes the newline character

# Reading all lines into a list
print("\nMethod 3: Read all lines into list")
with open("sample.txt", "r") as file:
    lines = file.readlines()
    print("Number of lines:", len(lines))
    print("First line:", lines[0].strip())

# Reading specific number of characters
print("\nMethod 4: Read first 10 characters")
with open("sample.txt", "r") as file:
    content = file.read(10)
    print(content)

# Checking if file exists
import os
if os.path.exists("sample.txt"):
    print("\nFile exists!")

# TODO: Create a text file with your favorite quotes (one per line)
# TODO: Read the file and print each quote with a number
# TODO: Count how many lines are in the file
