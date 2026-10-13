"""
================================================================================
TOPIC: Pythonic Getters & Setters with @property Decorator
================================================================================
SHORT THEORY:
- The `@property` decorator is the Pythonic way to implement getters and setters.
- It allows method calls to masquerade as standard attribute accesses (`obj.name` 
  instead of `obj.get_name()`), while still running validation code behind the scenes.
- Benefits:
  1. Preserves backwards compatibility: code using `obj.attribute` doesn't need to change.
  2. Enables computed attributes (attributes calculated on the fly without storing duplicate state).
  3. Supports deletion hooks via `@attribute.deleter`.

SYNTAX REFERENCE:
    class Model:
        @property
        def attribute(self):
            return self._attribute      # Getter

        @attribute.setter
        def attribute(self, value):
            self._attribute = value      # Setter

        @attribute.deleter
        def attribute(self):
            del self._attribute          # Deleter

KEY TAKEAWAYS / PITFALLS:
- The setter method name MUST match the getter method name (`@name.setter def name(self, val):`).
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

class Celsius:
    def __init__(self, temperature: float = 0.0) -> None:
        self._temperature = temperature

    # Getter: Access as obj.temperature without parentheses ()
    @property
    def temperature(self) -> float:
        return self._temperature

    # Setter: Set as obj.temperature = 25
    @temperature.setter
    def temperature(self, value: float) -> None:
        if value < -273.15:
            raise ValueError(f"Temperature {value}°C is below Absolute Zero (-273.15°C)!")
        self._temperature = value

    # Computed Property: Calculated dynamically
    @property
    def to_fahrenheit(self) -> float:
        return (self._temperature * 9 / 5) + 32


temp = Celsius(25.0)
print(f"Current temp in Celsius:    {temp.temperature}°C")
print(f"Computed temp in Fahrenheit: {temp.to_fahrenheit}°F")

# Mutating via property setter (clean syntax)
temp.temperature = 37.0
print(f"\nAfter update to 37°C:")
print(f"Celsius:    {temp.temperature}°C")
print(f"Fahrenheit: {temp.to_fahrenheit}°F")

# Validating boundaries
try:
    temp.temperature = -300.0  # Should trigger ValueError
except ValueError as err:
    print(f"\nValidation caught: {err}")
