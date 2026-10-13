"""
================================================================================
TOPIC: Decorators in Python (Functions as First-Class Citizens, Wrappers)
================================================================================
SHORT THEORY:
- A decorator is a design pattern that allows adding new behavior to an existing 
  function or method WITHOUT modifying its source code.
- In Python, functions are first-class objects:
  1. Functions can be passed as arguments to other functions.
  2. Functions can be defined inside other functions (nested/inner functions).
  3. Functions can return other functions.
- A decorator takes a function as input, wraps it with extra functionality inside 
  an inner wrapper function, and returns the wrapper.
- The `@decorator_name` syntactic sugar is equivalent to: `func = decorator_name(func)`.

SYNTAX REFERENCE:
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            # Code executed BEFORE original function
            result = func(*args, **kwargs)
            # Code executed AFTER original function
            return result
        return wrapper

    @my_decorator
    def greet(): ...

KEY TAKEAWAYS / PITFALLS:
- Always use `*args, **kwargs` in the wrapper function so that the decorator can 
  wrap functions with any number of positional or keyword parameters.
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

import time

# Example 1: Execution Time Benchmark Decorator
def timer_decorator(func):
    """Measures and logs elapsed execution time of a function."""
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed = end_time - start_time
        print(f"[BENCHMARK]: {func.__name__} took {elapsed:.6f} seconds to complete.")
        return result
    return wrapper


# Applying @timer_decorator
@timer_decorator
def compute_heavy_sum(limit: int) -> int:
    return sum(range(limit))

print(f"Result: {compute_heavy_sum(1000000)}")


# Example 2: Audit Logging Decorator
def audit_log(func):
    """Logs function calls, arguments, and return values."""
    def wrapper(*args, **kwargs):
        arg_str = ", ".join([repr(a) for a in args] + [f"{k}={repr(v)}" for k, v in kwargs.items()])
        print(f"[AUDIT LOG]: Calling {func.__name__}({arg_str})")
        result = func(*args, **kwargs)
        print(f"[AUDIT LOG]: {func.__name__} returned {result}")
        return result
    return wrapper


@audit_log
def transfer_money(sender: str, recipient: str, amount: float) -> bool:
    print(f"Executing transfer: ${amount:,.2f} from {sender} to {recipient}")
    return True

transfer_money("Bishal", "Ananya", 2500.0)
