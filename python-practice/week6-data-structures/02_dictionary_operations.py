# Week 6: Dictionary Operations
# Run: python3 week6-data-structures/02_dictionary_operations.py

# Looping through dictionaries
scores = {
    "Alice": 95,
    "Bob": 87,
    "Charlie": 92
}

# Loop through keys
print("Students:")
for name in scores:
    print(name)

# Loop through values
print("\nScores:")
for score in scores.values():
    print(score)

# Loop through both keys and values
print("\nStudent scores:")
for name, score in scores.items():
    print(f"{name}: {score}")

# List of dictionaries
students = [
    {"name": "Alice", "age": 20, "grade": "A"},
    {"name": "Bob", "age": 21, "grade": "B"},
    {"name": "Charlie", "age": 19, "grade": "A"}
]

print("\nAll students:")
for student in students:
    print(f"{student['name']} is {student['age']} years old and got grade {student['grade']}")

# Nested dictionaries
contacts = {
    "Alice": {
        "phone": "555-1234",
        "email": "alice@example.com"
    },
    "Bob": {
        "phone": "555-5678",
        "email": "bob@example.com"
    }
}

print("\nAlice's phone:", contacts["Alice"]["phone"])

# TODO: Create a dictionary of 3 countries with their capitals
# TODO: Loop through and print "The capital of [country] is [capital]"
# TODO: Create a list of 3 dictionaries representing products (name, price, quantity)
