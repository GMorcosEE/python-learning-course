# Week 8: Organizing Code with Functions
# Run: python3 week8-functions/02_function_organization.py

# Group related functions together

# String utilities
def capitalize_words(text):
    return text.title()

def reverse_string(text):
    return text[::-1]

def count_words(text):
    return len(text.split())

# Math utilities
def is_even(num):
    return num % 2 == 0

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def factorial(num):
    if num == 0 or num == 1:
        return 1
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result

# List utilities
def find_max(numbers):
    if not numbers:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

def remove_duplicates(items):
    return list(set(items))

# Testing the functions
print("String utilities:")
print("Capitalize:", capitalize_words("hello world"))
print("Reverse:", reverse_string("python"))
print("Word count:", count_words("This is a test"))

print("\nMath utilities:")
print("Is 4 even?", is_even(4))
print("Is 7 prime?", is_prime(7))
print("Factorial of 5:", factorial(5))

print("\nList utilities:")
print("Max of [3,7,2,9,1]:", find_max([3, 7, 2, 9, 1]))
print("Remove duplicates:", remove_duplicates([1, 2, 2, 3, 3, 4]))

# TODO: Create a function that validates email format (contains @ and .)
# TODO: Create a function that finds the second largest number in a list
# TODO: Create a function that converts a list of strings to uppercase
