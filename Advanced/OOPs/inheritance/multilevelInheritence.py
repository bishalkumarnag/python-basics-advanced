"""
================================================================================
TOPIC: Multilevel Inheritance in Python
================================================================================
SHORT THEORY:
- In Multilevel Inheritance, a class is derived from a class that is itself derived from another class.
- Structure: Grandparent -> Parent -> Child.
- The bottom child inherits all methods and attributes across the entire ancestor chain.

SYNTAX REFERENCE:
    class Base: ...
    class Intermediate(Base): ...
    class Derived(Intermediate): ...

KEY TAKEAWAYS / PITFALLS:
- Keep inheritance trees reasonably shallow (rarely exceed 3 levels) to avoid high coupling.
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

class Device:
    def __init__(self, brand: str) -> None:
        self.brand = brand

    def power_on(self) -> str:
        return f"{self.brand} device powered ON."


class Computer(Device):
    def __init__(self, brand: str, ram_gb: int) -> None:
        super().__init__(brand)
        self.ram_gb = ram_gb

    def run_diagnostics(self) -> str:
        return f"Checking {self.ram_gb}GB RAM integrity..."


class Laptop(Computer):
    def __init__(self, brand: str, ram_gb: int, battery_life_hrs: int) -> None:
        super().__init__(brand, ram_gb)
        self.battery_life_hrs = battery_life_hrs

    def battery_status(self) -> str:
        return f"Battery remaining: ~{self.battery_life_hrs} hours."


macbook = Laptop("Apple", 16, 18)

# Inherited from Device (Grandparent)
print(macbook.power_on())

# Inherited from Computer (Parent)
print(macbook.run_diagnostics())

# Native to Laptop (Child)
print(macbook.battery_status())

# Check inheritance hierarchy
print("\nMRO for Laptop:")
for cls in Laptop.__mro__:
    print(f"  -> {cls.__name__}")