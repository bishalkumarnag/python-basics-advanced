"""
================================================================================
TOPIC: Custom Exceptions & Exception Hierarchies
================================================================================
SHORT THEORY:
- In production applications, built-in exception types (`ValueError`, etc.) are often 
  too generic to pinpoint domain-specific business rule violations.
- Custom exceptions are created by subclassing Python's built-in `Exception` class.
- Best Practice: Define a base exception for your module/application, then derive 
  specific error classes from it. This allows consumers to catch either the general 
  module error or granular sub-errors.

SYNTAX REFERENCE:
    class AppBaseError(Exception):
        \"\"\"Base exception for entire application.\"\"\"
        pass

    class GranularError(AppBaseError):
        def __init__(self, message, error_code):
            super().__init__(message)
            self.error_code = error_code

KEY TAKEAWAYS / PITFALLS:
- Inherit from `Exception`, NOT `BaseException`. (Catching `BaseException` interferes 
  with Python system exits).
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

# Application Exception Hierarchy
class BankingError(Exception):
    """Base exception for all banking operations."""
    pass


class InsufficientFundsError(BankingError):
    """Raised when withdrawal exceeds available balance."""
    def __init__(self, requested: float, available: float) -> None:
        message = f"Cannot withdraw ${requested:,.2f}; balance is only ${available:,.2f}."
        super().__init__(message)
        self.requested = requested
        self.available = available


class AccountFrozenError(BankingError):
    """Raised when an action is attempted on a locked account."""
    def __init__(self, account_id: str, reason: str = "Suspicious activity") -> None:
        super().__init__(f"Account '{account_id}' is frozen: {reason}")
        self.account_id = account_id
        self.reason = reason


# Bank Account implementation using custom errors
class BankAccount:
    def __init__(self, account_id: str, initial_balance: float, is_frozen: bool = False) -> None:
        self.account_id = account_id
        self.balance = initial_balance
        self.is_frozen = is_frozen

    def withdraw(self, amount: float) -> float:
        if self.is_frozen:
            raise AccountFrozenError(self.account_id, "Pending compliance audit")
        if amount > self.balance:
            raise InsufficientFundsError(requested=amount, available=self.balance)
        self.balance -= amount
        return self.balance


# Testing custom exception handling
acc = BankAccount("ACC-9012", 500.0, is_frozen=False)

# Scenario 1: Insufficient Funds
try:
    acc.withdraw(750.0)
except InsufficientFundsError as ife:
    print(f"Caught Specific Error: {ife}")
    print(f"  Shortage amount:     ${ife.requested - ife.available:,.2f}")
except BankingError as be:
    print(f"Caught General Banking Error: {be}")

# Scenario 2: Account Frozen
acc.is_frozen = True
try:
    acc.withdraw(100.0)
except BankingError as be:
    print(f"\nCaught Banking Error: {be.__class__.__name__}: {be}")