# Week 12: Advanced OOP - Properties and Encapsulation
# Run: python3 week12-oop-advanced/02_properties_encapsulation.py

# Encapsulation: Hiding internal details and controlling access to data
# Properties: Allow controlled access to attributes with getter/setter methods

class Person:
    """Person class with encapsulation"""
    
    def __init__(self, name: str, age: int):
        self._name = name  # Protected attribute (convention: single underscore)
        self._age = age
    
    # Getter method using @property decorator
    @property
    def name(self) -> str:
        """Get the person's name"""
        return self._name
    
    # Setter method
    @name.setter
    def name(self, value: str) -> None:
        """Set the person's name with validation"""
        if not value or not isinstance(value, str):
            raise ValueError("Name must be a non-empty string")
        self._name = value
    
    @property
    def age(self) -> int:
        """Get the person's age"""
        return self._age
    
    @age.setter
    def age(self, value: int) -> None:
        """Set the person's age with validation"""
        if not isinstance(value, int) or value < 0 or value > 150:
            raise ValueError("Age must be between 0 and 150")
        self._age = value
    
    # Read-only property (no setter)
    @property
    def is_adult(self) -> bool:
        """Check if person is an adult"""
        return self._age >= 18
    
    def __str__(self) -> str:
        return f"{self._name}, {self._age} years old"


# Using properties
person = Person("Alice", 25)

# Access like attributes, but uses getter methods
print(f"Name: {person.name}")
print(f"Age: {person.age}")
print(f"Is adult: {person.is_adult}")

# Modify using setter methods
person.name = "Alice Smith"
person.age = 26
print(f"\nUpdated: {person}")

# Validation in action
try:
    person.age = -5  # Will raise ValueError
except ValueError as e:
    print(f"\nError: {e}")

try:
    person.age = 200  # Will raise ValueError
except ValueError as e:
    print(f"Error: {e}")

# Read-only property cannot be set
try:
    person.is_adult = False  # Will raise AttributeError
except AttributeError as e:
    print(f"Error: can't set attribute")


# More complex example - BankAccount with encapsulation
class BankAccount:
    """Bank account with protected balance"""
    
    def __init__(self, account_holder: str, initial_balance: float = 0):
        self._account_holder = account_holder
        self.__balance = initial_balance  # Private attribute (double underscore)
        self._transaction_count = 0
    
    @property
    def account_holder(self) -> str:
        return self._account_holder
    
    @property
    def balance(self) -> float:
        """Get balance (read-only from outside)"""
        return self.__balance
    
    @property
    def transaction_count(self) -> int:
        """Get number of transactions"""
        return self._transaction_count
    
    def deposit(self, amount: float) -> None:
        """Deposit money"""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount
        self._transaction_count += 1
        print(f"Deposited ${amount:.2f}. New balance: ${self.__balance:.2f}")
    
    def withdraw(self, amount: float) -> bool:
        """Withdraw money"""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.__balance:
            print("Insufficient funds")
            return False
        self.__balance -= amount
        self._transaction_count += 1
        print(f"Withdrew ${amount:.2f}. New balance: ${self.__balance:.2f}")
        return True
    
    def __str__(self) -> str:
        return f"Account: {self._account_holder}, Balance: ${self.__balance:.2f}"


print("\n--- Bank Account Example ---")
account = BankAccount("Bob", 1000)
print(account)

# Can read balance but not modify directly
print(f"Balance: ${account.balance:.2f}")

# Must use methods to modify
account.deposit(500)
account.withdraw(200)

print(f"Total transactions: {account.transaction_count}")

# Cannot directly modify balance (it's private)
try:
    account.balance = 10000  # Will raise AttributeError
except AttributeError:
    print("Cannot directly modify balance (read-only property)")


# Computed properties
class Rectangle:
    """Rectangle with computed area and perimeter"""
    
    def __init__(self, width: float, height: float):
        self._width = width
        self._height = height
    
    @property
    def width(self) -> float:
        return self._width
    
    @width.setter
    def width(self, value: float) -> None:
        if value <= 0:
            raise ValueError("Width must be positive")
        self._width = value
    
    @property
    def height(self) -> float:
        return self._height
    
    @height.setter
    def height(self, value: float) -> None:
        if value <= 0:
            raise ValueError("Height must be positive")
        self._height = value
    
    @property
    def area(self) -> float:
        """Computed property - calculated on access"""
        return self._width * self._height
    
    @property
    def perimeter(self) -> float:
        """Computed property"""
        return 2 * (self._width + self._height)
    
    def __str__(self) -> str:
        return f"Rectangle({self._width}x{self._height})"


print("\n--- Rectangle Example ---")
rect = Rectangle(5, 10)
print(rect)
print(f"Area: {rect.area}")
print(f"Perimeter: {rect.perimeter}")

# Modify dimensions
rect.width = 8
rect.height = 12
print(f"\nResized: {rect}")
print(f"New area: {rect.area}")
print(f"New perimeter: {rect.perimeter}")


# TODO: Create a Temperature class with celsius property and fahrenheit computed property
# TODO: Create a Circle class with radius property and computed area/circumference
# TODO: Add validation to ensure circle radius is positive
# TODO: Create a Product class with price property that validates positive values
# TODO: Add a discount property that calculates discounted price
