"""
================================================================================
TOPIC: Membership Testing in Dictionaries (in, not in)
================================================================================
SHORT THEORY:
- The `in` and `not in` operators test for key membership in a dictionary in average O(1) time.
- By default, `key in d` checks whether the key is in `d.keys()`.
- To check whether a value exists in a dictionary, use `val in d.values()` (O(N) time complexity).

SYNTAX REFERENCE:
    "key" in d             # Checks keys: O(1)
    "key" not in d         # Checks key absence: O(1)
    "val" in d.values()    # Checks values: O(N)

KEY TAKEAWAYS / PITFALLS:
- Never do `if key in d.keys():`. Just write `if key in d:`. It is cleaner, faster, 
  and idiomatic Python.
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

catalog = {
    "SKU-001": "Mechanical Keyboard",
    "SKU-002": "Wireless Mouse",
    "SKU-003": "USB-C Hub"
}

# Example 1: Key Membership (O(1))
query_sku = "SKU-002"
if query_sku in catalog:
    print(f"Product found for {query_sku}: {catalog[query_sku]}")
else:
    print(f"Product {query_sku} is out of catalog.")

# Example 2: Negative Key Membership
missing_sku = "SKU-999"
if missing_sku not in catalog:
    print(f"Verified: {missing_sku} does not exist in inventory.")

# Example 3: Value Membership (O(N))
target_item = "Wireless Mouse"
if target_item in catalog.values():
    print(f"'{target_item}' is offered in our product range!")
