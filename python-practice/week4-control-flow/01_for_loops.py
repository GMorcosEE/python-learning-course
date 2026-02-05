# Week 4: For Loops - Repeating Actions
# Run: python3 week4-control-flow/01_for_loops.py

# Basic for loop - count from 0 to 4
print("Counting:")
for i in range(5):
    print(i)

# Count from 1 to 10
print("\nCounting 1 to 10:")
for i in range(1, 11):
    print(i)

# Count by 2s
print("\nEven numbers:")
for i in range(0, 11, 2):
    print(i)

# Loop through a list of items
print("\nFruits:")
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print("I like", fruit)

# TODO: Print your name 5 times
# TODO: Print numbers from 10 down to 1 (hint: range(10, 0, -1))
# TODO: Create a list of your favorite movies and print each one
