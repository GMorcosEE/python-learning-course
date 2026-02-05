# Week 7: More Function Practice
# Run: python3 week7-functions/02_function_practice.py

# Function that returns multiple values
def get_min_max(numbers):
    return min(numbers), max(numbers)

nums = [5, 2, 8, 1, 9]
minimum, maximum = get_min_max(nums)
print(f"Min: {minimum}, Max: {maximum}")

# Function with list parameter
def print_list(items):
    for item in items:
        print("-", item)

fruits = ["apple", "banana", "orange"]
print_list(fruits)

# Function that modifies a list
def add_item(items, new_item):
    items.append(new_item)
    return items

shopping = ["milk", "bread"]
add_item(shopping, "eggs")
print("Shopping list:", shopping)

# Function with conditional logic
def check_age(age):
    if age < 13:
        return "child"
    elif age < 20:
        return "teenager"
    else:
        return "adult"

print("Age 10:", check_age(10))
print("Age 16:", check_age(16))
print("Age 25:", check_age(25))

# Function that uses a loop
def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count

print("Vowels in 'hello':", count_vowels("hello"))
print("Vowels in 'python':", count_vowels("python"))

# TODO: Create a function that takes a list of numbers and returns the average
# TODO: Create a function that checks if a number is even (returns True/False)
# TODO: Create a function that reverses a string
