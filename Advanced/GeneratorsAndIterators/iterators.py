"""
================================================================================
TOPIC: The Iterator Protocol in Python (__iter__, __next__, StopIteration)
================================================================================
SHORT THEORY:
- Iterable: An object capable of returning its members one at a time. Must implement `__iter__()`.
  Examples: `list`, `str`, `tuple`, `dict`, `range`.
- Iterator: An object that represents a stream of data. Must implement both:
  1. `__iter__()`: Returns the iterator object itself.
  2. `__next__()`: Returns the next element from the stream. When no further elements 
     remain, it MUST raise `StopIteration`.
- The built-in `iter(obj)` calls `obj.__iter__()`.
- The built-in `next(it[, default])` calls `it.__next__()`.
- A standard Python `for item in iterable:` loop is syntactic sugar that obtains 
  an iterator via `iter()` and calls `next()` until `StopIteration` is raised.

SYNTAX REFERENCE:
    class MyIterator:
        def __iter__(self):
            return self

        def __next__(self):
            if condition:
                return value
            raise StopIteration

KEY TAKEAWAYS / PITFALLS:
- An iterator can only be traversed ONCE. Once exhausted, calling `next()` keeps 
  raising `StopIteration`. To traverse again, obtain a fresh iterator from the iterable.
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

# Example 1: Manual Iteration with iter() and next()
fruits = ["apple", "banana", "cherry"]
iterator = iter(fruits)

print("Manual step-by-step iteration:")
print(next(iterator))  # 'apple'
print(next(iterator))  # 'banana'
print(next(iterator))  # 'cherry'

# Next call raises StopIteration; handle safely with fallback:
print("Exhausted iterator with fallback:", next(iterator, "STREAM_EXHAUSTED"))


# Example 2: Implementing a Custom Iterable Class from Scratch
class Countdown:
    """Custom iterator that counts down from start to 1."""
    def __init__(self, start: int) -> None:
        self.current = start

    def __iter__(self):
        # Must return self as the iterator
        return self

    def __next__(self) -> int:
        if self.current <= 0:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val


print("\nCustom Countdown Iterator via for loop:")
cd = Countdown(5)
for number in cd:
    print(f"Countdown: {number}")


# Example 3: Infinite Even Number Stream (Manual lazy iterator)
class InfiniteEvens:
    def __init__(self) -> None:
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self) -> int:
        val = self.num
        self.num += 2
        return val

even_stream = InfiniteEvens()
print("\nFetching first 4 items from infinite even stream:")
for _ in range(4):
    print(next(even_stream), end=" ")
print()
