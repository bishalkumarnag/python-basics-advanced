"""
================================================================================
TOPIC: The Diamond Problem & Method Resolution Order (MRO / C3 Linearization)
================================================================================
SHORT THEORY:
- The Diamond Problem occurs in multiple inheritance when a class derives from two 
  classes that share a common ancestor:
             A (Grandparent)
            / \\
           B   C (Parents)
            \\ /
             D (Child)
- Ambiguity: If A, B, and C all define `process()`, which one does `D.process()` execute?
- Solution: Python resolves this deterministically using the C3 Linearization algorithm.
- Rules of Python's MRO:
  1. Children precede parents.
  2. Order in class definition header is preserved (`class D(B, C)` checks B before C).
  3. Every class appears only once in the linearization.
- You can inspect the MRO at any time using `ClassName.__mro__` or `ClassName.mro()`.

SYNTAX REFERENCE:
    class D(B, C): ...
    print(D.__mro__)    # Tuple of classes in resolution order
    print(D.mro())      # List of classes in resolution order

KEY TAKEAWAYS / PITFALLS:
- Python will refuse to define a class with `TypeError: Cannot create a consistent method resolution order (MRO)`
  if your inheritance order violates monotonic linearization constraints.
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

# Structure:
#        GrandParent (A)
#           /       \
#      ParentB (B)  ParentC (C)
#           \       /
#            Child (D)

class GrandParent:
    def identify(self) -> str:
        return "Identity: GrandParent (A)"


class ParentB(GrandParent):
    def identify(self) -> str:
        return "Identity: ParentB (B)"


class ParentC(GrandParent):
    def identify(self) -> str:
        return "Identity: ParentC (C)"


class Child(ParentB, ParentC):
    """Child inherits from ParentB and ParentC in order."""
    pass


# Instantiate Child
c = Child()
# ParentB takes priority because it was listed first in `class Child(ParentB, ParentC)`:
print("c.identify() result:")
print(" ", c.identify())  # Identity: ParentB (B)

# Inspecting the exact Method Resolution Order (MRO):
print("\nExact Method Resolution Order (MRO) for Child:")
for step, cls in enumerate(Child.mro(), start=1):
    print(f"  Step {step}: {cls.__name__}")

# Expected sequence:
# Step 1: Child
# Step 2: ParentB
# Step 3: ParentC
# Step 4: GrandParent
# Step 5: object


# Example 2: Cooperative Super in Diamond Pattern
class Root:
    def execute(self):
        print("Root executed")

class Left(Root):
    def execute(self):
        print("Left start")
        super().execute()
        print("Left end")

class Right(Root):
    def execute(self):
        print("Right start")
        super().execute()
        print("Right end")

class Bottom(Left, Right):
    def execute(self):
        print("Bottom start")
        super().execute()
        print("Bottom end")

print("\nCooperative super execution order in Bottom:")
b = Bottom()
b.execute()
