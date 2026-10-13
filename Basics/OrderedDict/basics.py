"""
================================================================================
TOPIC: collections.OrderedDict vs Standard Python Dict
================================================================================
SHORT THEORY:
- In Python 3.7+, standard dictionaries (`dict`) are guaranteed to maintain 
  insertion order as an official language specification.
- However, `collections.OrderedDict` provides specialized capabilities that standard dicts do not:
  1. `move_to_end(key, last=True)`: Reorders a key to the very end or front in O(1) time.
  2. `popitem(last=True)`: Can pop from either the end (`last=True`, LIFO) or front (`last=False`, FIFO) in O(1).
  3. Order-sensitive equality: Two `OrderedDict` instances are only equal if keys are in the SAME order.
  4. Ideal foundation for building LRU (Least Recently Used) and MRU caches.

SYNTAX REFERENCE:
    from collections import OrderedDict
    od = OrderedDict()
    od.move_to_end('key', last=True)   # Move key to back (most recent)
    od.move_to_end('key', last=False)  # Move key to front (least recent)
    k, v = od.popitem(last=False)      # Pop oldest element (front)
    k, v = od.popitem(last=True)       # Pop newest element (back)

KEY TAKEAWAYS / PITFALLS:
- Standard `dict` equality checks ignore key order (`{'a': 1, 'b': 2} == {'b': 2, 'a': 1}` is True).
- `OrderedDict` equality checks REQUIRE matching key order.
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

from collections import OrderedDict

# Example 1: Creation and Order Preservation
od = OrderedDict([("a", 1), ("b", 2), ("c", 3), ("d", 4)])
print(f"Initial OrderedDict: {list(od.keys())}")  # ['a', 'b', 'c', 'd']

# Example 2: Reordering Keys in O(1) Time with move_to_end()
# Move 'b' to the back
od.move_to_end("b", last=True)
print(f"After move_to_end('b', last=True):  {list(od.keys())}")  # ['a', 'c', 'd', 'b']

# Move 'd' to the front
od.move_to_end("d", last=False)
print(f"After move_to_end('d', last=False): {list(od.keys())}")  # ['d', 'a', 'c', 'b']

# Example 3: FIFO and LIFO Popping with popitem()
# Pop front (oldest item in sequence)
front_key, front_val = od.popitem(last=False)
print(f"\nPopped front item: ({front_key}: {front_val}), Remaining: {list(od.keys())}")

# Pop back (newest item in sequence)
back_key, back_val = od.popitem(last=True)
print(f"Popped back item:  ({back_key}: {back_val}), Remaining: {list(od.keys())}")

# Example 4: Order-Sensitive Equality Comparison
standard_d1 = {"x": 10, "y": 20}
standard_d2 = {"y": 20, "x": 10}
print(f"\nStandard dict equality (order ignored): {standard_d1 == standard_d2}")  # True

ord_d1 = OrderedDict([("x", 10), ("y", 20)])
ord_d2 = OrderedDict([("y", 20), ("x", 10)])
print(f"OrderedDict equality (order enforced):  {ord_d1 == ord_d2}")  # False
