"""
================================================================================
TOPIC: List Slicing & Advanced Subscripting in Python
================================================================================
SHORT THEORY:
- Slicing extracts a contiguous subsequence from a list into a brand new shallow-copied list.
- Syntax: `sequence[start:stop:step]`
  - `start`: Index where slice begins (inclusive). Defaults to `0` (or end if negative step).
  - `stop`: Index where slice terminates (exclusive). Defaults to `len(sequence)`.
  - `step`: Interval between indices. Defaults to `1`.
- Slicing is forgiving: unlike single index access `lst[100]`, slicing out of bounds 
  does NOT raise an `IndexError`; it simply clips to the list boundary.

SYNTAX REFERENCE:
    lst[:]          # Shallow copy of the entire list
    lst[2:6]        # From index 2 up to index 5
    lst[:4]         # From index 0 up to index 3
    lst[3:]         # From index 3 to the very end
    lst[::2]        # Every second element
    lst[::-1]       # Reverses list
    lst[start:stop] = new_elements # In-place slice assignment/replacement

KEY TAKEAWAYS / PITFALLS:
- `lst[::-1]` creates a NEW reversed list; `lst.reverse()` reverses IN-PLACE.
- Slice assignment can change the length of the list in-place: `lst[1:3] = [10, 20, 30, 40]`.
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

# Example 1: Basic Positive Slicing
data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f"Full list: {data}")
print(f"data[2:6]: {data[2:6]}")    # [2, 3, 4, 5]
print(f"data[:4]:  {data[:4]}")     # [0, 1, 2, 3]
print(f"data[6:]:  {data[6:]}")     # [6, 7, 8, 9]

# Example 2: Negative Indices and Stepping
print(f"data[-4:]: {data[-4:]}")    # Last 4 elements: [6, 7, 8, 9]
print(f"data[:-3]: {data[:-3]}")    # Everything except last 3: [0, 1, 2, 3, 4, 5, 6]
print(f"data[::2]: {data[::2]}")    # Even indices: [0, 2, 4, 6, 8]
print(f"data[1::2]: {data[1::2]}")  # Odd indices: [1, 3, 5, 7, 9]

# Example 3: Reversal using Slicing
reversed_data = data[::-1]
print(f"Reversed via [::-1]: {reversed_data}")

# Example 4: In-Place Slice Assignment (Modifying Range of Elements)
colors = ["red", "green", "blue", "yellow", "purple"]
print(f"\nOriginal colors: {colors}")

# Replace 'green' and 'blue' (indices 1:3) with new items
colors[1:3] = ["emerald", "cyan"]
print(f"After slice replacement: {colors}")

# Delete items using slice deletion
del colors[3:]
print(f"After slice deletion: {colors}")

# Example 5: Creating an Independent Shallow Copy via [:]
original_nums = [1, 2, 3]
cloned_nums = original_nums[:]
cloned_nums.append(99)

print(f"\nOriginal: {original_nums}")  # [1, 2, 3] (Unchanged)
print(f"Cloned:   {cloned_nums}")    # [1, 2, 3, 99]