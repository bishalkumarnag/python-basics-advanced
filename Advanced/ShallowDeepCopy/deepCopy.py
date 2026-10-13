"""
================================================================================
TOPIC: Deep Copying in Python (copy.deepcopy)
================================================================================
SHORT THEORY:
- A deep copy constructs a new compound object and then, RECURSIVELY, inserts 
  copies into it of the objects found in the original.
- Completely decouples the copy from the original:
  - Both outer and ALL inner/nested mutable objects are cloned into independent memory addresses.
  - Modifying nested objects in the deep copy will NEVER affect the original.
- Handled via `copy.deepcopy(obj)`.
- Handles circular references safely (memorizes already-copied objects).

SYNTAX REFERENCE:
    import copy
    cloned_obj = copy.deepcopy(original_obj)

KEY TAKEAWAYS / PITFALLS:
- `deepcopy` is computationally slower and consumes more memory than shallow copy 
  due to recursive cloning. Use it only when nested mutability isolation is required.
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

import copy

# Example 1: Deep Copying Complex Nested Structure
original_profile = {
    "user_id": 101,
    "preferences": {
        "theme": "dark",
        "notifications": ["email", "sms"]
    },
    "tags": ["developer", "python"]
}

# Creating an independent deep copy
deep_cloned_profile = copy.deepcopy(original_profile)

# Mutating deep nested elements
deep_cloned_profile["preferences"]["theme"] = "light"
deep_cloned_profile["preferences"]["notifications"].append("push")
deep_cloned_profile["tags"].append("cloud")

print("--- Original Profile (Completely Untouched) ---")
print(f"Theme:         {original_profile['preferences']['theme']}")
print(f"Notifications: {original_profile['preferences']['notifications']}")
print(f"Tags:          {original_profile['tags']}")

print("\n--- Deep Cloned Profile (Modified Independently) ---")
print(f"Theme:         {deep_cloned_profile['preferences']['theme']}")
print(f"Notifications: {deep_cloned_profile['preferences']['notifications']}")
print(f"Tags:          {deep_cloned_profile['tags']}")


# Example 2: Verifying Memory Independence
orig_nested = [[1, 2], [3, 4]]
deep_nested = copy.deepcopy(orig_nested)

print(f"\nOuter ID match? {orig_nested is deep_nested}")         # False
print(f"Inner [0] ID match? {orig_nested[0] is deep_nested[0]}") # False (Independent objects!)