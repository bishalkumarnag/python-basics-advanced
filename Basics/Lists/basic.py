"""
================================================================================
TOPIC: Python Lists (Creation, Indexing, Mutability, Built-ins)
================================================================================
SHORT THEORY:
- A list is an ordered, mutable (changeable) collection of items.
- Lists allow duplicate elements and can contain heterogeneous data types 
  (integers, strings, floats, other lists, objects).
- Lists are dynamically sized arrays implemented under the hood in CPython as 
  contiguous arrays of pointers, offering O(1) random access by index.
- Negative indexing counts backward from the end (-1 is the last element).

SYNTAX REFERENCE:
    my_list = [item1, item2, item3]
    empty_list = [] or list()
    len(my_list)              # Total number of elements: O(1)
    min(my_list), max(my_list)# Min and max values in iterable
    sum(my_list)              # Sum of numeric elements
    sorted(my_list)           # Returns a NEW sorted list without modifying original
    list1 + list2             # List concatenation
    list1 * n                 # List repetition

KEY TAKEAWAYS / PITFALLS:
- Accessing an index outside `len(lst) - 1` raises an `IndexError`.
- `sorted(lst)` returns a new list; `lst.sort()` modifies the list in place and returns `None`.
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

# Example 1: Creation and Indexing
fruits = ["apple", "banana", "cherry", "date"]
print(f"Original list: {fruits}")
print(f"First element fruits[0]: {fruits[0]}")
print(f"Last element fruits[-1]: {fruits[-1]}")
print(f"Second to last fruits[-2]: {fruits[-2]}")

# Example 2: In-Place Mutation
fruits[1] = "blueberry"
print(f"After mutating index 1: {fruits}")

# Example 3: Concatenation and Repetition
primes = [2, 3, 5]
evens = [4, 6, 8]
combined = primes + evens
print(f"Concatenated: {combined}")

repeated = [0] * 5  # Common idiom to initialize fixed-size list
print(f"Repeated zeroes: {repeated}")

# Example 4: Built-in Aggregate Functions
scores = [88, 92, 79, 95, 64, 88]
print(f"\nScores: {scores}")
print(f"Count (len): {len(scores)}")
print(f"Highest (max): {max(scores)}")
print(f"Lowest (min): {min(scores)}")
print(f"Total (sum): {sum(scores)}")
print(f"Average: {sum(scores) / len(scores):.2f}")

# Example 5: sorted() vs in-place sort()
original = [5, 2, 9, 1, 7]
sorted_copy = sorted(original)
print(f"\nOriginal after sorted(): {original}")
print(f"New sorted copy: {sorted_copy}")

descending_copy = sorted(original, reverse=True)
print(f"Descending copy: {descending_copy}")
