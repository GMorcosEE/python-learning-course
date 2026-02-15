# Week 14: Testing - pytest Basics
# Run: pytest week14-testing/02_pytest_basics.py -v
# Install: pip install pytest

import pytest


# Functions to test
def greet(name: str) -> str:
    """Return greeting message"""
    if not name:
        raise ValueError("Name cannot be empty")
    return f"Hello, {name}!"


def calculate_discount(price: float, discount_percent: float) -> float:
    """Calculate price after discount"""
    if price < 0:
        raise ValueError("Price cannot be negative")
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Discount must be between 0 and 100")
    return price * (1 - discount_percent / 100)


def find_max(numbers: list) -> int:
    """Find maximum number in list"""
    if not numbers:
        raise ValueError("List cannot be empty")
    return max(numbers)


# Basic tests
def test_greet():
    """Test greeting function"""
    assert greet("Alice") == "Hello, Alice!"
    assert greet("Bob") == "Hello, Bob!"


def test_greet_empty_name():
    """Test greeting with empty name"""
    with pytest.raises(ValueError):
        greet("")


def test_calculate_discount():
    """Test discount calculation"""
    assert calculate_discount(100, 10) == 90
    assert calculate_discount(50, 20) == 40
    assert calculate_discount(100, 0) == 100


def test_calculate_discount_invalid_price():
    """Test discount with negative price"""
    with pytest.raises(ValueError, match="Price cannot be negative"):
        calculate_discount(-10, 10)


def test_calculate_discount_invalid_percent():
    """Test discount with invalid percentage"""
    with pytest.raises(ValueError, match="Discount must be between"):
        calculate_discount(100, 150)


def test_find_max():
    """Test finding maximum"""
    assert find_max([1, 2, 3, 4, 5]) == 5
    assert find_max([10, 5, 8, 3]) == 10
    assert find_max([-1, -5, -3]) == -1


def test_find_max_empty_list():
    """Test finding max in empty list"""
    with pytest.raises(ValueError):
        find_max([])


# Parametrized tests - test multiple inputs
@pytest.mark.parametrize("name,expected", [
    ("Alice", "Hello, Alice!"),
    ("Bob", "Hello, Bob!"),
    ("Charlie", "Hello, Charlie!"),
])
def test_greet_parametrized(name, expected):
    """Test greeting with multiple names"""
    assert greet(name) == expected


@pytest.mark.parametrize("price,discount,expected", [
    (100, 10, 90),
    (50, 20, 40),
    (200, 50, 100),
    (75, 25, 56.25),
])
def test_discount_parametrized(price, discount, expected):
    """Test discount with multiple values"""
    assert calculate_discount(price, discount) == expected


# Fixtures - reusable test data
@pytest.fixture
def sample_list():
    """Provide sample list for tests"""
    return [1, 2, 3, 4, 5]


@pytest.fixture
def sample_dict():
    """Provide sample dictionary for tests"""
    return {"name": "Alice", "age": 30, "city": "New York"}


def test_with_fixture(sample_list):
    """Test using fixture"""
    assert len(sample_list) == 5
    assert sum(sample_list) == 15
    assert max(sample_list) == 5


def test_dict_fixture(sample_dict):
    """Test using dictionary fixture"""
    assert sample_dict["name"] == "Alice"
    assert sample_dict["age"] == 30
    assert "city" in sample_dict


# Testing a class
class ShoppingCart:
    """Shopping cart class"""
    
    def __init__(self):
        self.items = []
    
    def add_item(self, name: str, price: float, quantity: int = 1) -> None:
        """Add item to cart"""
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 1:
            raise ValueError("Quantity must be at least 1")
        
        self.items.append({
            "name": name,
            "price": price,
            "quantity": quantity
        })
    
    def remove_item(self, name: str) -> bool:
        """Remove item from cart"""
        for item in self.items:
            if item["name"] == name:
                self.items.remove(item)
                return True
        return False
    
    def get_total(self) -> float:
        """Calculate total price"""
        return sum(item["price"] * item["quantity"] for item in self.items)
    
    def get_item_count(self) -> int:
        """Get total number of items"""
        return sum(item["quantity"] for item in self.items)
    
    def clear(self) -> None:
        """Remove all items"""
        self.items.clear()


@pytest.fixture
def cart():
    """Provide fresh shopping cart for each test"""
    return ShoppingCart()


class TestShoppingCart:
    """Test cases for ShoppingCart"""
    
    def test_empty_cart(self, cart):
        """Test new cart is empty"""
        assert cart.get_total() == 0
        assert cart.get_item_count() == 0
    
    def test_add_item(self, cart):
        """Test adding items"""
        cart.add_item("Apple", 1.50, 3)
        assert cart.get_item_count() == 3
        assert cart.get_total() == 4.50
    
    def test_add_multiple_items(self, cart):
        """Test adding multiple different items"""
        cart.add_item("Apple", 1.50, 2)
        cart.add_item("Banana", 0.75, 3)
        assert cart.get_item_count() == 5
        assert cart.get_total() == 5.25
    
    def test_remove_item(self, cart):
        """Test removing items"""
        cart.add_item("Apple", 1.50, 2)
        cart.add_item("Banana", 0.75, 3)
        
        result = cart.remove_item("Apple")
        assert result is True
        assert cart.get_item_count() == 3
    
    def test_remove_nonexistent_item(self, cart):
        """Test removing item that doesn't exist"""
        cart.add_item("Apple", 1.50, 2)
        result = cart.remove_item("Orange")
        assert result is False
    
    def test_clear_cart(self, cart):
        """Test clearing cart"""
        cart.add_item("Apple", 1.50, 2)
        cart.add_item("Banana", 0.75, 3)
        cart.clear()
        assert cart.get_item_count() == 0
        assert cart.get_total() == 0
    
    def test_negative_price(self, cart):
        """Test adding item with negative price"""
        with pytest.raises(ValueError, match="Price cannot be negative"):
            cart.add_item("Apple", -1.50, 2)
    
    def test_invalid_quantity(self, cart):
        """Test adding item with invalid quantity"""
        with pytest.raises(ValueError, match="Quantity must be at least 1"):
            cart.add_item("Apple", 1.50, 0)


# Marks - categorize tests
@pytest.mark.slow
def test_slow_operation():
    """Test marked as slow"""
    # Simulate slow operation
    import time
    time.sleep(0.1)
    assert True


@pytest.mark.skip(reason="Not implemented yet")
def test_future_feature():
    """Test to be implemented"""
    pass


@pytest.mark.skipif(True, reason="Skipping for demo")
def test_conditional_skip():
    """Test that is conditionally skipped"""
    assert True


# Run specific marks:
# pytest -m slow          # Run only slow tests
# pytest -m "not slow"    # Skip slow tests


# TODO: Write parametrized tests for a function that checks if a string is a palindrome
# TODO: Create fixtures for a User class with name, email, and age
# TODO: Write tests for a function that validates passwords (length, special chars, etc.)
# TODO: Create a test class for a BankAccount with deposits and withdrawals
