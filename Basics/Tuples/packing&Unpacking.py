"""
================================================================================
TOPIC: Tuple Packing & Unpacking (Extended Star Unpacking)
================================================================================
SHORT THEORY:
- Tuple Packing: Placing multiple comma-separated values into a single variable.
- Tuple Unpacking: Extracting elements of a tuple directly into separate variables.
- Extended Iterable Unpacking (`*` operator): Introduced in PEP 3132 (Python 3.0+), 
  allows capturing the "rest" of the elements into a list.

SYNTAX REFERENCE:
    packed = 1, 2, 3                   # Tuple packing
    a, b, c = packed                   # Standard unpacking (counts must match)
    first, *middle, last = sequence    # Extended unpacking with *
    a, b = b, a                        # Pythonic variable swap

KEY TAKEAWAYS / PITFALLS:
- In standard unpacking `a, b = tuple_val`, if the number of variables does not 
  match the length of the tuple, Python raises `ValueError: too many values to unpack`
  or `not enough values to unpack`.
- In extended unpacking, you can only have ONE starred expression `*var` per assignment.
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

# Example 1: Basic Packing and Unpacking
packed_coords = 12.5, 45.8  # Packing without parentheses
lat, lon = packed_coords    # Unpacking
print(f"Latitude: {lat}, Longitude: {lon}")

# Example 2: Pythonic Variable Swap (Internally uses tuple packing/unpacking)
x, y = 100, 200
print(f"Before swap: x={x}, y={y}")
x, y = y, x  # (y, x) is packed then unpacked into (x, y)
print(f"After swap:  x={x}, y={y}")

# Example 3: Extended Star Unpacking (*rest)
numbers = [1, 2, 3, 4, 5, 6, 7]

first, *middle, last = numbers
print(f"\nFirst: {first}")        # 1
print(f"Middle: {middle}")      # [2, 3, 4, 5, 6] (collected into a list!)
print(f"Last: {last}")          # 7

head, *tail = numbers
print(f"Head: {head}, Tail: {tail}")

*prefix, end1, end2 = numbers
print(f"Prefix: {prefix}, Last two: {end1}, {end2}")

# Example 4: Unpacking in Loop Iteration
records = [
    ("Alice", 25, "Data Analyst"),
    ("Bob", 32, "DevOps Engineer"),
    ("Charlie", 28, "Product Manager")
]

print("\nIterating and unpacking records:")
for name, age, title in records:
    print(f"  {name} ({age}) - {title}")

# Example 5: Function Returning Multiple Values
def compute_stats(data_list: list[int]) -> tuple[int, int, float]:
    return min(data_list), max(data_list), round(sum(data_list) / len(data_list), 2)

lowest, highest, average = compute_stats([10, 20, 30, 40, 50])
print(f"\nStats -> Low: {lowest}, High: {highest}, Avg: {average}")
