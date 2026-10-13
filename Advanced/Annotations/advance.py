"""
================================================================================
TOPIC: Advanced Type Hints (Union |, Optional, Any, Callable, TypedDict, TypeVar)
================================================================================
SHORT THEORY:
- Modern Python (3.9+ and 3.10+) supports built-in generics directly without 
  importing from `typing` (e.g., `list[int]`, `dict[str, Any]`, `tuple[int, ...]`).
- Union Types: In Python 3.10+, write `int | str` instead of `Union[int, str]`.
- Optional: `str | None` indicates that a value can either be a string or `None`.
- `Callable[[ParamTypes], ReturnType]`: Type hint for functions passed as arguments.
- `TypedDict`: Defines dictionaries with fixed keys and value types.
- `TypeVar`: Generic type parameter for generic functions and classes.

SYNTAX REFERENCE:
    from typing import Callable, Any, TypedDict, TypeVar

    num_list: list[int] = [1, 2, 3]
    mapping: dict[str, int | float] = {"pi": 3.14}
    maybe_name: str | None = None
    T = TypeVar("T")

KEY TAKEAWAYS / PITFALLS:
- Prefer `X | None` over `Optional[X]` in Python 3.10+.
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

from typing import Callable, Any, TypedDict, TypeVar

# Example 1: Modern Built-in Collections and Union Types (Python 3.10+)
def process_scores(student_scores: list[int | float]) -> float:
    """Accepts list of ints or floats, returns float mean."""
    return sum(student_scores) / len(student_scores)

scores = [85, 92.5, 78, 90.0]
print(f"Average score: {process_scores(scores):.2f}")


# Example 2: Optional Parameters (Value or None)
def fetch_user_bio(user_id: int) -> str | None:
    records = {101: "Backend engineer passionate about Python."}
    return records.get(user_id, None)

print(f"User 101 bio: {fetch_user_bio(101)}")
print(f"User 999 bio: {fetch_user_bio(999)}")


# Example 3: Callable Type Hints (Higher-Order Functions)
def transform_elements(
    data: list[int], 
    transformation_fn: Callable[[int], int]
) -> list[int]:
    """Takes a list and a transformer function, applies it element-wise."""
    return [transformation_fn(x) for x in data]

doubled = transform_elements([1, 2, 3, 4], lambda n: n * 2)
print(f"\nCallable transform (doubled): {doubled}")


# Example 4: TypedDict (Structured Dictionary Schema)
class UserProfile(TypedDict):
    id: int
    username: str
    is_active: bool
    roles: list[str]

current_user: UserProfile = {
    "id": 1,
    "username": "bishalnag",
    "is_active": True,
    "roles": ["admin", "developer"]
}
print(f"\nTypedDict user: {current_user['username']} - Active: {current_user['is_active']}")


# Example 5: Generics with TypeVar
T = TypeVar("T")

def get_first_element(collection: list[T]) -> T | None:
    return collection[0] if collection else None

print(f"Generic first element (int): {get_first_element([10, 20, 30])}")
print(f"Generic first element (str): {get_first_element(['alpha', 'beta'])}")
