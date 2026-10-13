"""
================================================================================
TOPIC: Built-in Data Types in Python
================================================================================
SHORT THEORY:
- Python categories data types into:
  1. Numeric: `int`, `float`, `complex`
  2. Text / Sequence: `str`
  3. Boolean: `bool` (Subclass of int: True == 1, False == 0)
  4. None Type: `NoneType` (Represents absence of a value)
  5. Collections (Sequences/Mappings/Sets): `list`, `tuple`, `dict`, `set`
- Mutable types (can be changed in-place): `list`, `dict`, `set`
- Immutable types (cannot be modified after creation): `int`, `float`, `str`, `tuple`, `frozenset`, `bool`

SYNTAX REFERENCE:
    type(obj)                 # Returns the type of obj
    isinstance(obj, type)     # Checks if obj is an instance of a type (preferred)
    complex(real, imag)       # Creates a complex number (or literal: 3 + 4j)

KEY TAKEAWAYS / PITFALLS:
- Python 3 handles arbitrarily large integers without overflow (limited only by memory).
- Floating-point calculations have precision constraints due to IEEE-754 representation (e.g., 0.1 + 0.2 != 0.3).
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

# Example 1: Numeric Types
integer_val = 42
large_int = 10**30  # Arbitrarily large int
float_val = 3.14159
scientific_float = 1.5e-3  # 0.0015
complex_val = 3 + 4j

print(f"int: {integer_val}, type: {type(integer_val)}")
print(f"large int: {large_int}")
print(f"float: {float_val}, scientific: {scientific_float}")
print(f"complex: {complex_val}, real part: {complex_val.real}, imag part: {complex_val.imag}")

# Example 2: Booleans as Integers
flag_true = True
flag_false = False
print(f"True + True = {flag_true + flag_true}")    # Output: 2
print(f"True == 1: {flag_true == 1}")              # Output: True
print(f"False == 0: {flag_false == 0}")            # Output: True

# Example 3: NoneType (The Pythonic Null)
empty_val = None
print(f"empty_val is: {empty_val}, type: {type(empty_val)}")
# Idiomatic check for None uses identity operator `is`
if empty_val is None:
    print("Variable is currently unassigned or None")

# Example 4: Type Verification using isinstance()
score = 98.5
print(isinstance(score, (int, float)))  # True (checks multiple allowed types)
print(isinstance("hello", str))         # True
print(isinstance(True, int))            # True (bool is a subclass of int!)
