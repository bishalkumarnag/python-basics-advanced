"""
================================================================================
TOPIC: enumerate() & zip() in Python Loops
================================================================================
SHORT THEORY:
- `enumerate(iterable, start=0)`: Adds a counter/index to an iterable and returns 
  an enumerate object yielding `(index, value)` tuples.
- Eliminates manual index tracking variables (`i = 0 ... i += 1`).
- `zip(*iterables)`: Aggregates elements from two or more iterables in parallel, 
  yielding tuples of corresponding elements. It stops at the shortest iterable length.

SYNTAX REFERENCE:
    for index, value in enumerate(iterable, start=0):
        ...

    for val1, val2 in zip(list1, list2):
        ...

KEY TAKEAWAYS / PITFALLS:
- Never do `for i in range(len(my_list)): print(i, my_list[i])`. 
  The Pythonic idiom is `for i, item in enumerate(my_list):`.
- `zip()` stops when the shortest iterable is exhausted. If you need padding for 
  unequal lengths, use `itertools.zip_longest()`.
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

# Example 1: Basic enumerate() (0-indexed)
languages = ["Python", "Go", "Rust", "TypeScript"]
print("0-based indexing:")
for idx, lang in enumerate(languages):
    print(f"Index {idx}: {lang}")

# Example 2: enumerate() with Custom Starting Index
print("\n1-based rank indexing:")
for rank, lang in enumerate(languages, start=1):
    print(f"Rank #{rank}: {lang}")

# Example 3: Parallel Iteration with zip()
names = ["Alice", "Bob", "Charlie"]
scores = [95, 88, 92]
grades = ["A+", "B+", "A"]

print("\nCombining collections with zip():")
for name, score, grade in zip(names, scores, grades):
    print(f"Student: {name:<8} | Score: {score} | Grade: {grade}")

# Example 4: Creating a Dictionary using zip()
keys = ["id", "username", "role"]
values = [101, "bnag", "Admin"]
user_dict = dict(zip(keys, values))
print(f"\nDictionary constructed from zipped pairs: {user_dict}")