"""
================================================================================
TOPIC: Single Inheritance in Python
================================================================================
SHORT THEORY:
- Inheritance is an OOP mechanism where a new class (derived/child class) inherits 
  attributes and behaviors from an existing class (base/parent class).
- Enables code reuse, polymorphism, and models "is-a" relationships (e.g., Dog is an Animal).
- In Single Inheritance, a child class inherits from exactly ONE parent class.
- The child class automatically inherits parent methods unless it chooses to override them.

SYNTAX REFERENCE:
    class Parent:
        def parent_method(self): ...

    class Child(Parent):
        def child_method(self): ...

    isinstance(obj, Parent)    # Checks object type hierarchy
    issubclass(Child, Parent)  # Checks class inheritance relationship

KEY TAKEAWAYS / PITFALLS:
- All Python classes implicitly inherit from the built-in root `object` class.
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

class Vehicle:
    """Base class for all vehicles."""
    def __init__(self, brand: str, year: int) -> None:
        self.brand = brand
        self.year = year

    def start_engine(self) -> str:
        return f"The {self.brand} engine is running smoothly."

    def description(self) -> str:
        return f"{self.year} {self.brand}"


class Car(Vehicle):
    """Child class inheriting from Vehicle."""
    def __init__(self, brand: str, year: int, doors: int = 4) -> None:
        super().__init__(brand, year)  # Delegate common initialization to parent
        self.doors = doors

    def honk(self) -> str:
        return f"{self.brand} honks: Beep beep!"


# Testing single inheritance
my_car = Car("Honda", 2024, doors=4)

# Calling inherited methods
print("Description:", my_car.description())
print("Engine:     ", my_car.start_engine())

# Calling child-specific methods
print("Action:     ", my_car.honk())

# Verifying inheritance relationships
print(f"isinstance(my_car, Car):     {isinstance(my_car, Car)}")      # True
print(f"isinstance(my_car, Vehicle): {isinstance(my_car, Vehicle)}")  # True
print(f"issubclass(Car, Vehicle):     {issubclass(Car, Vehicle)}")      # True
