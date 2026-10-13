"""
================================================================================
TOPIC: Dictionaries in Python (Key-Value Mappings, Hash Tables)
================================================================================
SHORT THEORY:
- A dictionary (`dict`) is an unordered (insertion-ordered since Python 3.7+), 
  mutable collection of key-value pairs.
- Keys MUST be immutable and hashable (e.g., `str`, `int`, `float`, `tuple`, `frozenset`).
  Mutable types like `list` or `dict` CANNOT be used as dictionary keys.
- Values can be of ANY data type, including duplicates and nested structures.
- Average time complexity for lookup, insertion, and deletion is O(1) due to hash tables.

SYNTAX REFERENCE:
    d = {"key": "value", 10: [1, 2, 3]}
    d = dict(key1="val1", key2="val2")
    d["key"]                       # Access by key (raises KeyError if key absent)
    d.get("key", default=None)     # Safe access (returns default if absent)
    len(d)                         # Number of key-value pairs

KEY TAKEAWAYS / PITFALLS:
- Using `d[missing_key]` raises a `KeyError`. Always prefer `d.get(missing_key, fallback)`
  when the key might not exist.
- Dictionary keys are unique; assigning to an existing key overwrites its previous value.
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

# Example 1: Valid and Invalid Keys
student = {
    "name": "Bishal",
    "roll_no": 101,
    (2026, "semester_1"): "Passed",  # Tuple is immutable -> Valid key!
    # [1, 2]: "Invalid"              # List is mutable -> Raises TypeError: unhashable type: 'list'
}

print(f"Student record: {student}")
print(f"Access via tuple key: {student[(2026, 'semester_1')]}")

# Example 2: Safe Lookup with .get() vs Direct Key Access []
marks = {"Math": 95, "Physics": 88, "Chemistry": 92}

print(f"\nMath mark (direct): {marks['Math']}")

# Direct access with missing key raises KeyError:
# print(marks["Biology"]) -> KeyError: 'Biology'

# Safe access with .get()
print(f"Biology mark (.get default None): {marks.get('Biology')}")
print(f"Biology mark (.get custom fallback): {marks.get('Biology', 0)}")

# Example 3: Modifying and Adding Elements
marks["English"] = 85      # Adding new key
marks["Math"] = 98         # Updating existing key
print(f"\nUpdated marks dictionary: {marks}")

# Example 4: Checking Existence using `in`
subject = "History"
if subject in marks:
    print(f"{subject}: {marks[subject]}")
else:
    print(f"'{subject}' is not enrolled in records.")