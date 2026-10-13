"""
================================================================================
TOPIC: Classic Getter & Setter Methods (Java-Style)
================================================================================
SHORT THEORY:
- In object-oriented programming, getter and setter methods provide indirect 
  controlled access to private/protected attributes.
- Getters return the attribute value without exposing internal representation.
- Setters allow validating incoming data before updating state (e.g., rejecting negative values).

SYNTAX REFERENCE:
    def get_attr(self): return self.__attr
    def set_attr(self, val): self.__attr = val

KEY TAKEAWAYS / PITFALLS:
- Classic `get_attr()` and `set_attr()` can feel verbose and unpythonic compared to 
  the `@property` decorator, but they are common in traditional OOP designs.
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

class Student:
    def __init__(self, name: str, age: int) -> None:
        self.__name = name
        self.__age = age

    # Getter for name
    def get_name(self) -> str:
        return self.__name

    # Setter for name
    def set_name(self, new_name: str) -> None:
        if not new_name.strip():
            raise ValueError("Student name cannot be empty.")
        self.__name = new_name.strip()

    # Getter for age
    def get_age(self) -> int:
        return self.__age

    # Setter for age with validation
    def set_age(self, new_age: int) -> None:
        if new_age < 0 or new_age > 120:
            raise ValueError("Invalid age provided.")
        self.__age = new_age


s1 = Student("Bishal", 22)
print("Initial student name:", s1.get_name())
print("Initial student age: ", s1.get_age())

s1.set_name("Bishal Nag")
s1.set_age(23)
print("\nUpdated student name:", s1.get_name())
print("Updated student age: ", s1.get_age())