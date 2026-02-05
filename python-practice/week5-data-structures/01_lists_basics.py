# Week 5: Lists - Storing Multiple Items
# Run: python3 week5-data-structures/01_lists_basics.py

# Creating lists
fruits = ["apple", "banana", "orange", "grape"]
numbers = [1, 2, 3, 4, 5]
mixed = ["hello", 42, True, 3.14]

print("Fruits:", fruits)
print("Numbers:", numbers)

# Accessing items by index (starts at 0)
print("\nFirst fruit:", fruits[0])
print("Second fruit:", fruits[1])
print("Last fruit:", fruits[-1])  # Negative index counts from end

# List length
print("\nNumber of fruits:", len(fruits))

# Adding items
fruits.append("mango")  # Add to end
print("After append:", fruits)

fruits.insert(1, "kiwi")  # Insert at position 1
print("After insert:", fruits)

# Removing items
fruits.remove("banana")  # Remove by value
print("After remove:", fruits)

last_fruit = fruits.pop()  # Remove and return last item
print("Popped:", last_fruit)
print("After pop:", fruits)

# TODO: Create a list of your 5 favorite movies
# TODO: Print the first and last movie
# TODO: Add a new movie to the list
# TODO: Remove one movie from the list
