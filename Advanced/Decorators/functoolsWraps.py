"""
================================================================================
TOPIC: Preserving Function Metadata with @functools.wraps & Class Decorators
================================================================================
SHORT THEORY:
- Problem: When you decorate a function, the original function is replaced by the `wrapper`.
  As a result, metadata like `func.__name__` and `func.__doc__` gets overwritten by the wrapper's 
  name and docstring! This breaks debuggers, Sphinx docs, and introspection.
- Solution: Decorate your inner `wrapper` with `@functools.wraps(func)`. 
  It copies original metadata (`__name__`, `__doc__`, `__annotations__`) to the wrapper.
- Class Decorators:
  1. A class that acts as a decorator (implements `__call__`).
  2. A decorator that decorates an entire class (e.g., adding class methods or attributes).

SYNTAX REFERENCE:
    from functools import wraps

    def my_decorator(func):
        @wraps(func)              # Preserves identity and docstring
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper

KEY TAKEAWAYS / PITFALLS:
- In production, ALWAYS use `@wraps(func)` on every custom decorator you write.
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

from functools import wraps

# Example 1: Demonstrating the Metadata Loss Issue vs @wraps Fix
def unwrap_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

def correct_decorator(func):
    @wraps(func)  # Crucial!
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@unwrap_decorator
def sample_function_bad():
    """This is the original docstring."""
    pass

@correct_decorator
def sample_function_good():
    """This is the original docstring."""
    pass

print(f"Without @wraps name: {sample_function_bad.__name__}") # 'wrapper' (LOST IDENTITY!)
print(f"With @wraps name:    {sample_function_good.__name__}") # 'sample_function_good' (PRESERVED!)
print(f"With @wraps doc:     {sample_function_good.__doc__}")


# Example 2: Class Implemented as a Decorator (using __call__)
class CallCounter:
    """Class-based decorator maintaining state of function invocation counts."""
    def __init__(self, func) -> None:
        self.func = func
        self.count = 0
        wraps(func)(self)  # Preserve metadata

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"[COUNTER]: {self.func.__name__} has been invoked {self.count} time(s).")
        return self.func(*args, **kwargs)


@CallCounter
def process_order(order_id: int):
    return f"Order #{order_id} fulfilled."

process_order(101)
process_order(102)
process_order(103)
print(f"Total processed invocations: {process_order.count}")
