"""
================================================================================
TOPIC: Type Conversion & Casting (Implicit vs Explicit)
================================================================================
SHORT THEORY:
- Implicit Type Conversion (Coercion): Python automatically promotes a lower
  data type to a higher data type to prevent data loss (e.g., int + float -> float).
- Explicit Type Conversion (Type Casting): The programmer manually converts a
  data type to another using built-in constructors like `int()`, `float()`, 
  `str()`, `bool()`, `list()`, `tuple()`.

SYNTAX REFERENCE:
    int("123")         # Convert numeric string or float to integer
    float("3.14")      # Convert numeric string or int to float
    str(100)           # Convert any object to its string representation
    bool(val)          # Convert to boolean (Truthiness evaluation)
    bin(), oct(), hex()# Base conversion

KEY TAKEAWAYS / PITFALLS:
- Converting a float to an int truncates the decimal part (it does NOT round).
  `int(3.9)` -> `3`. Use `round()` for standard rounding.
- Non-empty collections and non-zero numbers evaluate to `True`.
  `0`, `0.0`, `""`, `[]`, `{}`, `set()`, `None` evaluate to `False`.
- `int("12.34")` raises `ValueError`! Convert via `int(float("12.34"))`.
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

# Example 1: Implicit Conversion (Type Coercion)
int_num = 15
float_num = 4.5
result = int_num + float_num
print(f"Result: {result}, Type: {type(result)}")  # Output: 19.5, <class 'float'>

# Example 2: Explicit Casting (Strings to Numbers)
s_int = "100"
s_float = "25.75"

num_a = int(s_int)
num_b = float(s_float)
print(f"Sum: {num_a + num_b}")  # Output: 125.75

# Example 3: Truncation vs Rounding
pi_float = 3.84
print(f"Truncated with int(): {int(pi_float)}")   # Output: 3
print(f"Rounded with round(): {round(pi_float)}") # Output: 4

# Example 4: Truthiness and Boolean Conversion
falsy_values = [0, 0.0, "", [], {}, set(), None, False]
truthy_values = [1, -5, "Hello", [0], {"k": "v"}, True]

print("Falsy evaluations:")
for val in falsy_values:
    print(f"bool({repr(val)}) -> {bool(val)}")

print("\nTruthy evaluations:")
for val in truthy_values:
    print(f"bool({repr(val)}) -> {bool(val)}")

# Example 5: Handling Base Conversions
number = 42
print(f"Binary of {number}: {bin(number)}")   # 0b101010
print(f"Octal of {number}: {oct(number)}")    # 0o52
print(f"Hex of {number}: {hex(number)}")      # 0x2a
print(f"Parse Hex back to int: {int('0x2a', 16)}")  # 42