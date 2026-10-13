"""
================================================================================
TOPIC: Operators in Python (Arithmetic, Comparison, Logical, Bitwise, Identity)
================================================================================
SHORT THEORY:
- Operators are special symbols that perform computations on operands.
- Python categories operators into:
  1. Arithmetic: `+`, `-`, `*`, `/` (float div), `//` (floor div), `%` (modulo), `**` (power)
  2. Comparison: `==`, `!=`, `>`, `<`, `>=`, `<=` (return boolean `True`/`False`)
  3. Logical: `and`, `or`, `not` (support short-circuit evaluation)
  4. Identity: `is`, `is not` (test whether two references point to the SAME object in memory)
  5. Membership: `in`, `not in` (test whether a value is present in an iterable)
  6. Bitwise: `&`, `|`, `^`, `~`, `<<`, `>>` (operate bit-by-bit on integer binaries)

SYNTAX & PRECEDENCE HIERARCHY (High to Low):
    1. Parentheses: `()`
    2. Exponentiation: `**`
    3. Unary minus, bitwise NOT: `+x`, `-x`, `~x`
    4. Multiplication, Division, Modulo, Floor Div: `*`, `/`, `%`, `//`
    5. Addition, Subtraction: `+`, `-`
    6. Bitwise shifts: `<<`, `>>`
    7. Bitwise AND, XOR, OR: `&`, `^`, `|`
    8. Comparison, Identity, Membership: `==`, `!=`, `<`, `<=`, `>`, `>=`, `is`, `in`
    9. Logical NOT, AND, OR: `not`, `and`, `or`

KEY TAKEAWAYS / PITFALLS:
- `==` checks VALUE equality (`a == b`), whereas `is` checks IDENTITY/memory address (`id(a) == id(b)`).
- Never use `== None`; always use `is None` or `is not None`.
- Division `/` ALWAYS yields a `float`, even for `4 / 2` -> `2.0`. Use `//` for floor integer division.
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

# Example 1: Arithmetic Operators & Division Nuances
a, b = 17, 5
print(f"Addition: {a} + {b} = {a + b}")           # 22
print(f"Subtraction: {a} - {b} = {a - b}")        # 12
print(f"Multiplication: {a} * {b} = {a * b}")     # 85
print(f"True Division (/): {a} / {b} = {a / b}")  # 3.4 (Always float)
print(f"Floor Division (//): {a} // {b} = {a // b}") # 3 (Truncated int)
print(f"Modulo (%): {a} % {b} = {a % b}")         # 2 (Remainder)
print(f"Power (**): 2 ** 4 = {2 ** 4}")           # 16
print(f"Square root with **: 100 ** 0.5 = {100 ** 0.5}") # 10.0

# Example 2: Comparison & Chained Comparisons (Pythonic)
age = 25
# In Python, comparisons can be chained naturally:
print(f"Is age between 18 and 65: {18 <= age < 65}")  # True
print(f"Equality check: {5 == 5.0}")                 # True (value match)

# Example 3: Logical Operators & Short-Circuit Evaluation
has_id = True
has_ticket = False
# `and` requires both True; `or` requires at least one True
print(f"Can enter with ticket AND id: {has_id and has_ticket}")  # False
print(f"Can enter with ticket OR id: {has_id or has_ticket}")    # True
print(f"Not has_ticket: {not has_ticket}")                       # True

# Short-circuiting: second operand isn't evaluated if first determines result
default_name = None or "Guest"
print(f"Default name fallback: {default_name}")                  # "Guest"

# Example 4: Identity (is) vs Equality (==)
list_1 = [1, 2, 3]
list_2 = [1, 2, 3]
list_3 = list_1

print(f"list_1 == list_2: {list_1 == list_2}")  # True (same values)
print(f"list_1 is list_2: {list_1 is list_2}")  # False (different objects in memory)
print(f"list_1 is list_3: {list_1 is list_3}")  # True (referencing same object)

# Example 5: Membership Operators (in, not in)
fruits = ["apple", "banana", "mango"]
print(f"'banana' in fruits: {'banana' in fruits}")         # True
print(f"'cherry' not in fruits: {'cherry' not in fruits}") # True

# Example 6: Bitwise Operators
x, y = 5, 3  # 5 is 0b0101, 3 is 0b0011
print(f"Bitwise AND (5 & 3): {x & y}")  # 0b0001 -> 1
print(f"Bitwise OR (5 | 3): {x | y}")   # 0b0111 -> 7
print(f"Bitwise XOR (5 ^ 3): {x ^ y}")  # 0b0110 -> 6
print(f"Bitwise Shift Left (5 << 1): {x << 1}") # 10 (multiplied by 2)