# Week 7: Mini Project - Calculator with Functions
# Run: python3 week7-functions/03_calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def calculator():
    print("Simple Calculator")
    print("=" * 30)
    
    while True:
        print("\nOperations:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Quit")
        
        choice = input("\nChoose operation (1-5): ")
        
        if choice == "5":
            print("Goodbye!")
            break
        
        if choice in ["1", "2", "3", "4"]:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == "1":
                result = add(num1, num2)
                print(f"Result: {num1} + {num2} = {result}")
            elif choice == "2":
                result = subtract(num1, num2)
                print(f"Result: {num1} - {num2} = {result}")
            elif choice == "3":
                result = multiply(num1, num2)
                print(f"Result: {num1} * {num2} = {result}")
            elif choice == "4":
                result = divide(num1, num2)
                print(f"Result: {num1} / {num2} = {result}")
        else:
            print("Invalid choice. Please choose 1-5")

calculator()

# TODO: Add a power function (a ** b)
# TODO: Add a square root function
# TODO: Add a function to calculate percentage
