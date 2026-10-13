"""
================================================================================
TOPIC: Exception Handling in Python (try, except, else, finally)
================================================================================
SHORT THEORY:
- Exceptions are runtime errors that disrupt the normal flow of program execution.
- Exception Handling blocks:
  1. `try`: Contains code that might raise an exception.
  2. `except [ExceptionType]`: Catches and handles specific exceptions.
  3. `else`: Runs ONLY if the `try` block succeeded WITHOUT raising any exception.
  4. `finally`: ALWAYS runs regardless of whether an exception occurred, was handled, 
     or was re-raised (crucial for resource cleanup like closing files or connections).
- Common Built-in Exceptions:
  `ValueError`, `TypeError`, `ZeroDivisionError`, `IndexError`, `KeyError`, 
  `FileNotFoundError`, `AttributeError`, `ImportError`, `StopIteration`.

SYNTAX REFERENCE:
    try:
        # risky operation
    except (ValueError, TypeError) as err:
        # handle multiple specific errors
    except Exception as general_err:
        # fallback catch-all
    else:
        # executed only on success
    finally:
        # always executed for cleanup

KEY TAKEAWAYS / PITFALLS:
- Avoid bare `except:`! It catches `KeyboardInterrupt` (Ctrl+C) and `SystemExit`, 
  preventing clean program termination. Always catch `except Exception:` at minimum.
- Order specific exception types before generic ones (`ValueError` before `Exception`).
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

# Example 1: Robust Number Division with Specific Error Handlers
def safe_divide(numerator: float, denominator: float) -> float | None:
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        print("[ERROR]: Division by zero is mathematically undefined.")
        return None
    except TypeError as te:
        print(f"[ERROR]: Invalid data type passed to division: {te}")
        return None
    else:
        print(f"[SUCCESS]: Division computed successfully: {result}")
        return result
    finally:
        print("[CLEANUP]: Division operation routine completed.\n")


safe_divide(10, 2)     # Success case
safe_divide(10, 0)     # ZeroDivisionError handled
safe_divide(10, "two") # TypeError handled


# Example 2: Catching Multiple Exception Types Simultaneously
def parse_and_fetch_element(items: list[str], index_str: str) -> str | None:
    try:
        idx = int(index_str)
        return items[idx]
    except (ValueError, IndexError) as err:
        print(f"Failed to access item at '{index_str}': {err.__class__.__name__} - {err}")
        return None

fruits = ["apple", "banana", "cherry"]
print("Valid fetch:   ", parse_and_fetch_element(fruits, "1"))
print("Out of bounds: ", parse_and_fetch_element(fruits, "99"))
print("Invalid string:", parse_and_fetch_element(fruits, "abc"))