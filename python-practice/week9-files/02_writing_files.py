# Week 9: Writing to Files
# Run: python3 week9-files/02_writing_files.py

# Writing to a file (overwrites existing content)
print("Writing to file...")
with open("output.txt", "w") as file:
    file.write("This is the first line.\n")
    file.write("This is the second line.\n")
    file.write("This is the third line.\n")

print("Created output.txt")

# Appending to a file (adds to existing content)
print("\nAppending to file...")
with open("output.txt", "a") as file:
    file.write("This line was appended.\n")
    file.write("This is another appended line.\n")

print("Appended to output.txt")

# Reading back what we wrote
print("\nReading output.txt:")
with open("output.txt", "r") as file:
    print(file.read())

# Writing multiple lines at once
lines = [
    "Line 1\n",
    "Line 2\n",
    "Line 3\n"
]

with open("multiple_lines.txt", "w") as file:
    file.writelines(lines)

print("Created multiple_lines.txt")

# Writing user input to file
print("\nWriting user input to file:")
name = input("Enter your name: ")
age = input("Enter your age: ")

with open("user_info.txt", "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")

print("Saved to user_info.txt")

# TODO: Create a program that asks for 5 favorite foods and saves them to a file
# TODO: Read the file back and display the foods
# TODO: Add a new food to the file using append mode
