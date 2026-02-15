# Tests for Week 11 Bank Account System
# Run: pytest python-practice/tests/test_bank_account.py -v

import pytest
import sys
import os

# Add parent directory to path to import the module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from week11_oop.bank_account_03 import BankAccount, SavingsAccount, CheckingAccount


class TestBankAccount:
    """Test basic BankAccount functionality"""
    
    def test_initial_balance(self):
        """Test account starts with correct balance"""
        account = BankAccount("John Doe", 1000)
        assert account.get_balance() == 1000
    
    def test_zero_initial_balance(self):
        """Test account can start with zero balance"""
        account = BankAccount("Jane Doe")
        assert account.get_balance() == 0
    
    def test_deposit(self):
        """Test depositing money"""
        account = BankAccount("John Doe", 100)
        account.deposit(50)
        assert account.get_balance() == 150
    
    def test_deposit_negative(self):
        """Test depositing negative amount does nothing"""
        account = BankAccount("John Doe", 100)
        account.deposit(-50)
        assert account.get_balance() == 100
    
    def test_withdraw_success(self):
        """Test successful withdrawal"""
        account = BankAccount("John Doe", 100)
        result = account.withdraw(50)
        assert result is True
        assert account.get_balance() == 50
    
    def test_withdraw_insufficient_funds(self):
        """Test withdrawal with insufficient funds"""
        account = BankAccount("John Doe", 100)
        result = account.withdraw(150)
        assert result is False
        assert account.get_balance() == 100
    
    def test_withdraw_negative(self):
        """Test withdrawing negative amount"""
        account = BankAccount("John Doe", 100)
        result = account.withdraw(-50)
        assert result is False
        assert account.get_balance() == 100
    
    def test_transaction_history(self):
        """Test transaction history is recorded"""
        account = BankAccount("John Doe", 100)
        account.deposit(50)
        account.withdraw(30)
        history = account.transaction_history
        assert len(history) >= 3  # Initial + deposit + withdrawal
    
    def test_account_number_generation(self):
        """Test unique account numbers are generated"""
        account1 = BankAccount("John Doe")
        account2 = BankAccount("Jane Doe")
        assert account1.account_number != account2.account_number


class TestSavingsAccount:
    """Test SavingsAccount functionality"""
    
    def test_interest_rate(self):
        """Test savings account has interest rate"""
        account = SavingsAccount("John Doe", 1000, 0.05)
        assert account.interest_rate == 0.05
    
    def test_add_interest(self):
        """Test adding interest"""
        account = SavingsAccount("John Doe", 1000, 0.10)
        account.add_interest()
        assert account.get_balance() == 1100
    
    def test_multiple_interest_additions(self):
        """Test adding interest multiple times"""
        account = SavingsAccount("John Doe", 1000, 0.10)
        account.add_interest()
        account.add_interest()
        assert account.get_balance() == pytest.approx(1210, 0.01)


class TestCheckingAccount:
    """Test CheckingAccount functionality"""
    
    def test_overdraft_limit(self):
        """Test checking account has overdraft limit"""
        account = CheckingAccount("John Doe", 100, 50)
        assert account.overdraft_limit == 50
    
    def test_withdraw_with_overdraft(self):
        """Test withdrawal using overdraft"""
        account = CheckingAccount("John Doe", 100, 50)
        result = account.withdraw(120)
        assert result is True
        assert account.get_balance() == -20
    
    def test_withdraw_exceeds_overdraft(self):
        """Test withdrawal exceeding overdraft limit"""
        account = CheckingAccount("John Doe", 100, 50)
        result = account.withdraw(200)
        assert result is False
        assert account.get_balance() == 100
    
    def test_overdraft_warning(self, capsys):
        """Test overdraft warning is displayed"""
        account = CheckingAccount("John Doe", 50, 100)
        account.withdraw(75)
        captured = capsys.readouterr()
        assert "overdraft" in captured.out.lower()


@pytest.fixture
def sample_accounts():
    """Provide sample accounts for testing"""
    return {
        "basic": BankAccount("Test User", 1000),
        "savings": SavingsAccount("Saver", 5000, 0.03),
        "checking": CheckingAccount("Checker", 500, 200)
    }


def test_multiple_accounts(sample_accounts):
    """Test working with multiple accounts"""
    assert len(sample_accounts) == 3
    assert sample_accounts["basic"].get_balance() == 1000
    assert sample_accounts["savings"].get_balance() == 5000
    assert sample_accounts["checking"].get_balance() == 500
