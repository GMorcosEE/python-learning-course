# Week 14: Testing - unittest Basics
# Run: python3 -m unittest week14-testing/01_unittest_basics.py

import unittest


# Functions to test
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


def subtract(a: int, b: int) -> int:
    """Subtract b from a"""
    return a - b


def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b


def divide(a: float, b: float) -> float:
    """Divide a by b"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def is_even(n: int) -> bool:
    """Check if number is even"""
    return n % 2 == 0


def reverse_string(s: str) -> str:
    """Reverse a string"""
    return s[::-1]


# Test class
class TestMathFunctions(unittest.TestCase):
    """Test cases for math functions"""
    
    def test_add_positive_numbers(self):
        """Test adding positive numbers"""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(10, 20), 30)
    
    def test_add_negative_numbers(self):
        """Test adding negative numbers"""
        self.assertEqual(add(-5, -3), -8)
        self.assertEqual(add(-10, 5), -5)
    
    def test_subtract(self):
        """Test subtraction"""
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(5, 10), -5)
        self.assertEqual(subtract(0, 5), -5)
    
    def test_multiply(self):
        """Test multiplication"""
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 5), -10)
        self.assertEqual(multiply(0, 100), 0)
    
    def test_divide(self):
        """Test division"""
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(9, 3), 3)
        self.assertAlmostEqual(divide(10, 3), 3.333, places=3)
    
    def test_divide_by_zero(self):
        """Test division by zero raises error"""
        with self.assertRaises(ValueError):
            divide(10, 0)
    
    def test_is_even(self):
        """Test even number checker"""
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(0))
        self.assertTrue(is_even(-4))
        self.assertFalse(is_even(3))
        self.assertFalse(is_even(-5))


class TestStringFunctions(unittest.TestCase):
    """Test cases for string functions"""
    
    def test_reverse_string(self):
        """Test string reversal"""
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("Python"), "nohtyP")
        self.assertEqual(reverse_string(""), "")
        self.assertEqual(reverse_string("a"), "a")
    
    def test_reverse_string_palindrome(self):
        """Test reversing palindromes"""
        self.assertEqual(reverse_string("racecar"), "racecar")
        self.assertEqual(reverse_string("noon"), "noon")


# Test class with setup and teardown
class TestWithSetup(unittest.TestCase):
    """Test class demonstrating setUp and tearDown"""
    
    def setUp(self):
        """Run before each test method"""
        print("\n  Setting up test...")
        self.test_list = [1, 2, 3, 4, 5]
        self.test_dict = {"a": 1, "b": 2}
    
    def tearDown(self):
        """Run after each test method"""
        print("  Tearing down test...")
    
    def test_list_operations(self):
        """Test list operations"""
        self.assertEqual(len(self.test_list), 5)
        self.assertIn(3, self.test_list)
        self.test_list.append(6)
        self.assertEqual(len(self.test_list), 6)
    
    def test_dict_operations(self):
        """Test dictionary operations"""
        self.assertEqual(self.test_dict["a"], 1)
        self.assertIn("b", self.test_dict)
        self.test_dict["c"] = 3
        self.assertEqual(len(self.test_dict), 3)


# Testing a class
class Calculator:
    """Simple calculator class"""
    
    def __init__(self):
        self.result = 0
    
    def add(self, value: float) -> float:
        """Add to result"""
        self.result += value
        return self.result
    
    def subtract(self, value: float) -> float:
        """Subtract from result"""
        self.result -= value
        return self.result
    
    def multiply(self, value: float) -> float:
        """Multiply result"""
        self.result *= value
        return self.result
    
    def divide(self, value: float) -> float:
        """Divide result"""
        if value == 0:
            raise ValueError("Cannot divide by zero")
        self.result /= value
        return self.result
    
    def clear(self) -> None:
        """Reset result to zero"""
        self.result = 0
    
    def get_result(self) -> float:
        """Get current result"""
        return self.result


class TestCalculator(unittest.TestCase):
    """Test cases for Calculator class"""
    
    def setUp(self):
        """Create a fresh calculator for each test"""
        self.calc = Calculator()
    
    def test_initial_result(self):
        """Test calculator starts at zero"""
        self.assertEqual(self.calc.get_result(), 0)
    
    def test_add(self):
        """Test addition"""
        self.calc.add(5)
        self.assertEqual(self.calc.get_result(), 5)
        self.calc.add(3)
        self.assertEqual(self.calc.get_result(), 8)
    
    def test_subtract(self):
        """Test subtraction"""
        self.calc.add(10)
        self.calc.subtract(3)
        self.assertEqual(self.calc.get_result(), 7)
    
    def test_multiply(self):
        """Test multiplication"""
        self.calc.add(5)
        self.calc.multiply(3)
        self.assertEqual(self.calc.get_result(), 15)
    
    def test_divide(self):
        """Test division"""
        self.calc.add(10)
        self.calc.divide(2)
        self.assertEqual(self.calc.get_result(), 5)
    
    def test_divide_by_zero(self):
        """Test division by zero"""
        self.calc.add(10)
        with self.assertRaises(ValueError):
            self.calc.divide(0)
    
    def test_clear(self):
        """Test clearing result"""
        self.calc.add(100)
        self.calc.clear()
        self.assertEqual(self.calc.get_result(), 0)
    
    def test_chain_operations(self):
        """Test chaining multiple operations"""
        self.calc.add(10)
        self.calc.multiply(2)
        self.calc.subtract(5)
        self.calc.divide(3)
        self.assertAlmostEqual(self.calc.get_result(), 5, places=1)


# Common assertion methods:
# assertEqual(a, b)       - a == b
# assertNotEqual(a, b)    - a != b
# assertTrue(x)           - bool(x) is True
# assertFalse(x)          - bool(x) is False
# assertIs(a, b)          - a is b
# assertIsNot(a, b)       - a is not b
# assertIsNone(x)         - x is None
# assertIsNotNone(x)      - x is not None
# assertIn(a, b)          - a in b
# assertNotIn(a, b)       - a not in b
# assertIsInstance(a, b)  - isinstance(a, b)
# assertRaises(exc)       - raises exception
# assertAlmostEqual(a, b) - round(a-b, 7) == 0


if __name__ == "__main__":
    # Run tests with verbose output
    unittest.main(verbosity=2)


# TODO: Write tests for a function that finds the maximum in a list
# TODO: Create tests for a function that validates email addresses
# TODO: Write tests for a class that manages a shopping cart
# TODO: Add tests that check for specific error messages
