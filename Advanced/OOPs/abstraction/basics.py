"""
================================================================================
TOPIC: Abstraction & Abstract Base Classes (abc Module)
================================================================================
SHORT THEORY:
- Abstraction hides internal implementation complexities and exposes only 
  the essential interface to users.
- In Python, abstraction is enforced using the `abc` (Abstract Base Class) module:
  1. Inherit from `abc.ABC`.
  2. Decorate mandatory interface methods with `@abstractmethod`.
- An abstract class CANNOT be instantiated directly.
- Subclasses MUST implement ALL abstract methods. If any abstract method is 
  left unimplemented, instantiating the subclass raises a `TypeError`.

SYNTAX REFERENCE:
    from abc import ABC, abstractmethod

    class InterfaceName(ABC):
        @abstractmethod
        def required_method(self, arg):
            pass

KEY TAKEAWAYS / PITFALLS:
- Forgetting to inherit from `ABC` prevents Python from enforcing the abstract contract,
  allowing premature instantiation without error!
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """Abstract Base Class defining the contract for all shapes."""
    def __init__(self, color: str) -> None:
        self.color = color

    @abstractmethod
    def area(self) -> float:
        """Calculate shape surface area."""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """Calculate shape boundary perimeter."""
        pass

    def display(self) -> None:
        """Concrete method shared across all concrete shapes."""
        print(f"[{self.color} {self.__class__.__name__}] Area: {self.area():.2f}, Perimeter: {self.perimeter():.2f}")


# Concrete Subclass 1: Rectangle
class Rectangle(Shape):
    def __init__(self, color: str, length: float, width: float) -> None:
        super().__init__(color)
        self.length = length
        self.width = width

    def area(self) -> float:
        return self.length * self.width

    def perimeter(self) -> float:
        return 2 * (self.length + self.width)


# Concrete Subclass 2: Circle
class Circle(Shape):
    def __init__(self, color: str, radius: float) -> None:
        super().__init__(color)
        self.radius = radius

    def area(self) -> float:
        return math.pi * (self.radius ** 2)

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius


# 1. Verification of Subclasses
rect = Rectangle("Blue", 10.0, 5.0)
circ = Circle("Emerald", 7.0)

rect.display()
circ.display()

# 2. Verification of Contract Enforcement:
print("\nVerifying ABC Enforcement:")
try:
    # Attempting to instantiate the Abstract Base Class directly
    shape = Shape("Red")
except TypeError as err:
    print(f"Correctly caught instantiation error on Shape: {err}")


# Class missing required implementation
class IncompleteShape(Shape):
    def area(self) -> float:
        return 1.0
    # missing perimeter()!

try:
    bad_obj = IncompleteShape("Yellow")
except TypeError as err:
    print(f"Correctly caught missing method on IncompleteShape: {err}")
