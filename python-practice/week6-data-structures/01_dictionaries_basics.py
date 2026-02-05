# Week 6: Dictionaries - Key-Value Pairs
# Run: python3 week6-data-structures/01_dictionaries_basics.py

# Creating dictionaries
person = {
    "name": "John",
    "age": 25,
    "city": "New York"
}

print("Person:", person)

# Accessing values by key
print("\nName:", person["name"])
print("Age:", person["age"])

# Using .get() method (safer - doesn't crash if key doesn't exist)
print("City:", person.get("city"))
print("Country:", person.get("country", "Not specified"))

# Adding/updating values
person["email"] = "john@example.com"  # Add new key
person["age"] = 26  # Update existing key

print("\nUpdated person:", person)

# Removing items
del person["email"]  # Remove by key
print("After deletion:", person)

# Checking if key exists
if "name" in person:
    print("\nName exists in dictionary")

# Getting all keys and values
print("\nAll keys:", person.keys())
print("All values:", person.values())
print("All items:", person.items())

# TODO: Create a dictionary for your favorite book with keys: title, author, year
# TODO: Print the title and author
# TODO: Add a new key "genre" with a value
# TODO: Update the year
