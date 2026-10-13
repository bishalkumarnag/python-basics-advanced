"""
================================================================================
TOPIC: Multiple Inheritance in Python
================================================================================
SHORT THEORY:
- In Multiple Inheritance, a class derives from MORE THAN ONE parent class simultaneously.
- Powerful for composing functionality through "Mixins" (e.g., logging, serialization).
- Attribute/method resolution follows the order specified in class definition: `class Child(P1, P2)`.
  If both P1 and P2 have a method with the same name, P1 takes precedence.

SYNTAX REFERENCE:
    class ParentA: ...
    class ParentB: ...
    class Child(ParentA, ParentB): ...

KEY TAKEAWAYS / PITFALLS:
- Can lead to ambiguity when multiple parents define identical method names 
  (the Diamond Problem).
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

class JSONSerializableMixin:
    """Mixin class providing JSON export behavior."""
    def to_json(self) -> str:
        import json
        return json.dumps(self.__dict__)


class LoggingMixin:
    """Mixin class providing audit logging capability."""
    def log(self, message: str) -> None:
        print(f"[{self.__class__.__name__} LOG]: {message}")


class UserAccount(JSONSerializableMixin, LoggingMixin):
    """Business entity inheriting from multiple mixins."""
    def __init__(self, username: str, email: str) -> None:
        self.username = username
        self.email = email
        self.log(f"Account instantiated for '{self.username}'")


user = UserAccount("bishal_nag", "bishal@example.com")

# Calling method from LoggingMixin
user.log("User updated credentials.")

# Calling method from JSONSerializableMixin
print("JSON representation:", user.to_json())

# Inspect MRO
print("\nMRO for UserAccount:", [cls.__name__ for cls in UserAccount.__mro__])
