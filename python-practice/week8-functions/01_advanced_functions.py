# Week 8: Advanced Function Concepts
# Run: python3 week8-functions/01_advanced_functions.py

# Variable number of arguments (*args)
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print("Sum of 1, 2, 3:", sum_all(1, 2, 3))
print("Sum of 1, 2, 3, 4, 5:", sum_all(1, 2, 3, 4, 5))

# Keyword arguments (**kwargs)
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print("\nPerson info:")
print_info(name="Alice", age=25, city="New York")

# Lambda functions (small anonymous functions)
square = lambda x: x ** 2
print("\nSquare of 5:", square(5))

add = lambda a, b: a + b
print("Add 3 and 7:", add(3, 7))

# Using lambda with built-in functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print("\nSquared numbers:", squared)

# Filter with lambda
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

# Nested functions
def outer_function(text):
    def inner_function():
        return text.upper()
    return inner_function()

print("\nOuter function result:", outer_function("hello"))

# TODO: Create a function that takes any number of strings and returns them joined
# TODO: Create a lambda function that checks if a number is positive
# TODO: Use map() to convert a list of Celsius temps to Fahrenheit
