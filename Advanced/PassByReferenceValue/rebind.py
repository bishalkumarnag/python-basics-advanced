"""
================================================================================
TOPIC: Rebinding vs Mutating in Python Functions
================================================================================
SHORT THEORY:
- Rebinding occurs when an assignment statement (`var = new_value`) binds a variable 
  name to a completely different object in memory.
- Inside a function, assigning `param = ...` creates a local binding.
- It severs the local variable's connection to the caller's outside object!
- Consequently, the caller's outside object will NOT change, even if the object is mutable.
- Crucial Distinction:
  - `lst.append(5)` -> MUTATION: Modifies the referenced object. Affects caller.
  - `lst = [1, 2, 3]` -> REBINDING: Points local name to a new list. Does NOT affect caller.
  - `lst += [4, 5]` on lists -> MUTATION (calls `__iadd__`, mutating in-place!).
  - `lst = lst + [4, 5]` -> REBINDING (creates new list and rebinds!).

SYNTAX REFERENCE:
    def rebind(x):
        x = [4, 5, 6]        # Rebinding: does NOT affect caller

    def in_place(x):
        x[:] = [4, 5, 6]     # Slice assignment: MUTATES in-place, affects caller!

KEY TAKEAWAYS / PITFALLS:
- `x += [1]` vs `x = x + [1]`: On lists, `+=` mutates in-place (like `extend`), 
  while `x = x + ...` creates a new list and rebinds.
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

# Example 1: Rebinding a Mutable List Inside Function
def rebind_list(target: list) -> None:
    print(f"Inside rebind (before): target={target}, id={id(target)}")
    target = [999, 888, 777]  # Rebinding local variable to brand new list!
    print(f"Inside rebind (after):  target={target}, id={id(target)}")

original_list = [10, 20, 30]
print(f"Outside (initial): original={original_list}, id={id(original_list)}")
rebind_list(original_list)
print(f"Outside (after call): original={original_list}, id={id(original_list)}")
# Notice: Outside list remained [10, 20, 30] untouched!


# Example 2: Rebinding vs Slice Assignment
def slice_replace(target: list) -> None:
    # Slice assignment mutates the existing object in-place without rebinding!
    target[:] = [999, 888, 777]

slice_test = [10, 20, 30]
print(f"\nBefore slice assignment: {slice_test}")
slice_replace(slice_test)
print(f"After slice assignment:  {slice_test}")  # [999, 888, 777] affected caller!


# Example 3: += vs + on Mutable Lists
list_a = [1, 2]
list_b = list_a
list_a += [3]  # in-place mutation (__iadd__)
print(f"\nAfter list_a += [3]: list_a={list_a}, list_b={list_b}")  # Both are [1, 2, 3]

list_c = [1, 2]
list_d = list_c
list_c = list_c + [3]  # creates new list and rebinds list_c
print(f"After list_c = list_c + [3]: list_c={list_c}, list_d={list_d}") # list_d is still [1, 2]!