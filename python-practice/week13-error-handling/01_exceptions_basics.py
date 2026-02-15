# Week 13: Error Handling - Exception Basics
# Run: python3 week13-error-handling/01_exceptions_basics.py

# Errors happen! Good programs handle them gracefully

# Basic try-except
print("=== Basic Exception Handling ===\n")

try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print(f"100 / {number} = {result}")
except ValueError:
    print("❌ That's not a valid number!")
except ZeroDivisionError:
    print("❌ Cannot divide by zero!")

print("Program continues...\n")


# Catching multiple exceptions
print("=== Multiple Exception Types ===\n")

def divide_numbers(a: str, b: str) -> None:
    """Divide two numbers with error handling"""
    try:
        num1 = float(a)
        num2 = float(b)
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    except ValueError:
        print("❌ Invalid number format")
    except ZeroDivisionError:
        print("❌ Cannot divide by zero")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

divide_numbers("10", "2")
divide_numbers("10", "0")
divide_numbers("abc", "5")
divide_numbers("10", "xyz")


# Using else and finally
print("\n=== Try-Except-Else-Finally ===\n")

def read_file_safe(filename: str) -> None:
    """Read file with complete error handling"""
    file = None
    try:
        print(f"Attempting to open {filename}...")
        file = open(filename, "r")
        content = file.read()
        print(f"✅ File content: {content[:50]}...")
    except FileNotFoundError:
        print(f"❌ File '{filename}' not found")
    except PermissionError:
        print(f"❌ No permission to read '{filename}'")
    except Exception as e:
        print(f"❌ Error reading file: {e}")
    else:
        # Runs only if no exception occurred
        print("✅ File read successfully")
    finally:
        # Always runs, even if exception occurred
        if file:
            file.close()
            print("🔒 File closed")
        print("--- Done ---\n")

# Create a test file
with open("test_file.txt", "w") as f:
    f.write("This is a test file for error handling examples.")

read_file_safe("test_file.txt")
read_file_safe("nonexistent.txt")


# Getting exception details
print("=== Exception Details ===\n")

def process_list(items: list, index: int) -> None:
    """Access list with error handling"""
    try:
        value = items[index]
        print(f"Value at index {index}: {value}")
    except IndexError as e:
        print(f"❌ IndexError: {e}")
        print(f"   List has {len(items)} items, index {index} is out of range")
    except TypeError as e:
        print(f"❌ TypeError: {e}")

my_list = [10, 20, 30, 40, 50]
process_list(my_list, 2)
process_list(my_list, 10)
process_list(my_list, "abc")


# Raising exceptions
print("\n=== Raising Exceptions ===\n")

def validate_age(age: int) -> None:
    """Validate age with custom error messages"""
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems unrealistic")
    print(f"✅ Valid age: {age}")

try:
    validate_age(25)
    validate_age(-5)
except ValueError as e:
    print(f"❌ ValueError: {e}")

try:
    validate_age("twenty")
except TypeError as e:
    print(f"❌ TypeError: {e}")


# Common exception types
print("\n=== Common Exception Types ===\n")

exceptions_demo = {
    "ValueError": lambda: int("abc"),
    "TypeError": lambda: "string" + 5,
    "KeyError": lambda: {"a": 1}["b"],
    "AttributeError": lambda: "string".nonexistent_method(),
    "IndexError": lambda: [1, 2, 3][10],
    "ZeroDivisionError": lambda: 10 / 0,
}

for name, func in exceptions_demo.items():
    try:
        func()
    except Exception as e:
        print(f"{name}: {e}")


# Nested try-except
print("\n=== Nested Exception Handling ===\n")

def complex_operation(data: dict) -> None:
    """Multiple levels of error handling"""
    try:
        # Outer try: check if key exists
        user_input = data["value"]
        
        try:
            # Inner try: convert to number
            number = float(user_input)
            
            try:
                # Innermost try: perform calculation
                result = 100 / number
                print(f"✅ Result: {result}")
            except ZeroDivisionError:
                print("❌ Cannot divide by zero")
        except ValueError:
            print(f"❌ '{user_input}' is not a valid number")
    except KeyError:
        print("❌ Missing 'value' key in data")

complex_operation({"value": "10"})
complex_operation({"value": "0"})
complex_operation({"value": "abc"})
complex_operation({"other": "data"})


# TODO: Create a function that safely converts string to int with default value
# TODO: Write a function that reads a file and handles all possible errors
# TODO: Create a calculator function with comprehensive error handling
# TODO: Add error handling to user input validation (email, phone, etc.)
