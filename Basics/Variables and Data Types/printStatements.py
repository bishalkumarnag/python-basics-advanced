"""
================================================================================
TOPIC: Output Formatting & print() in Python
================================================================================
SHORT THEORY:
- The built-in `print()` function sends text output to standard output (sys.stdout).
- `sep`: Defines the string inserted between values (default is a space `" "`).
- `end`: Defines what is appended at the very end of the output (default is newline `"\n"`).
- Formatting options:
  1. f-strings (Python 3.6+): `f"Hello {name}"` (Fastest, cleanest, recommended)
  2. `str.format()`: `"Hello {}".format(name)`
  3. `%` operator: `"Hello %s" % name` (Legacy C-style)

SYNTAX REFERENCE:
    print(*objects, sep=' ', end='\\n', file=sys.stdout, flush=False)
    f"{value:.2f}"             # Floating point rounding to 2 decimals
    f"{value:>10}"             # Right align within 10 spaces
    f"{value:<10}"             # Left align within 10 spaces
    f"{value:^10}"             # Center align within 10 spaces
    f"{value:,}"              # Comma thousand separator

KEY TAKEAWAYS / PITFALLS:
- Forgetting the leading `f` before an f-string results in `{variable}` printed literally.
- Setting `flush=True` forces immediate output buffer flushing (useful in progress bars or loops).
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

# Example 1: Basic print with sep and end parameters
name = "Bishal"
age = 36
role = "Software Engineer"

print("1. Standard print:")
print(name, age, role)  # Default: space separated, newline at end

print("\n2. Custom separator (sep):")
print(name, age, role, sep=" | ")
print("2026", "10", "13", sep="-")  # Date formatting

print("\n3. Custom line termination (end):")
print("Loading", end="...")
print("Complete!")  # Continues on the same line

# Example 2: Modern f-string Formatting (Precision, Padding, Alignment)
pi = 3.1415926535
large_number = 12500000

print(f"\nPi rounded to 2 decimals: {pi:.2f}")
print(f"Pi rounded to 4 decimals: {pi:.4f}")
print(f"Formatted currency: ${large_number:,.2f}")

# Example 3: String Alignment & Padding
headers = ["Name", "Score", "Rank"]
print(f"\n{headers[0]:<12} {headers[1]:^10} {headers[2]:>8}")
print("-" * 32)
print(f"{'Alice':<12} {98.5:^10.1f} {1:>8}")
print(f"{'Bob':<12} {87.0:^10.1f} {5:>8}")

# Example 4: Inline Expressions and Debugging with f"{var=}" (Python 3.8+)
radius = 7
print(f"\nCircle area calculation: radius={radius}, area={3.1416 * radius**2}")
# Debugging shorthand:
print(f"Debug inspect: {radius=}, {name=}")  # Outputs 'radius=7, name='Bishal''
