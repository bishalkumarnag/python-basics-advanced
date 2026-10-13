"""
================================================================================
TOPIC: Polymorphism & Duck Typing in Python
================================================================================
SHORT THEORY:
- Polymorphism (Greek for "many forms") is the ability of different objects to respond 
  to the same method call in their own specific ways.
- Forms of Polymorphism in Python:
  1. Method Overriding: Subclasses providing custom implementations of parent methods.
  2. Duck Typing: "If it walks like a duck and quacks like a duck, it's a duck." 
     Python does not care about an object's formal class inheritance—only whether 
     it possesses the requested methods/attributes at runtime.
  3. Operator Polymorphism: The `+` operator performs addition on numbers, 
     concatenation on strings/lists, and custom vector addition if `__add__` is defined.

SYNTAX REFERENCE:
    # Polymorphic loop over diverse objects:
    for item in [obj1, obj2, obj3]:
        item.common_action()

KEY TAKEAWAYS / PITFALLS:
- Duck typing emphasizes behavioral contracts over strict nominal type checks (`isinstance()`).
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

# Example 1: Polymorphism via Class Hierarchy
class Animal:
    def speak(self) -> str:
        raise NotImplementedError("Subclasses must implement speak()")


class Dog(Animal):
    def speak(self) -> str:
        return "Woof! Woof!"


class Cat(Animal):
    def speak(self) -> str:
        return "Meow~"


class Duck(Animal):
    def speak(self) -> str:
        return "Quack quack!"


# Polymorphic execution
animals: list[Animal] = [Dog(), Cat(), Duck()]
print("Polymorphic sound outputs:")
for a in animals:
    print(f"  {a.__class__.__name__}: {a.speak()}")


# Example 2: Python Duck Typing (No Shared Base Class Required!)
class AudioBook:
    def read(self) -> str:
        return "Playing narrator audio stream..."

class PDFDocument:
    def read(self) -> str:
        return "Extracting text from PDF pages..."

class KindleEBook:
    def read(self) -> str:
        return "Rendering e-ink digital typography..."


# Notice: No shared base class, yet all satisfy the 'reader' contract!
def process_reading_material(media_item) -> None:
    print(f"[MEDIA VIEWER]: {media_item.read()}")

print("\nDuck Typing Demonstration:")
library = [AudioBook(), PDFDocument(), KindleEBook()]
for item in library:
    process_reading_material(item)


# Example 3: Operator Polymorphism
print("\nOperator Polymorphism with '+':")
print("Ints:    ", 5 + 10)                  # 15
print("Floats:  ", 3.2 + 1.8)                # 5.0
print("Strings: ", "Python" + "ic")          # Pythonic
print("Lists:   ", [1, 2] + [3, 4])          # [1, 2, 3, 4]
