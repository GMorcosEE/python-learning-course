# Week 7: Functions - Reusable Code
# Run: python3 week7-functions/01_functions_basics.py

# Basic function
def greet() -> None:
    print("Hello, World!")

greet()  # Call the function

# Function with parameters and type hints
def greet_person(name: str) -> None:
    print(f"Hello, {name}!")

greet_person("Alice")
greet_person("Bob")

# Function with multiple parameters and type hints
def add_numbers(a: int, b: int) -> None:
    result = a + b
    print(f"{a} + {b} = {result}")

add_numbers(5, 3)
add_numbers(10, 20)

# Function with return value and type hints
def multiply(a: int, b: int) -> int:
    return a * b

result = multiply(4, 5)
print("Result:", result)

# Type hints help document what types a function expects
# Format: def function_name(param: type) -> return_type:

# Using return value in expressions
total = multiply(3, 4) + multiply(2, 5)
print("Total:", total)

# Function with default parameters
def greet_with_title(name, title="Mr."):
    print(f"Hello, {title} {name}")

greet_with_title("Smith")
greet_with_title("Johnson", "Dr.")

# TODO: Create a function that takes a name and age, and prints a greeting
# TODO: Create a function that calculates the area of a rectangle (width * height)
# TODO: Create a function that converts Celsius to Fahrenheit (F = C * 9/5 + 32)
