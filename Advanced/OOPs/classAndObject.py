"""
================================================================================
TOPIC: Object-Oriented Programming (Classes, Objects, __init__, and self)
================================================================================
SHORT THEORY:
- Python is an object-oriented programming (OOP) language where real-world entities 
  are modeled as objects possessing state (attributes) and behavior (methods).
- `class`: Blueprint or template for creating objects.
- `object` / `instance`: A concrete manifestation of a class.
- `__init__(self, ...)`: The constructor / initializer method automatically executed 
  when a new instance is created.
- `self`: Represents the specific instance calling the method. Python passes it 
  automatically as the first parameter.

SYNTAX REFERENCE:
    class ClassName:
        def __init__(self, attr1, attr2):
            self.attr1 = attr1      # Instance attribute
            self.attr2 = attr2

        def method_name(self):       # Instance method
            return f"Action on {self.attr1}"

    obj = ClassName(val1, val2)      # Object instantiation
    obj.method_name()                # Invocation

KEY TAKEAWAYS / PITFALLS:
- Forgetting `self` as the first parameter in an instance method signature causes
  `TypeError: takes 0 positional arguments but 1 was given`.
- Instance attributes belong strictly to the specific instance created.
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

class Student:
    """Represents an academic student record."""
    def __init__(self, name: str, roll_no: int, age: int, marks: list[float]) -> None:
        self.name = name
        self.roll_no = roll_no
        self.age = age
        self.marks = marks

    def total(self) -> float:
        """Returns the sum of all subject marks."""
        return sum(self.marks)

    def average(self) -> float:
        """Returns the mean average mark."""
        return sum(self.marks) / len(self.marks) if self.marks else 0.0

    def get_grade(self) -> str:
        """Calculates letter grade based on average."""
        avg = self.average()
        if avg >= 90:
            return "Grade A"
        elif avg >= 75:
            return "Grade B"
        elif avg >= 60:
            return "Grade C"
        else:
            return "Grade F"

    def display_report(self) -> None:
        print(f"--- Student Report: {self.name} (Roll #{self.roll_no}) ---")
        print(f"Age: {self.age} | Total: {self.total()} | Average: {self.average():.2f}")
        print(f"Status: {self.get_grade()}\n")


# Instantiating objects
student1 = Student("Bishal Nag", 101, 22, [88.0, 92.5, 79.0, 95.0])
student2 = Student("Ananya Rao", 102, 21, [95.0, 98.0, 91.0, 94.0])

# Invoking methods on instances
student1.display_report()
student2.display_report()

# Inspecting attributes
print(f"Direct attribute access: student1.name = {student1.name}")