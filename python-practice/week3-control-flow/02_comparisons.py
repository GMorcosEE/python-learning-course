# Week 3: Comparison Operators
# Run: python3 week3-control-flow/02_comparisons.py

# Comparison operators
x = 10
y = 5

print("x == y:", x == y)  # Equal to
print("x != y:", x != y)  # Not equal to
print("x > y:", x > y)    # Greater than
print("x < y:", x < y)    # Less than
print("x >= y:", x >= y)  # Greater than or equal
print("x <= y:", x <= y)  # Less than or equal

# Logical operators (and, or, not)
age = 25
has_license = True

if age >= 18 and has_license:
    print("You can drive")

is_weekend = False
is_holiday = True

if is_weekend or is_holiday:
    print("No work today!")

is_raining = False
if not is_raining:
    print("You don't need an umbrella")

# TODO: Create a password checker
# TODO: Ask for a password
# TODO: If password is "python123", print "Access granted"
# TODO: Otherwise, print "Access denied"
