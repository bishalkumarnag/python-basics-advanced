"""
================================================================================
TOPIC: Removing Elements from a Dictionary (pop, popitem, del, clear)
================================================================================
SHORT THEORY:
- Python provides multiple techniques for removing items from a dictionary:
  1. `d.pop(key[, default])`: Removes `key` and returns its value. If `key` is missing 
     and no default is specified, raises `KeyError`.
  2. `d.popitem()`: Removes and returns the last inserted `(key, value)` pair (LIFO order).
     Raises `KeyError` if dictionary is empty.
  3. `del d[key]`: Removes `key` via Python statement (raises `KeyError` if missing).
  4. `d.clear()`: Empties the entire dictionary in-place.

SYNTAX REFERENCE:
    val = d.pop("key", default_val)
    key, val = d.popitem()
    del d["key"]
    d.clear()

KEY TAKEAWAYS / PITFALLS:
- `del d[key]` will crash your program if `key` doesn't exist. Prefer `d.pop(key, None)` 
  for safe deletion without throwing an exception.
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

session = {
    "user_id": 1052,
    "ip_address": "192.168.1.1",
    "token": "xyz987abc",
    "active": True
}
print(f"Initial session: {session}")

# Example 1: Removing with pop() and fallback
token = session.pop("token")
print(f"Popped token: {token}")
print(f"Session after pop('token'): {session}")

# Safe pop on non-existent key
removed_val = session.pop("non_existent_key", "NOT_FOUND")
print(f"Safe pop fallback: {removed_val}")

# Example 2: LIFO removal with popitem()
last_k, last_v = session.popitem()
print(f"Popped last item: ({last_k}: {last_v})")
print(f"Session after popitem(): {session}")

# Example 3: del statement
del session["user_id"]
print(f"Session after del: {session}")

# Example 4: clear()
session.clear()
print(f"Session after clear(): {session}")  # {}
