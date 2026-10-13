"""
================================================================================
TOPIC: Pass by Object Reference: Mutable Objects ("Pass by Reference" Illusion)
================================================================================
SHORT THEORY:
- When a mutable object (e.g., `list`, `dict`, `set`, custom class instances) is passed 
  to a function:
  1. The parameter variable receives a copy of the reference pointing to the SAME object.
  2. If the function performs IN-PLACE mutations on that object (such as `.append()`, 
     `[index] = val`, `.update()`, `.pop()`), the modification directly impacts 
     the original object in memory.
  3. Consequently, the caller's outside object reflects those changes immediately.
- This creates the appearance of "Pass by Reference".

SYNTAX REFERENCE:
    def mutate_list(lst: list):
        lst.append(999)      # In-place mutation -> Affects caller

KEY TAKEAWAYS / PITFALLS:
- If you don't want a function to mutate your original mutable object, pass an explicit 
  copy to the function: `func(my_list.copy())` or `func(my_list[:])`.
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

# Example 1: In-Place Mutation of a List
def append_element(target_list: list) -> None:
    print(f"Inside (before mutation): id={id(target_list)}")
    target_list.append("NEW_ITEM")
    print(f"Inside (after mutation):  id={id(target_list)}")


shared_list = [1, 2, 3]
print(f"Outside (initial): {shared_list}, id={id(shared_list)}")

append_element(shared_list)

print(f"Outside (after call): {shared_list}, id={id(shared_list)}")
# Notice: Outside list was mutated in-place and ID never changed!


# Example 2: In-Place Mutation of Dictionaries and Sets
def update_registry(config: dict, allowed_users: set) -> None:
    config["status"] = "ACTIVE"
    allowed_users.add("admin_user")

app_config = {"environment": "production"}
user_set = {"guest"}

update_registry(app_config, user_set)

print(f"\nMutated config: {app_config}")
print(f"Mutated user set: {user_set}")


# Example 3: Protecting Against Unwanted Mutation via Defensive Copying
def safe_processor(data: list) -> None:
    # Work on a defensive local copy
    local_copy = data.copy()
    local_copy.append("PROCESSED")
    print(f"Inside safe processor: {local_copy}")

original_data = ["alpha", "beta"]
safe_processor(original_data)
print(f"Original data protected: {original_data}")  # ['alpha', 'beta']
