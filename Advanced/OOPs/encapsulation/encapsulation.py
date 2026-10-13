"""
================================================================================
TOPIC: Encapsulation & Access Modifiers in Python
================================================================================
SHORT THEORY:
- Encapsulation is the OOP principle of bundling data and methods that operate on 
  that data within a single unit, and restricting direct access to internal state.
- Python does not enforce strict access specifiers (`private`, `protected`, `public`) 
  at the language keyword level; it follows conventions:
  1. Public: `name` — Accessible from anywhere.
  2. Protected: `_name` (Single underscore) — Convention signaling internal use. 
     Should only be accessed within class and subclasses.
  3. Private: `__name` (Double underscore) — Triggers Python Name Mangling. 
     Python rewrites the identifier internally as `_ClassName__name` to prevent 
     accidental overriding in subclasses.

SYNTAX REFERENCE:
    class Account:
        def __init__(self, balance):
            self.public_id = "ACC-01"     # Public
            self._interest_rate = 0.05    # Protected convention
            self.__balance = balance      # Private (Name Mangling)

    # Name Mangling access:
    obj._Account__balance                 # Technical backdoor (not recommended)

KEY TAKEAWAYS / PITFALLS:
- Python operates on the "We are all consenting adults here" philosophy.
  Name mangling is meant to avoid namespace collisions in inheritance, NOT to provide 
  impenetrable cryptographic security.
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

class BankAccount:
    """Demonstrating data protection through encapsulation."""
    def __init__(self, account_holder: str, initial_balance: float) -> None:
        self.account_holder = account_holder   # Public attribute
        self._branch_code = "BR-702"           # Protected attribute convention
        self.__balance = initial_balance       # Private attribute (name-mangled)

    def deposit(self, amount: float) -> None:
        """Controlled public interface for state mutation."""
        if amount <= 0:
            raise ValueError("Deposit amount must be strictly positive.")
        self.__balance += amount
        print(f"Deposited ${amount:,.2f}. Current balance: ${self.__balance:,.2f}")

    def withdraw(self, amount: float) -> bool:
        """Business validation before balance decrement."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be strictly positive.")
        if amount > self.__balance:
            print("Transaction declined: Insufficient funds.")
            return False
        self.__balance -= amount
        print(f"Withdrew ${amount:,.2f}. Remaining balance: ${self.__balance:,.2f}")
        return True

    def get_balance(self) -> float:
        """Controlled read-only accessor."""
        return self.__balance


account = BankAccount("Bishal Nag", 1000.0)

# Accessing public attribute
print(f"Account holder: {account.account_holder}")

# Performing transactions via public interface
account.deposit(500.0)
account.withdraw(300.0)
print(f"Verified balance: ${account.get_balance():,.2f}")

# Attempting direct access to private attribute
try:
    print(account.__balance)
except AttributeError as err:
    print(f"\nDirect access blocked: {err}")

# How Name Mangling works internally under the hood:
print(f"Access via mangled name: ${account._BankAccount__balance:,.2f}")