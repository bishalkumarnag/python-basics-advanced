"""
================================================================================
TOPIC: Instance Methods vs Class Methods vs Static Methods
================================================================================
SHORT THEORY:
- Instance Method: Takes `self` as the first parameter. Accesses and modifies object state.
- Class Method (`@classmethod`): Takes `cls` as the first parameter. Bound to the class, 
  not the instance. Frequently used as alternative constructors (factory methods).
- Static Method (`@staticmethod`): Takes neither `self` nor `cls`. Behaves like a regular 
  plain function scoped inside the class namespace for logical grouping.

SYNTAX REFERENCE:
    class Service:
        def instance_method(self):
            ...

        @classmethod
        def from_string(cls, data_str):
            # Alternative constructor
            return cls(...)

        @staticmethod
        def is_valid_port(port):
            return 1 <= port <= 65535

KEY TAKEAWAYS / PITFALLS:
- Use `@classmethod` when you need access to the class (e.g., creating instances or modifying class state).
- Use `@staticmethod` for pure utility functions that don't need access to instance or class state.
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

class Date:
    def __init__(self, year: int, month: int, day: int) -> None:
        self.year = year
        self.month = month
        self.day = day

    # 1. Instance Method
    def format_iso(self) -> str:
        return f"{self.year:04d}-{self.month:02d}-{self.day:02d}"

    # 2. Class Method as Factory Constructor
    @classmethod
    def from_string(cls, date_str: str):
        """Parses 'YYYY-MM-DD' formatted string and returns Date instance."""
        year, month, day = map(int, date_str.split("-"))
        return cls(year, month, day)

    # 3. Static Method Utility
    @staticmethod
    def is_leap_year(year: int) -> bool:
        """Pure utility check independent of any specific Date instance."""
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


# Standard instantiation
d1 = Date(2026, 10, 13)
print(f"Direct instantiation: {d1.format_iso()}")

# Factory instantiation via @classmethod
d2 = Date.from_string("2024-02-29")
print(f"Factory instantiation via from_string: {d2.format_iso()}")

# Calling static method via Class and Instance
print(f"Is 2024 leap year? {Date.is_leap_year(2024)}")  # True
print(f"Is 2026 leap year? {Date.is_leap_year(2026)}")  # False
