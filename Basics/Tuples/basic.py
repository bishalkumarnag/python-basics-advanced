"""
================================================================================
TOPIC: Tuples in Python (Immutability, Creation, Methods, Operations)
================================================================================
SHORT THEORY:
- A tuple is an ordered, immutable collection of elements.
- Once created, elements of a tuple cannot be added, removed, or changed.
- Why use tuples instead of lists?
  1. Performance: Tuples are stored in a single memory block; faster to allocate and iterate.
  2. Safety: Write-protection prevents accidental mutation of constants/records.
  3. Hashability: Tuples can be used as dictionary keys and set elements (if all contained items are hashable).
- Single element syntax: A trailing comma is REQUIRED: `t = (42,)` or `42,`. 
  Writing `(42)` evaluates to a plain integer!

SYNTAX REFERENCE:
    t = (1, 2, 3)
    t_single = (42,)         # Trailing comma required
    t_empty = ()
    t.count(val)             # Count occurrences of val
    t.index(val)             # Find index of first occurrence of val

KEY TAKEAWAYS / PITFALLS:
- Immutability is shallow: if a tuple contains a mutable object (like a list `(1, [2, 3])`),
  the list INSIDE the tuple CAN still be mutated!
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

# Example 1: Creation and Single-element Quirk
single_int = (42)       # int, not a tuple!
single_tuple = (42,)    # tuple

print(f"type((42)):   {type(single_int)}")    # <class 'int'>
print(f"type((42,)):  {type(single_tuple)}")  # <class 'tuple'>

# Example 2: Access, Slicing, and Indexing
person = ("Bishal", 30, "Engineer", "India")
print(f"\nPerson: {person}")
print(f"Name (index 0): {person[0]}")
print(f"Last item (index -1): {person[-1]}")
print(f"Slice (0:2): {person[0:2]}")

# Attempting mutation raises TypeError
# person[1] = 31 -> TypeError: 'tuple' object does not support item assignment

# Example 3: Tuple Methods (count & index)
digits = (1, 2, 3, 2, 4, 2, 5)
print(f"\nOccurrences of 2: {digits.count(2)}")  # 3
print(f"First index of 4: {digits.index(4)}")    # 4

# Example 4: Shallow Immutability Caveat (Mutable items inside tuple)
composite_tuple = (10, [20, 30], "constant")
print(f"\nInitial composite tuple: {composite_tuple}")

# Mutating the list inside the tuple
composite_tuple[1].append(40)
print(f"After mutating nested list: {composite_tuple}")  # (10, [20, 30, 40], 'constant')

# Example 5: Tuples as Dictionary Keys
# Coordinates as dictionary keys (impossible with lists!)
locations = {
    (12.9716, 77.5946): "Bengaluru",
    (28.7041, 77.1025): "Delhi",
    (19.0760, 72.8777): "Mumbai"
}
bengaluru_coords = (12.9716, 77.5946)
print(f"City at {bengaluru_coords}: {locations[bengaluru_coords]}")
