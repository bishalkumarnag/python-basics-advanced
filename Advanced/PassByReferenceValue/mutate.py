"""
================================================================================
TOPIC: In-Place Mutation of Mutable Objects
================================================================================
SHORT THEORY:
- In-place mutation refers to modifying the internal contents/state of an existing 
  object without creating a new object at a new memory address.
- Methods that mutate in-place in Python:
  - Lists: `append()`, `extend()`, `insert()`, `pop()`, `remove()`, `sort()`, `reverse()`, `lst[i] = x`, `lst[slice] = [...]`
  - Dictionaries: `d[key] = val`, `update()`, `pop()`, `popitem()`, `clear()`
  - Sets: `add()`, `update()`, `remove()`, `discard()`, `pop()`
- Mutating in-place preserves the memory ID (`id(obj)` remains identical).

SYNTAX REFERENCE:
    lst[index] = new_val     # Index mutation
    lst.append(new_val)      # Method mutation
    d[key] = new_val         # Key mutation

KEY TAKEAWAYS / PITFALLS:
- Mutating methods on lists (`sort()`, `reverse()`) return `None` by design in Python 
  to remind the developer that the mutation happened in-place.
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

# Example 1: In-Place Mutation via Index Assignment
def mutate_elements(arr: list[int]) -> None:
    arr[1] = 999  # Replaces element at index 1 directly in existing array

nums = [10, 20, 30]
print(f"Nums before mutate: {nums}, id={id(nums)}")
mutate_elements(nums)
print(f"Nums after mutate:  {nums}, id={id(nums)}")  # [10, 999, 30], same id!


# Example 2: In-Place Mutation via Methods
def enrich_catalog(catalog: dict) -> None:
    catalog["version"] = 2.0
    catalog["tags"].append("verified")

product = {
    "title": "Ergonomic Chair",
    "tags": ["furniture", "office"]
}

print(f"\nProduct before enrich: {product}")
enrich_catalog(product)
print(f"Product after enrich:  {product}")