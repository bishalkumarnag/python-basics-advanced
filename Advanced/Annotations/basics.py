"""
================================================================================
TOPIC: Type Annotations & Function Signatures (PEP 484)
================================================================================
SHORT THEORY:
- Type annotations allow developers to specify expected data types for variables, 
  function parameters, and return values.
- Python remains dynamically typed: Type hints are NOT enforced at runtime by default. 
  The Python interpreter does not crash if you pass a string to an `int` parameter.
- Purpose:
  1. Documentation: Code is self-explanatory for teammates.
  2. IDE Intelligence: Enables autocomplete, auto-refactoring, and inline bug detection.
  3. Static Analysis: Tools like `mypy` and `pyright` catch type mismatches before production.
- Metadata is stored in the function's `__annotations__` dictionary attribute.

SYNTAX REFERENCE:
    variable: int = 10
    def add(a: int, b: int) -> int: ...
    def greet(name: str) -> None: ...
    func.__annotations__               # Dictionary of defined annotations

KEY TAKEAWAYS / PITFALLS:
- Type hints do NOT add runtime overhead; they are purely metadata.
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

# Example 1: Annotated Function Signatures
def calculate_tax(income: float, rate: float = 0.18) -> float:
    """Calculates tax liability given income and decimal rate."""
    return income * rate

print(f"Tax on $80,000 at 18%: ${calculate_tax(80000.0):,.2f}")

# Example 2: Inspecting Runtime __annotations__
print(f"Annotations dictionary: {calculate_tax.__annotations__}")
# Output: {'income': <class 'float'>, 'rate': <class 'float'>, 'return': <class 'float'>}

# Example 3: Runtime Dynamic Nature Demonstration
def concatenate_or_add(a: int, b: int) -> int:
    return a + b

print(f"Valid call (int):    {concatenate_or_add(5, 10)}")   # 15
# Python still allows strings even though annotated with int (interpreter doesn't enforce):
print(f"Bypassed call (str): {concatenate_or_add('Py', 'thon')}") # 'Python'