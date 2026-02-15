# Week 11: Mini Project - Bank Account System
# Run: python3 week11-oop/03_bank_account.py

from typing import List


class BankAccount:
    """Represents a bank account with basic operations"""
    
    # Class variable to track total accounts
    total_accounts = 0
    
    def __init__(self, account_holder: str, initial_balance: float = 0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transaction_history: List[str] = []
        
        # Generate account number
        BankAccount.total_accounts += 1
        self.account_number = f"ACC{BankAccount.total_accounts:04d}"
        
        # Record initial deposit
        if initial_balance > 0:
            self.transaction_history.append(f"Initial deposit: ${initial_balance:.2f}")
    
    def deposit(self, amount: float) -> None:
        """Deposit money into the account"""
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposit: +${amount:.2f}")
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive")
    
    def withdraw(self, amount: float) -> bool:
        """Withdraw money from the account"""
        if amount <= 0:
            print("Withdrawal amount must be positive")
            return False
        
        if amount > self.balance:
            print(f"Insufficient funds. Balance: ${self.balance:.2f}")
            return False
        
        self.balance -= amount
        self.transaction_history.append(f"Withdrawal: -${amount:.2f}")
        print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        return True
    
    def get_balance(self) -> float:
        """Return current balance"""
        return self.balance
    
    def show_transaction_history(self) -> None:
        """Display all transactions"""
        print(f"\n--- Transaction History for {self.account_holder} ---")
        print(f"Account Number: {self.account_number}")
        if not self.transaction_history:
            print("No transactions yet")
        else:
            for transaction in self.transaction_history:
                print(f"  {transaction}")
        print(f"Current Balance: ${self.balance:.2f}")
        print("-" * 50)
    
    def __str__(self) -> str:
        """String representation of the account"""
        return f"Account {self.account_number}: {self.account_holder} - ${self.balance:.2f}"


class SavingsAccount(BankAccount):
    """Savings account with interest rate"""
    
    def __init__(self, account_holder: str, initial_balance: float = 0, interest_rate: float = 0.02):
        super().__init__(account_holder, initial_balance)
        self.interest_rate = interest_rate
    
    def add_interest(self) -> None:
        """Add interest to the account"""
        interest = self.balance * self.interest_rate
        self.balance += interest
        self.transaction_history.append(f"Interest: +${interest:.2f}")
        print(f"Added ${interest:.2f} interest. New balance: ${self.balance:.2f}")


class CheckingAccount(BankAccount):
    """Checking account with overdraft protection"""
    
    def __init__(self, account_holder: str, initial_balance: float = 0, overdraft_limit: float = 100):
        super().__init__(account_holder, initial_balance)
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount: float) -> bool:
        """Withdraw with overdraft protection"""
        if amount <= 0:
            print("Withdrawal amount must be positive")
            return False
        
        available = self.balance + self.overdraft_limit
        
        if amount > available:
            print(f"Exceeds overdraft limit. Available: ${available:.2f}")
            return False
        
        self.balance -= amount
        self.transaction_history.append(f"Withdrawal: -${amount:.2f}")
        print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        
        if self.balance < 0:
            print(f"⚠️  Using overdraft: ${abs(self.balance):.2f}")
        
        return True


# Demo the bank account system
def main():
    print("=== Bank Account System ===\n")
    
    # Create accounts
    savings = SavingsAccount("Alice Johnson", 1000, 0.03)
    checking = CheckingAccount("Bob Smith", 500, 200)
    
    print(savings)
    print(checking)
    
    # Perform transactions
    print("\n--- Savings Account Transactions ---")
    savings.deposit(500)
    savings.withdraw(200)
    savings.add_interest()
    savings.show_transaction_history()
    
    print("\n--- Checking Account Transactions ---")
    checking.deposit(100)
    checking.withdraw(400)
    checking.withdraw(300)  # Will use overdraft
    checking.show_transaction_history()
    
    # Show total accounts
    print(f"\nTotal accounts created: {BankAccount.total_accounts}")


if __name__ == "__main__":
    main()


# TODO: Add a transfer() method to transfer money between accounts
# TODO: Create a CreditCard class that inherits from BankAccount
# TODO: Add a transaction limit feature (max transactions per day)
# TODO: Add a method to calculate total deposits and withdrawals
# TODO: Create a Bank class that manages multiple accounts
