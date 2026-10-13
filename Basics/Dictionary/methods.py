"""
================================================================================
TOPIC: Dictionary Methods & Iteration Patterns
================================================================================
SHORT THEORY:
- Dictionaries provide dynamic view objects (`dict_keys`, `dict_values`, `dict_items`).
  These views reflect changes made to the dictionary in real-time.
- `items()` yields `(key, value)` tuples, ideal for unpacking inside `for` loops.
- `setdefault(key, default)` returns the value if `key` is present; if not, inserts 
  `key` with `default` and returns `default`.
- Merging dictionaries:
  - `.update(other_dict)`: In-place update
  - Python 3.9+ Merge Operator `|`: `merged = d1 | d2` (creates new dict)
  - Python 3.9+ Update Operator `|=`: `d1 |= d2` (in-place)

SYNTAX REFERENCE:
    d.keys()                  # View of all keys
    d.values()                # View of all values
    d.items()                 # View of (key, value) pairs
    d.setdefault(key, default)# Get value or insert default
    d.update(other_dict)      # In-place merge
    d1 | d2                   # Python 3.9+ union merge

KEY TAKEAWAYS / PITFALLS:
- Modifying a dictionary's keys while iterating directly over it raises `RuntimeError: dictionary changed size during iteration`. 
  To mutate while iterating, iterate over a copy of the keys: `for k in list(d.keys()):`.
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

# Example 1: Iterating over Keys, Values, and Items
inventory = {"apple": 50, "orange": 35, "banana": 120}

print("1. Iterating over keys directly:")
for fruit in inventory:  # default iteration is over keys
    print(f"  Fruit: {fruit}")

print("\n2. Iterating over values:")
for qty in inventory.values():
    print(f"  Quantity: {qty}")
print(f"  Total stock sum: {sum(inventory.values())}")

print("\n3. Iterating over items (Key-Value pairs):")
for fruit, qty in inventory.items():
    print(f"  {fruit:<8}: {qty} in stock")

# Example 2: setdefault() for Grouping
students_by_grade = {}
raw_data = [("A", "Alice"), ("B", "Bob"), ("A", "Charlie"), ("B", "Diana")]

for grade, student in raw_data:
    # If grade not present, initialize with empty list, then append
    students_by_grade.setdefault(grade, []).append(student)

print(f"\nGrouped students: {students_by_grade}")

# Example 3: Modern Dictionary Merging (Python 3.9+ | Operator)
defaults = {"theme": "light", "font_size": 14, "auto_save": True}
user_preferences = {"theme": "dark", "font_size": 16}

# | returns a brand new merged dictionary; right operand overwrites left
final_config = defaults | user_preferences
print(f"\nMerged configuration: {final_config}")

# Example 4: Min, Max, and Aggregate Statistics
exam_scores = {"Math": 95, "Physics": 78, "Chemistry": 88, "English": 92}
print(f"\nSubject with highest mark: {max(exam_scores, key=exam_scores.get)} ({max(exam_scores.values())})")
print(f"Subject with lowest mark:  {min(exam_scores, key=exam_scores.get)} ({min(exam_scores.values())})")
