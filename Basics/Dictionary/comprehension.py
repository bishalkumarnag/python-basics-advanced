"""
================================================================================
TOPIC: Dictionary Comprehensions in Python
================================================================================
SHORT THEORY:
- A dictionary comprehension provides a concise syntax to transform or filter 
  one dictionary or iterable into a new dictionary.
- Follows the mathematical set-builder notation: `{key_expr: val_expr for item in iterable if condition}`.
- Much faster and more readable than instantiating an empty dictionary and filling it 
  with a standard `for` loop.

SYNTAX REFERENCE:
    {key_expr: value_expr for item in iterable}
    {key_expr: value_expr for item in iterable if condition}
    {key_expr: (val1 if condition else val2) for item in iterable}

KEY TAKEAWAYS / PITFALLS:
- If `key_expr` yields duplicate keys during the comprehension, only the LAST 
  evaluated value will be stored (previous values will be overwritten).
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

# Example 1: Basic Numerical Transformations
# Squares of numbers from 1 to 10
squares = {n: n**2 for n in range(1, 11)}
print(f"Squares 1..10: {squares}")

# Example 2: Filtering with Conditional `if`
student_marks = {
    "Math": 95,
    "Science": 72,
    "English": 88,
    "History": 59,
    "Coding": 98
}

# Keep only distinction subjects (>= 85)
distinctions = {sub: mark for sub, mark in student_marks.items() if mark >= 85}
print(f"\nDistinction subjects: {distinctions}")

# Example 3: Inverting a Dictionary (Swap Keys and Values)
status_codes = {"OK": 200, "CREATED": 201, "BAD_REQUEST": 400, "NOT_FOUND": 404}
code_to_status = {code: status for status, code in status_codes.items()}
print(f"\nInverted map (Code -> Status): {code_to_status}")

# Example 4: Categorization with Ternary if-else in Value Expression
performance = {sub: ("Pass" if mark >= 60 else "Remedial") for sub, mark in student_marks.items()}
print(f"\nSubject performance status: {performance}")

# Example 5: Pairing Two Lists using zip() Inside Comprehension
keys = ["name", "designation", "location"]
values = ["Bishal", "Senior Python Engineer", "Bengaluru"]
user_profile = {k: v for k, v in zip(keys, values)}
print(f"\nConstructed profile from lists: {user_profile}")
