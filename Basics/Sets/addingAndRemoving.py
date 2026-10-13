"""
================================================================================
TOPIC: Adding & Removing Elements in Sets (add, update, remove, discard, pop)
================================================================================
SHORT THEORY:
- Adding elements:
  - `s.add(elem)`: Adds a single hashable element.
  - `s.update(iterable)`: Adds multiple elements from an iterable (bulk add).
- Removing elements:
  - `s.remove(elem)`: Removes `elem`. If `elem` is absent, raises `KeyError`.
  - `s.discard(elem)`: Removes `elem` safely. If `elem` is absent, DOES NOTHING (no error).
  - `s.pop()`: Removes and returns an arbitrary element (raises `KeyError` if empty).
  - `s.clear()`: Empties the set completely.

SYNTAX REFERENCE:
    s.add("item")
    s.update(["item1", "item2"])
    s.remove("must_exist")        # Unsafe if item missing (KeyError)
    s.discard("may_exist")        # Safe (idempotent, no error)
    val = s.pop()
    s.clear()

KEY TAKEAWAYS / PITFALLS:
- Use `.discard()` over `.remove()` when you want idempotent deletion without try-except blocks.
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

skills = {"Python", "Git"}
print(f"Initial set: {skills}")

# Example 1: Adding Single Elements with .add()
skills.add("Docker")
skills.add("Python")  # Duplicate: no effect
print(f"After .add('Docker'): {skills}")

# Example 2: Bulk Adding with .update()
skills.update(["PostgreSQL", "Redis", "FastAPI"])
print(f"After .update(): {skills}")

# Example 3: .remove() vs .discard() (KeyError safety)
skills.remove("Git")
print(f"After .remove('Git'): {skills}")

# .remove('Kubernetes') -> would raise KeyError!
# .discard() is safe when element is absent:
skills.discard("Kubernetes")
print("Successfully discarded non-existent 'Kubernetes' without crashing!")

# Example 4: Arbitrary removal with .pop()
arbitrary_skill = skills.pop()
print(f"Popped arbitrary skill: {arbitrary_skill}")
print(f"Remaining skills: {skills}")

# Example 5: Clearing the set
skills.clear()
print(f"Cleared set: {skills}")  # set()
