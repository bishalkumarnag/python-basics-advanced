"""
================================================================================
TOPIC: Magic / Dunder Methods in Python (Data Model & Operator Overloading)
================================================================================
SHORT THEORY:
- Dunder methods (double underscore methods) are special hook methods that Python 
  invokes behind the scenes when performing built-in operations.
- They allow custom objects to emulate native Python types (numbers, sequences, callables).
- Core Dunder Categories:
  1. String Representation: `__str__` (user-friendly display), `__repr__` (unambiguous developer representation)
  2. Arithmetic Operators: `__add__` (+), `__sub__` (-), `__mul__` (*), `__truediv__` (/)
  3. Comparison Operators: `__eq__` (==), `__lt__` (<), `__gt__` (>), `__le__` (<=)
  4. Sequence Protocol: `__len__` (len()), `__getitem__` (obj[key]), `__setitem__`
  5. Callables: `__call__` (enables calling object instances like functions: `obj()`)

SYNTAX REFERENCE:
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __eq__(self, other) -> bool: ...
    def __add__(self, other): ...
    def __len__(self) -> int: ...
    def __getitem__(self, index): ...
    def __call__(self, *args, **kwargs): ...

KEY TAKEAWAYS / PITFALLS:
- If `__str__` is not defined, Python falls back to `__repr__`. Always implement `__repr__` first!
- Implementing `__eq__` makes instances unhashable unless `__hash__` is also defined.
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

# Example 1: __str__, __repr__, and __add__ Operator Overloading
class Vector2D:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        # Machine / developer representation
        return f"Vector2D({self.x}, {self.y})"

    def __str__(self) -> str:
        # Clean user-facing representation
        return f"({self.x}, {self.y})"

    def __add__(self, other: "Vector2D") -> "Vector2D":
        # Overloads '+' operator
        if not isinstance(other, Vector2D):
            return NotImplemented
        return Vector2D(self.x + other.x, self.y + other.y)

    def __eq__(self, other: object) -> bool:
        # Overloads '==' operator
        if not isinstance(other, Vector2D):
            return False
        return self.x == other.x and self.y == other.y


v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)
v3 = v1 + v2  # Invokes v1.__add__(v2)

print(f"print(v3) using __str__: {v3}")          # (4, 6)
print(f"repr(v3) using __repr__: {repr(v3)}")    # Vector2D(4, 6)
print(f"v1 == Vector2D(3, 4): {v1 == Vector2D(3, 4)}") # True


# Example 2: Container Protocol (__len__, __getitem__)
class CustomPlaylist:
    def __init__(self, title: str, tracks: list[str]) -> None:
        self.title = title
        self.tracks = tracks

    def __len__(self) -> int:
        return len(self.tracks)

    def __getitem__(self, index: int) -> str:
        return self.tracks[index]


playlist = CustomPlaylist("Lo-Fi Study", ["Chill Beats", "Rain Sounds", "Midnight Drive"])
print(f"\nPlaylist length (len()): {len(playlist)}")  # 3
print(f"Accessing index 1 (playlist[1]): {playlist[1]}") # Rain Sounds

# Implementing __getitem__ automatically allows iteration via for loop!
print("Iterating playlist:")
for track in playlist:
    print(f"  Track: {track}")


# Example 3: Callable Instances (__call__)
class Multiplier:
    def __init__(self, factor: int) -> None:
        self.factor = factor

    def __call__(self, value: int) -> int:
        return self.factor * value


triple = Multiplier(3)
print(f"\nCallable object: triple(10) = {triple(10)}")  # 30
