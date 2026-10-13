"""
================================================================================
TOPIC: Set Operations (Union, Intersection, Difference, Symmetric Difference)
================================================================================
SHORT THEORY:
- Python sets implement mathematical set operations both as methods and infix operators:
  1. Union (`|` or `.union()`): Elements present in EITHER set.
  2. Intersection (`&` or `.intersection()`): Elements present in BOTH sets.
  3. Difference (`-` or `.difference()`): Elements in set A but NOT in set B.
  4. Symmetric Difference (`^` or `.symmetric_difference()`): Elements in either set, but NOT both.
  5. Subset (`<=` or `.issubset()`): Checks if all elements of A are in B.
  6. Superset (`>=` or `.issuperset()`): Checks if A contains all elements of B.
  7. Disjoint (`.isdisjoint()`): Checks if two sets share NO common elements.

SYNTAX REFERENCE:
    a | b       # Union
    a & b       # Intersection
    a - b       # Difference (A minus B)
    a ^ b       # Symmetric Difference
    a <= b      # Is subset?
    a.isdisjoint(b)

KEY TAKEAWAYS / PITFALLS:
- Operators (`|`, `&`, `-`, `^`) require both operands to be sets. 
  Methods (`.union()`, `.intersection()`, etc.) accept ANY iterable as arguments!
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

frontend_devs = {"Alice", "Bob", "Charlie", "David"}
backend_devs = {"Charlie", "David", "Emma", "Frank"}

print(f"Frontend Devs: {frontend_devs}")
print(f"Backend Devs:  {backend_devs}")

# Example 1: Union (All unique developers in engineering)
all_devs = frontend_devs | backend_devs
print(f"\n1. Union (|): All developers ({len(all_devs)}):")
print(f"   {all_devs}")

# Example 2: Intersection (Fullstack developers who do both)
fullstack_devs = frontend_devs & backend_devs
print(f"\n2. Intersection (&): Fullstack developers:")
print(f"   {fullstack_devs}")

# Example 3: Difference (Only frontend developers, not backend)
pure_frontend = frontend_devs - backend_devs
print(f"\n3. Difference (-): Pure Frontend developers:")
print(f"   {pure_frontend}")

# Example 4: Symmetric Difference (Specialists in only one domain, not both)
specialists = frontend_devs ^ backend_devs
print(f"\n4. Symmetric Difference (^): Non-fullstack specialists:")
print(f"   {specialists}")

# Example 5: Subsets and Disjoint Sets
team_lead = {"Alice"}
mobile_devs = {"George", "Hannah"}

print(f"\nIs team_lead a subset of frontend? {team_lead <= frontend_devs}") # True
print(f"Are frontend and mobile disjoint?   {frontend_devs.isdisjoint(mobile_devs)}") # True
