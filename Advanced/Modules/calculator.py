"""
================================================================================
TOPIC: Python Modules & if __name__ == '__main__' Boilerplate
================================================================================
SHORT THEORY:
- A module in Python is simply a `.py` file containing Python code (functions, classes, constants).
- When a file is executed directly from the terminal, Python sets the special built-in 
  variable `__name__ = "__main__"`.
- When the file is imported by another module, Python sets `__name__ = "module_filename"` 
  (without the `.py`).
- The `if __name__ == "__main__":` idiom prevents test code or side-effects from executing 
  when the file is imported as a dependency into another program.

SYNTAX REFERENCE:
    # Inside module file:
    CONST_NAME = value
    def func(): ...

    if __name__ == "__main__":
        # Unit tests / CLI entry point

KEY TAKEAWAYS / PITFALLS:
- Never put top-level executable code with side-effects (like calling APIs or DB migrations) 
  outside functions or the `__name__ == '__main__'` block in a reusable module.
================================================================================
"""

# Module Constants
PI: float = 3.141592653589793
E: float = 2.718281828459045


# Module Functions
def add(a: float, b: float) -> float:
    """Returns the arithmetic sum of a and b."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Returns the arithmetic difference of a and b."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Returns the product of a and b."""
    return a * b


def divide(a: float, b: float) -> float:
    """Returns the quotient of a and b."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


# Standalone Execution Entry Point
if __name__ == "__main__":
    print(f"Executing '{__file__}' directly as main program:")
    print(f"PI constant: {PI}")
    print(f"add(15, 25) = {add(15, 25)}")
    print(f"multiply(4, 5) = {multiply(4, 5)}")