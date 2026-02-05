# Week 10: Working with CSV Files
# Run: python3 week10-files/01_csv_files.py

import csv

# Writing to CSV file
print("Creating CSV file...")
with open("students.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "Grade"])  # Header
    writer.writerow(["Alice", 20, "A"])
    writer.writerow(["Bob", 21, "B"])
    writer.writerow(["Charlie", 19, "A"])

print("Created students.csv")

# Reading from CSV file
print("\nReading CSV file:")
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Reading CSV as dictionary
print("\nReading CSV as dictionary:")
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['Name']} is {row['Age']} years old and got grade {row['Grade']}")

# Writing dictionary to CSV
print("\nWriting dictionary to CSV:")
students = [
    {"Name": "David", "Age": 22, "Grade": "B"},
    {"Name": "Eve", "Age": 20, "Grade": "A"},
]

with open("more_students.csv", "w", newline='') as file:
    fieldnames = ["Name", "Age", "Grade"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(students)

print("Created more_students.csv")

# Appending to CSV
print("\nAppending to CSV:")
with open("students.csv", "a", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Frank", 23, "C"])

print("Appended to students.csv")

# TODO: Create a CSV file with product data (name, price, quantity)
# TODO: Read the CSV and calculate total value (price * quantity) for each product
# TODO: Add a new product to the CSV file
