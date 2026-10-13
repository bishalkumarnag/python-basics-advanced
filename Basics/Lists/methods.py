"""
================================================================================
TOPIC: Essential List Methods in Python
================================================================================
SHORT THEORY:
- Python provides built-in methods on list objects for adding, removing, searching, 
  and rearranging elements.
- Time complexities:
  - `append(x)`: O(1) amortized
  - `pop()`: O(1) from end
  - `pop(0)` or `insert(0, x)`: O(N) due to shifting all remaining elements
  - `remove(x)`: O(N) linear search followed by shift
  - `index(x)`: O(N) linear search
  - `sort()`: O(N log N) using Timsort algorithm

SYNTAX REFERENCE:
    lst.append(item)            # Adds item to the very end
    lst.extend(iterable)        # Appends all items from iterable
    lst.insert(index, item)     # Inserts item at specified index
    lst.remove(item)            # Removes first matching item (raises ValueError if absent)
    lst.pop([index])            # Removes and returns item at index (default: last)
    lst.clear()                 # Removes all items
    lst.index(item)             # Returns index of first occurrence
    lst.count(item)             # Counts occurrences of item
    lst.sort(key=None, reverse=False) # In-place sort
    lst.reverse()               # In-place reversal

KEY TAKEAWAYS / PITFALLS:
- `append([1, 2])` appends the list AS A SINGLE NESTED ELEMENT. Use `extend([1, 2])` 
  to flatten/concatenate items.
- `lst.sort()` returns `None`, not the list! Doing `lst = lst.sort()` overwrites `lst` with `None`.
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

# Example 1: Insertion (append vs extend vs insert)
nums = [10, 20, 30]
nums.append(40)              # [10, 20, 30, 40]
print(f"After append(40): {nums}")

nums.extend([50, 60])        # [10, 20, 30, 40, 50, 60]
print(f"After extend([50, 60]): {nums}")

nums.insert(0, 5)            # Insert 5 at index 0
print(f"After insert(0, 5): {nums}")


# Example 2: Deletion (pop vs remove vs clear)
last_val = nums.pop()        # Removes 60
print(f"Popped last element: {last_val}, remaining: {nums}")

idx2_val = nums.pop(2)       # Removes element at index 2
print(f"Popped index 2: {idx2_val}, remaining: {nums}")

nums.remove(30)              # Removes value 30
print(f"After remove(30): {nums}")


# Example 3: Searching and Counting
letters = ["a", "b", "c", "a", "b", "a"]
print(f"\nCount of 'a': {letters.count('a')}")     # 3
print(f"First index of 'b': {letters.index('b')}") # 1

# Safe check before index to prevent ValueError
target = "z"
if target in letters:
    print(letters.index(target))
else:
    print(f"'{target}' not found in letters")


# Example 4: In-place Sorting and Reversing
ranks = [45, 12, 89, 34, 7]
ranks.sort()
print(f"\nIn-place ascending: {ranks}")

ranks.sort(reverse=True)
print(f"In-place descending: {ranks}")

ranks.reverse()
print(f"In-place reversed: {ranks}")
