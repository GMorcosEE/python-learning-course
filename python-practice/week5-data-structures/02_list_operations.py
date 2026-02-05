# Week 5: List Operations
# Run: python3 week5-data-structures/02_list_operations.py

# Slicing lists
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("First 3:", numbers[0:3])  # Items 0, 1, 2
print("Middle:", numbers[3:7])   # Items 3, 4, 5, 6
print("Last 3:", numbers[-3:])   # Last 3 items

# Checking if item exists
fruits = ["apple", "banana", "orange"]

if "banana" in fruits:
    print("We have bananas!")

if "grape" not in fruits:
    print("No grapes available")

# Sorting
numbers = [5, 2, 8, 1, 9]
numbers.sort()
print("Sorted:", numbers)

# Reversing
numbers.reverse()
print("Reversed:", numbers)

# Looping through lists
print("\nAll fruits:")
for fruit in fruits:
    print("-", fruit)

# Looping with index
print("\nFruits with index:")
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# TODO: Create a list of numbers from 1 to 10
# TODO: Print only the even numbers (hint: use if inside the loop)
# TODO: Create a list of names and sort them alphabetically
