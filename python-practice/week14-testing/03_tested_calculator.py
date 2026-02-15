# Week 14: Mini Project - Tested Calculator
# Run tests: pytest week14-testing/03_tested_calculator.py -v
# Run program: python3 week14-testing/03_tested_calculator.py

import pytest
from typing import List, Optional


class CalculatorError(Exception):
    """Base exception for calculator errors"""
    pass


class DivisionByZeroError(CalculatorError):
    """Raised when dividing by zero"""
    pass


class InvalidOperationError(CalculatorError):
    """Raised when operation is invalid"""
    pass


class Calculator:
    """Calculator with history and error handling"""
    
    def __init__(self):
        self.result: float = 0
        self.history: List[str] = []
    
    def add(self, value: float) -> float:
        """Add value to result"""
        old_result = self.result
        self.result += value
        self._add_to_history(f"{old_result} + {value} = {self.result}")
        return self.result
    
    def subtract(self, value: float) -> float:
        """Subtract value from result"""
        old_result = self.result
        self.result -= value
        self._add_to_history(f"{old_result} - {value} = {self.result}")
        return self.result
    
    def multiply(self, value: float) -> float:
        """Multiply result by value"""
        old_result = self.result
        self.result *= value
        self._add_to_history(f"{old_result} × {value} = {self.result}")
        return self.result
    
    def divide(self, value: float) -> float:
        """Divide result by value"""
        if value == 0:
            raise DivisionByZeroError("Cannot divide by zero")
        old_result = self.result
        self.result /= value
        self._add_to_history(f"{old_result} ÷ {value} = {self.result}")
        return self.result
    
    def power(self, exponent: float) -> float:
        """Raise result to power"""
        old_result = self.result
        self.result = self.result ** exponent
        self._add_to_history(f"{old_result} ^ {exponent} = {self.result}")
        return self.result
    
    def square_root(self) -> float:
        """Calculate square root of result"""
        if self.result < 0:
            raise InvalidOperationError("Cannot calculate square root of negative number")
        old_result = self.result
        self.result = self.result ** 0.5
        self._add_to_history(f"√{old_result} = {self.result}")
        return self.result
    
    def percentage(self, percent: float) -> float:
        """Calculate percentage of result"""
        old_result = self.result
        self.result = (self.result * percent) / 100
        self._add_to_history(f"{percent}% of {old_result} = {self.result}")
        return self.result
    
    def clear(self) -> None:
        """Reset result to zero"""
        self.result = 0
        self._add_to_history("Cleared")
    
    def get_result(self) -> float:
        """Get current result"""
        return self.result
    
    def get_history(self) -> List[str]:
        """Get calculation history"""
        return self.history.copy()
    
    def clear_history(self) -> None:
        """Clear calculation history"""
        self.history.clear()
    
    def _add_to_history(self, entry: str) -> None:
        """Add entry to history"""
        self.history.append(entry)
    
    def __str__(self) -> str:
        return f"Calculator(result={self.result})"


# ============= TESTS =============

@pytest.fixture
def calc():
    """Provide fresh calculator for each test"""
    return Calculator()


class TestBasicOperations:
    """Test basic arithmetic operations"""
    
    def test_initial_result(self, calc):
        """Calculator should start at zero"""
        assert calc.get_result() == 0
    
    def test_add(self, calc):
        """Test addition"""
        calc.add(5)
        assert calc.get_result() == 5
        calc.add(3)
        assert calc.get_result() == 8
    
    def test_add_negative(self, calc):
        """Test adding negative numbers"""
        calc.add(-5)
        assert calc.get_result() == -5
    
    def test_subtract(self, calc):
        """Test subtraction"""
        calc.add(10)
        calc.subtract(3)
        assert calc.get_result() == 7
    
    def test_multiply(self, calc):
        """Test multiplication"""
        calc.add(5)
        calc.multiply(3)
        assert calc.get_result() == 15
    
    def test_multiply_by_zero(self, calc):
        """Test multiplying by zero"""
        calc.add(10)
        calc.multiply(0)
        assert calc.get_result() == 0
    
    def test_divide(self, calc):
        """Test division"""
        calc.add(10)
        calc.divide(2)
        assert calc.get_result() == 5
    
    def test_divide_by_zero(self, calc):
        """Test division by zero raises error"""
        calc.add(10)
        with pytest.raises(DivisionByZeroError, match="Cannot divide by zero"):
            calc.divide(0)
    
    @pytest.mark.parametrize("initial,operation,value,expected", [
        (10, "add", 5, 15),
        (10, "subtract", 3, 7),
        (10, "multiply", 2, 20),
        (10, "divide", 2, 5),
    ])
    def test_operations_parametrized(self, calc, initial, operation, value, expected):
        """Test operations with multiple values"""
        calc.add(initial)
        getattr(calc, operation)(value)
        assert calc.get_result() == expected


class TestAdvancedOperations:
    """Test advanced operations"""
    
    def test_power(self, calc):
        """Test power operation"""
        calc.add(2)
        calc.power(3)
        assert calc.get_result() == 8
    
    def test_power_zero(self, calc):
        """Test raising to power of zero"""
        calc.add(5)
        calc.power(0)
        assert calc.get_result() == 1
    
    def test_square_root(self, calc):
        """Test square root"""
        calc.add(16)
        calc.square_root()
        assert calc.get_result() == 4
    
    def test_square_root_negative(self, calc):
        """Test square root of negative number"""
        calc.add(-4)
        with pytest.raises(InvalidOperationError, match="Cannot calculate square root"):
            calc.square_root()
    
    def test_percentage(self, calc):
        """Test percentage calculation"""
        calc.add(200)
        calc.percentage(50)
        assert calc.get_result() == 100
    
    @pytest.mark.parametrize("value,percent,expected", [
        (100, 10, 10),
        (200, 50, 100),
        (50, 20, 10),
    ])
    def test_percentage_parametrized(self, calc, value, percent, expected):
        """Test percentage with multiple values"""
        calc.add(value)
        calc.percentage(percent)
        assert calc.get_result() == expected


class TestHistory:
    """Test calculation history"""
    
    def test_empty_history(self, calc):
        """New calculator should have empty history"""
        assert len(calc.get_history()) == 0
    
    def test_history_records_operations(self, calc):
        """History should record all operations"""
        calc.add(5)
        calc.multiply(2)
        calc.subtract(3)
        
        history = calc.get_history()
        assert len(history) == 3
        assert "0 + 5 = 5" in history[0]
        assert "5 × 2 = 10" in history[1]
        assert "10 - 3 = 7" in history[2]
    
    def test_clear_history(self, calc):
        """Test clearing history"""
        calc.add(5)
        calc.multiply(2)
        calc.clear_history()
        assert len(calc.get_history()) == 0
    
    def test_clear_adds_to_history(self, calc):
        """Test that clear operation is recorded"""
        calc.add(10)
        calc.clear()
        history = calc.get_history()
        assert "Cleared" in history[-1]


class TestChainedOperations:
    """Test chaining multiple operations"""
    
    def test_complex_calculation(self, calc):
        """Test complex chained calculation"""
        calc.add(10)
        calc.multiply(2)
        calc.subtract(5)
        calc.divide(3)
        assert pytest.approx(calc.get_result(), 0.01) == 5.0
    
    def test_calculation_with_clear(self, calc):
        """Test calculation with clear in middle"""
        calc.add(100)
        calc.multiply(2)
        calc.clear()
        calc.add(50)
        assert calc.get_result() == 50


# ============= INTERACTIVE PROGRAM =============

def main():
    """Interactive calculator program"""
    calc = Calculator()
    
    print("=" * 50)
    print("  TESTED CALCULATOR")
    print("=" * 50)
    print("\nOperations:")
    print("  +  : Add")
    print("  -  : Subtract")
    print("  *  : Multiply")
    print("  /  : Divide")
    print("  ^  : Power")
    print("  √  : Square root")
    print("  %  : Percentage")
    print("  c  : Clear")
    print("  h  : Show history")
    print("  q  : Quit")
    print("=" * 50)
    
    while True:
        print(f"\nCurrent result: {calc.get_result()}")
        operation = input("Enter operation: ").strip().lower()
        
        if operation == "q":
            print("Goodbye!")
            break
        
        elif operation == "c":
            calc.clear()
            print("✅ Cleared")
        
        elif operation == "h":
            history = calc.get_history()
            if history:
                print("\n--- History ---")
                for entry in history:
                    print(f"  {entry}")
            else:
                print("No history yet")
        
        elif operation == "√":
            try:
                result = calc.square_root()
                print(f"✅ Result: {result}")
            except InvalidOperationError as e:
                print(f"❌ Error: {e}")
        
        elif operation in ["+", "-", "*", "/", "^", "%"]:
            try:
                value = float(input("Enter value: "))
                
                if operation == "+":
                    result = calc.add(value)
                elif operation == "-":
                    result = calc.subtract(value)
                elif operation == "*":
                    result = calc.multiply(value)
                elif operation == "/":
                    result = calc.divide(value)
                elif operation == "^":
                    result = calc.power(value)
                elif operation == "%":
                    result = calc.percentage(value)
                
                print(f"✅ Result: {result}")
            
            except (DivisionByZeroError, InvalidOperationError) as e:
                print(f"❌ Error: {e}")
            except ValueError:
                print("❌ Invalid number")
        
        else:
            print("❌ Invalid operation")


if __name__ == "__main__":
    # Check if running tests or program
    import sys
    if "pytest" not in sys.modules:
        main()


# TODO: Add memory functions (store, recall, clear memory)
# TODO: Add trigonometric functions (sin, cos, tan)
# TODO: Add ability to undo last operation
# TODO: Save and load calculation history to file
# TODO: Add support for expressions like "2 + 3 * 4"
