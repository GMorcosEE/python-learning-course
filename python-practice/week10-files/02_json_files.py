# Week 10: Working with JSON Files
# Run: python3 week10-files/02_json_files.py

import json

# Writing to JSON file
print("Creating JSON file...")
data = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "hobbies": ["reading", "coding", "gaming"]
}

with open("person.json", "w") as file:
    json.dump(data, file, indent=4)

print("Created person.json")

# Reading from JSON file
print("\nReading JSON file:")
with open("person.json", "r") as file:
    loaded_data = json.load(file)
    print(loaded_data)
    print(f"\nName: {loaded_data['name']}")
    print(f"Age: {loaded_data['age']}")
    print(f"Hobbies: {', '.join(loaded_data['hobbies'])}")

# Writing list of dictionaries to JSON
print("\nWriting list to JSON:")
students = [
    {"name": "Bob", "age": 20, "grade": "A"},
    {"name": "Charlie", "age": 21, "grade": "B"},
    {"name": "David", "age": 19, "grade": "A"}
]

with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

print("Created students.json")

# Reading and modifying JSON
print("\nModifying JSON data:")
with open("person.json", "r") as file:
    person = json.load(file)

person["age"] = 26
person["hobbies"].append("traveling")

with open("person.json", "w") as file:
    json.dump(person, file, indent=4)

print("Updated person.json")

# Converting Python objects to JSON strings
print("\nJSON string:")
data = {"status": "success", "count": 42}
json_string = json.dumps(data)
print(json_string)

# Parsing JSON strings
parsed = json.loads(json_string)
print("Parsed:", parsed)

# TODO: Create a JSON file with your favorite movies (title, year, rating)
# TODO: Read the JSON and print movies with rating > 8
# TODO: Add a new movie to the JSON file
