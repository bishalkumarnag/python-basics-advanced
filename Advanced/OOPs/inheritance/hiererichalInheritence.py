"""
================================================================================
TOPIC: Hierarchical Inheritance in Python
================================================================================
SHORT THEORY:
- In Hierarchical Inheritance, multiple child classes inherit from a SINGLE shared base class.
- Structure:
             Parent
            /      \\
        Child1    Child2
- Promotes code sharing: shared common logic lives in the single parent class, 
  while child classes specialize behaviors independently.

SYNTAX REFERENCE:
    class Parent: ...
    class Child1(Parent): ...
    class Child2(Parent): ...

KEY TAKEAWAYS / PITFALLS:
- Child classes are siblings; they do not inherit from each other.
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

class Shape:
    """Shared parent class for all shapes."""
    def __init__(self, color: str) -> None:
        self.color = color

    def describe(self) -> str:
        return f"This is a {self.color} geometric shape."


class Circle(Shape):
    def __init__(self, color: str, radius: float) -> None:
        super().__init__(color)
        self.radius = radius

    def area(self) -> float:
        import math
        return round(math.pi * self.radius ** 2, 2)


class Rectangle(Shape):
    def __init__(self, color: str, width: float, height: float) -> None:
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self) -> float:
        return round(self.width * self.height, 2)


c = Circle("Crimson", 5.0)
r = Rectangle("Sapphire", 4.0, 6.0)

print(f"Circle:    color={c.color}, area={c.area()} | {c.describe()}")
print(f"Rectangle: color={r.color}, area={r.area()} | {r.describe()}")