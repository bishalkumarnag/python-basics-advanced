"""
================================================================================
TOPIC: Raising & Re-raising Exceptions (raise statement)
================================================================================
SHORT THEORY:
- The `raise` keyword forces a specified exception to occur.
- Used for contract validation, pre-condition assertions, and failing fast on invalid inputs.
- Re-raising: A bare `raise` inside an `except` block re-raises the active exception 
  currently being handled, preserving the original traceback.
- Exception Chaining (`raise ... from original_err`): Links a high-level exception 
  to its underlying cause.

SYNTAX REFERENCE:
    raise ValueError("Descriptive failure message")
    raise CustomError("Failure") from original_error   # Exception chaining

    try:
        ...
    except SomeError:
        logger.error(...)
        raise                         # Re-raise active exception

KEY TAKEAWAYS / PITFALLS:
- Never raise generic `Exception("error")`. Raise specific built-in types (`ValueError`, `KeyError`, etc.) 
  or custom subclasses of `Exception`.
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

# Example 1: Input Validation with Explicit raise
def validate_registration_age(age: int) -> None:
    """Validates age boundary rules."""
    if not isinstance(age, int):
        raise TypeError(f"Age must be an integer, got {type(age).__name__}")
    if age < 0:
        raise ValueError("Age cannot be negative.")
    if age > 130:
        raise ValueError(f"Age {age} exceeds realistic human limits.")
    if age < 18:
        raise PermissionError("User must be at least 18 years old to register.")
    print(f"Age {age} successfully verified!")


# Testing validation checks
try:
    validate_registration_age(25)   # Valid
    validate_registration_age(-5)   # Triggers ValueError
except (ValueError, TypeError, PermissionError) as err:
    print(f"Validation Error caught: {err.__class__.__name__} -> {err}")


# Example 2: Re-raising Active Exceptions after Logging
def process_transaction(amount: float) -> None:
    try:
        if amount <= 0:
            raise ValueError(f"Invalid transaction amount: ${amount}")
        print(f"Transaction of ${amount} approved.")
    except ValueError as ve:
        print(f"[AUDIT LOG]: Logged failure for amount: {amount}")
        # Bare 'raise' forwards exception up the call stack:
        # raise (Commented to allow execution flow to continue demonstration)


process_transaction(-50.0)


# Example 3: Exception Chaining (raise ... from ...)
class DatabaseError(Exception):
    """Application-level database failure."""
    pass

def query_user(user_id: int):
    try:
        # Simulate low-level socket timeout
        raise ConnectionResetError("Remote server closed socket connection abruptly")
    except ConnectionResetError as net_err:
        # Chain low-level socket error into domain DatabaseError
        raise DatabaseError(f"Failed to fetch user {user_id}") from net_err

try:
    query_user(101)
except DatabaseError as db_err:
    print(f"\nCaught chained exception: {db_err}")
    print(f"Root underlying cause:   {db_err.__cause__}")