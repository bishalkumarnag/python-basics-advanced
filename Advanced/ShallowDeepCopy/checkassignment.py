"""
================================================================================
TOPIC: Reference Assignment vs Copying (The = Operator in Python)
================================================================================
SHORT THEORY:
- In Python, simple assignment (`b = a`) NEVER creates a copy of an object!
- It simply binds the new variable name `b` to the EXACT SAME object that `a` references in memory.
- Both `a` and `b` share the same memory address (`id(a) == id(b)`).
- Mutating the object through `b` will immediately reflect through `a`.
- Identity check: `a is b` returns `True`.

SYNTAX REFERENCE:
    b = a              # Reference assignment (aliases the same object)
    a is b             # True: checks identity (id(a) == id(b))
    a == b             # True: checks equality of values

KEY TAKEAWAYS / PITFALLS:
- Beginners often think `b = a` copies a list. It does not. It merely creates an alias!
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

# Example 1: Aliasing via Simple Assignment
original_list = [1, 2, 3]
alias_list = original_list  # Aliases the exact same list

print(f"original_list ID: {id(original_list)}")
print(f"alias_list ID:    {id(alias_list)}")
print(f"Are they identical objects (is)? {alias_list is original_list}")  # True

# Mutating via alias
alias_list.append(100)
print(f"\nAfter mutating alias_list.append(100):")
print(f"alias_list:    {alias_list}")     # [1, 2, 3, 100]
print(f"original_list: {original_list}")  # [1, 2, 3, 100] (Also mutated!)


# Example 2: Identity (is) vs Value Equality (==)
list_x = [4, 5, 6]
list_y = [4, 5, 6]

print(f"\nComparing two independently created lists with identical content:")
print(f"list_x ID: {id(list_x)} | list_y ID: {id(list_y)}")
print(f"list_x == list_y (Value match):    {list_x == list_y}")  # True
print(f"list_x is list_y (Same identity?): {list_x is list_y}")  # False