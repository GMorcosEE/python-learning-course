# Week 4: Mini Project - Multiplication Table
# Run: python3 week4-control-flow/03_multiplication_table.py

# Ask user for a number
number = int(input("Enter a number: "))

print(f"\nMultiplication table for {number}:")
print("-" * 20)

# Print multiplication table
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")

# TODO: Create a program that prints all even numbers from 1 to 50
# TODO: Create a program that asks for 5 numbers and prints the largest one
# TODO: Make a simple menu system that loops until user chooses "quit"
