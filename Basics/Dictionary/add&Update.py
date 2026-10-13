"""
================================================================================
TOPIC: Adding & Updating Dictionary Elements
================================================================================
SHORT THEORY:
- Dictionaries are mutable; items can be added, updated, or merged dynamically.
- `d[key] = value`: If `key` exists, updates the value; otherwise adds the key-value pair.
- `.update({k: v, ...})` or `.update(k1=v1, k2=v2)`: Updates from another dict or key-value pairs.
- Modern Python 3.9+ syntax introduces the union operator `|` and in-place union `|=`.

SYNTAX REFERENCE:
    d[key] = new_value           # Assignment / insertion
    d.update(iterable/dict)      # Bulk update in-place
    d |= other_dict              # Python 3.9+ in-place merge

KEY TAKEAWAYS / PITFALLS:
- `.update()` modifies the caller dictionary in-place and returns `None`.
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

# Example 1: Direct Index Assignment
profile = {"username": "rahul99", "role": "Junior Analyst"}
print(f"Initial: {profile}")

# Update existing
profile["role"] = "Senior Analyst"

# Add new key
profile["department"] = "Data Science"
print(f"After direct updates: {profile}")

# Example 2: Bulk Update via .update()
extra_info = {"city": "Bengaluru", "remote": True, "department": "AI Engineering"}
profile.update(extra_info)
print(f"After .update(): {profile}")

# Example 3: In-Place Union Operator (|=)
metrics = {"cpu": 45.2, "ram": 68.0}
new_metric = {"disk": 82.5, "cpu": 48.0}
metrics |= new_metric
print(f"After |= update: {metrics}")
