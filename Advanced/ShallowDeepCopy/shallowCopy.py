"""
================================================================================
TOPIC: Shallow Copying in Python (copy.copy, .copy(), slicing [:])
================================================================================
SHORT THEORY:
- A shallow copy constructs a new compound object and then inserts references into 
  it to the objects found in the original.
- Ways to create a shallow copy:
  1. `copy.copy(obj)`
  2. `list.copy()` or `dict.copy()`
  3. Slicing: `lst[:]`
  4. Type constructors: `list(original)`, `dict(original)`
- The Shallow Copy Caveat:
  - Top-level changes in the copy DO NOT affect the original.
  - BUT nested mutable objects (e.g., lists inside lists) are NOT cloned!
    The copy merely references the same nested inner objects. Mutating an inner 
    nested object WILL affect both the original and the copy!

SYNTAX REFERENCE:
    import copy
    shallow_1 = copy.copy(original)
    shallow_2 = original.copy()
    shallow_3 = original[:]

KEY TAKEAWAYS / PITFALLS:
- Shallow copies only protect top-level elements. If your data structure has 
  nested lists or nested dicts, shallow copying is NOT enough!
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

import copy

# Example 1: Shallow Copying Flat Structures (Safe)
flat_original = [1, 2, 3]
flat_copy = flat_original.copy()

flat_copy.append(100)
print("1. Flat List Shallow Copy:")
print(f"   original: {flat_original}")  # [1, 2, 3] (Protected!)
print(f"   copy:     {flat_copy}")      # [1, 2, 3, 100]
print(f"   Different IDs? {id(flat_original) != id(flat_copy)}")  # True


# Example 2: The Shallow Copy Nested Mutation Caveat
nested_original = ["apple", ["sub_item_1", "sub_item_2"], "banana"]
nested_shallow = copy.copy(nested_original)

print("\n2. Nested List Shallow Copy:")
print(f"   Outer list IDs are different: id(orig)={id(nested_original)} vs id(copy)={id(nested_shallow)}")
print(f"   Inner list IDs are IDENTICAL: id={id(nested_original[1])} vs id={id(nested_shallow[1])}")

# Mutating the nested inner list
nested_shallow[1].append("INTRUDER")

print(f"\nAfter mutating nested_shallow[1].append('INTRUDER'):")
print(f"   nested_shallow:  {nested_shallow}")
print(f"   nested_original: {nested_original}")
# Notice: 'INTRUDER' appears in nested_original because the inner list was shared!
