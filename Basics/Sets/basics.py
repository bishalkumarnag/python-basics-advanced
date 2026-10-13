"""
================================================================================
TOPIC: Sets in Python (Uniqueness, Hashability, Creation)
================================================================================
SHORT THEORY:
- A set is an unordered collection of unique, immutable (hashable) elements.
- Sets automatically eliminate duplicate entries.
- Elements in a set cannot be accessed via indexing or slicing (`s[0]` fails with `TypeError`) 
  because sets do not maintain an ordered sequence.
- Empty set creation: To create an empty set, you MUST use `set()`. 
  Writing `{}` creates an empty dictionary (`dict`)!
- Membership testing (`x in set`) has an average time complexity of O(1), making sets 
  vastly faster than lists (O(N)) for lookup-heavy checks.

SYNTAX REFERENCE:
    s = {1, 2, 3}
    empty_s = set()             # Correct empty set syntax
    not_a_set = {}              # Empty DICTIONARY, not a set!
    set_from_list = set(my_list)# Deduplicates list
    len(s)                      # Count of unique elements

KEY TAKEAWAYS / PITFALLS:
- Set elements must be hashable. You cannot put a `list`, `dict`, or another `set` 
  inside a set (use `frozenset` if an immutable set is needed as an element).
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

# Example 1: Creation and Automatic Deduplication
numbers = {1, 2, 3, 2, 4, 1, 5, 3}
print(f"Set automatically removes duplicates: {numbers}")  # {1, 2, 3, 4, 5}

# Example 2: Empty Set vs Empty Dict
empty_dict = {}
empty_set = set()
print(f"type({{}}):     {type(empty_dict)}")  # <class 'dict'>
print(f"type(set()): {type(empty_set)}")   # <class 'set'>

# Example 3: Deduplicating a List while Maintaining Types
raw_ips = ["192.168.1.1", "10.0.0.1", "192.168.1.1", "172.16.0.1", "10.0.0.1"]
unique_ips = list(set(raw_ips))
print(f"\nOriginal IPs ({len(raw_ips)}): {raw_ips}")
print(f"Unique IPs ({len(unique_ips)}):   {unique_ips}")

# Example 4: O(1) Fast Membership Testing
active_user_ids = {101, 102, 105, 109, 115}
check_id = 105
if check_id in active_user_ids:
    print(f"\nUser ID {check_id} is active (tested in O(1) time)")

# Example 5: Hashability Restriction
valid_set = {1, "Python", (10, 20)}  # tuple is hashable -> valid
print(f"\nValid set with tuple: {valid_set}")

# Attempting to store a list in a set raises TypeError:
# invalid_set = {1, [2, 3]} -> TypeError: unhashable type: 'list'