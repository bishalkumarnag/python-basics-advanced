"""
================================================================================
TOPIC: Sorting Dictionaries (By Key, By Value)
================================================================================
SHORT THEORY:
- Dictionaries themselves cannot be sorted in-place, but you can sort their views
  using Python's built-in `sorted()` function.
- `sorted(d.items(), key=...)` returns a list of `(key, value)` tuples sorted according 
  to the criteria defined in the `key` function (typically a lambda).
- The resulting list of tuples can be converted back into a sorted dictionary using `dict()`.

SYNTAX REFERENCE:
    # Sort by Key:
    sorted_by_key = dict(sorted(d.items(), key=lambda item: item[0]))

    # Sort by Value (Ascending):
    sorted_by_val = dict(sorted(d.items(), key=lambda item: item[1]))

    # Sort by Value (Descending):
    sorted_by_val_desc = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

KEY TAKEAWAYS / PITFALLS:
- In Python 3.7+, dictionaries preserve insertion order. Converting a sorted list of 
  tuples back to `dict()` preserves the sorted order!
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

subject_scores = {
    "Mathematics": 85,
    "Science": 92,
    "English": 88,
    "History": 74,
    "Computer": 99
}

print(f"Original dictionary: {subject_scores}")

# Example 1: Sort by Keys Alphabetically
by_key = dict(sorted(subject_scores.items(), key=lambda pair: pair[0]))
print(f"\n1. Sorted by Key (Subject): {by_key}")

# Example 2: Sort by Values (Marks Ascending)
by_val_asc = dict(sorted(subject_scores.items(), key=lambda pair: pair[1]))
print(f"2. Sorted by Value (Ascending): {by_val_asc}")

# Example 3: Sort by Values (Marks Descending)
by_val_desc = dict(sorted(subject_scores.items(), key=lambda pair: pair[1], reverse=True))
print(f"3. Sorted by Value (Descending): {by_val_desc}")

# Example 4: Sorting by Multiple Criteria (Length of Key, then Value)
inventory = {"pen": 10, "notebook": 5, "eraser": 10, "ruler": 15}
by_custom = dict(sorted(inventory.items(), key=lambda item: (-item[1], item[0])))
print(f"\n4. Sorted by quantity desc, then key asc: {by_custom}")