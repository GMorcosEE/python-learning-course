# Week 13: Error Handling - Custom Exceptions
# Run: python3 week13-error-handling/02_custom_exceptions.py

# Custom exceptions make your code more readable and maintainable

# Basic custom exception
class InvalidEmailError(Exception):
    """Raised when email format is invalid"""
    pass


def validate_email(email: str) -> bool:
    """Validate email format"""
    if "@" not in email or "." not in email:
        raise InvalidEmailError(f"'{email}' is not a valid email address")
    return True


print("=== Basic Custom Exception ===\n")

try:
    validate_email("user@example.com")
    print("✅ Valid email")
except InvalidEmailError as e:
    print(f"❌ {e}")

try:
    validate_email("invalid-email")
except InvalidEmailError as e:
    print(f"❌ {e}")


# Custom exception with additional data
class InsufficientFundsError(Exception):
    """Raised when account has insufficient funds"""
    
    def __init__(self, balance: float, amount: float):
        self.balance = balance
        self.amount = amount
        self.shortage = amount - balance
        super().__init__(
            f"Insufficient funds: need ${amount:.2f}, have ${balance:.2f} (short ${self.shortage:.2f})"
        )


class BankAccount:
    """Bank account with custom exceptions"""
    
    def __init__(self, balance: float = 0):
        self.balance = balance
    
    def withdraw(self, amount: float) -> None:
        """Withdraw money with error checking"""
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        print(f"✅ Withdrew ${amount:.2f}. Balance: ${self.balance:.2f}")


print("\n=== Custom Exception with Data ===\n")

account = BankAccount(100)
try:
    account.withdraw(50)
    account.withdraw(80)  # Will fail
except InsufficientFundsError as e:
    print(f"❌ {e}")
    print(f"   You need ${e.shortage:.2f} more")


# Exception hierarchy
class ValidationError(Exception):
    """Base class for validation errors"""
    pass


class AgeValidationError(ValidationError):
    """Raised when age is invalid"""
    pass


class NameValidationError(ValidationError):
    """Raised when name is invalid"""
    pass


class EmailValidationError(ValidationError):
    """Raised when email is invalid"""
    pass


class User:
    """User class with validation"""
    
    def __init__(self, name: str, age: int, email: str):
        self.name = self._validate_name(name)
        self.age = self._validate_age(age)
        self.email = self._validate_email(email)
    
    def _validate_name(self, name: str) -> str:
        """Validate name"""
        if not name or len(name) < 2:
            raise NameValidationError("Name must be at least 2 characters")
        if not name.replace(" ", "").isalpha():
            raise NameValidationError("Name must contain only letters")
        return name
    
    def _validate_age(self, age: int) -> int:
        """Validate age"""
        if not isinstance(age, int):
            raise AgeValidationError("Age must be an integer")
        if age < 0 or age > 150:
            raise AgeValidationError("Age must be between 0 and 150")
        return age
    
    def _validate_email(self, email: str) -> str:
        """Validate email"""
        if "@" not in email or "." not in email.split("@")[1]:
            raise EmailValidationError(f"Invalid email format: {email}")
        return email
    
    def __str__(self) -> str:
        return f"User({self.name}, {self.age}, {self.email})"


print("\n=== Exception Hierarchy ===\n")

def create_user(name: str, age: int, email: str) -> None:
    """Create user with error handling"""
    try:
        user = User(name, age, email)
        print(f"✅ Created: {user}")
    except NameValidationError as e:
        print(f"❌ Name Error: {e}")
    except AgeValidationError as e:
        print(f"❌ Age Error: {e}")
    except EmailValidationError as e:
        print(f"❌ Email Error: {e}")
    except ValidationError as e:
        # Catches any ValidationError subclass
        print(f"❌ Validation Error: {e}")

create_user("Alice", 25, "alice@example.com")
create_user("A", 25, "alice@example.com")
create_user("Alice", -5, "alice@example.com")
create_user("Alice", 25, "invalid-email")


# Custom exception with context manager
class DatabaseConnectionError(Exception):
    """Raised when database connection fails"""
    pass


class Database:
    """Simulated database with custom exceptions"""
    
    def __init__(self, name: str, fail: bool = False):
        self.name = name
        self.fail = fail
        self.connected = False
    
    def __enter__(self):
        """Connect to database"""
        if self.fail:
            raise DatabaseConnectionError(f"Failed to connect to {self.name}")
        self.connected = True
        print(f"✅ Connected to {self.name}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Disconnect from database"""
        if self.connected:
            print(f"🔒 Disconnected from {self.name}")
        return False
    
    def query(self, sql: str) -> list:
        """Execute query"""
        if not self.connected:
            raise DatabaseConnectionError("Not connected to database")
        print(f"📊 Executing: {sql}")
        return [{"id": 1, "name": "Result"}]


print("\n=== Custom Exceptions with Context Managers ===\n")

try:
    with Database("users_db") as db:
        results = db.query("SELECT * FROM users")
        print(f"Results: {results}")
except DatabaseConnectionError as e:
    print(f"❌ Database Error: {e}")

try:
    with Database("broken_db", fail=True) as db:
        results = db.query("SELECT * FROM users")
except DatabaseConnectionError as e:
    print(f"❌ Database Error: {e}")


# Re-raising exceptions
print("\n=== Re-raising Exceptions ===\n")

def process_data(data: dict) -> None:
    """Process data with logging and re-raising"""
    try:
        value = data["value"]
        result = 100 / int(value)
        print(f"✅ Result: {result}")
    except KeyError:
        print("⚠️  Logging: Missing 'value' key")
        raise  # Re-raise the same exception
    except (ValueError, ZeroDivisionError) as e:
        print(f"⚠️  Logging: Calculation error - {e}")
        raise  # Re-raise the same exception

try:
    process_data({"value": "10"})
except Exception as e:
    print(f"Caught: {e}")

try:
    process_data({"other": "data"})
except KeyError:
    print("❌ Handled KeyError at top level")


# TODO: Create a custom PasswordTooWeakError exception
# TODO: Create a custom FileFormatError for invalid file types
# TODO: Build a validation system with multiple custom exceptions
# TODO: Create a custom exception that logs errors to a file
