"""
================================================================================
TOPIC: For Loops & range() in Python
================================================================================
SHORT THEORY:
- In Python, a `for` loop iterates over the items of any sequence (such as a 
  list, tuple, string) or other iterable object, in the order they appear.
- Unlike traditional C-style index loops, Python loops are essentially "for-each" loops.
- The `range()` built-in type generates an immutable arithmetic sequence of integers on-demand (lazy evaluation, memory efficient).
- `for...else`: The `else` block executes when the loop finishes iterating normally, 
  but is SKIPPED if the loop was terminated by a `break`.

SYNTAX REFERENCE:
    for item in iterable:
        # body

    range(stop)                        # 0 to stop - 1
    range(start, stop)                 # start to stop - 1
    range(start, stop, step)           # step increments (or decrements if negative)

    for item in iterable:
        if condition:
            break                      # Exit loop immediately
        if condition2:
            continue                   # Skip rest of current iteration
    else:
        # Runs ONLY if loop completed without encountering break

KEY TAKEAWAYS / PITFALLS:
- `range(start, stop)` is exclusive of `stop`.
- `range` objects do not generate all numbers in memory at once; they generate them on demand in O(1) memory.
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

# Example 1: Basic range() Traversals
print("1. Counting 1 to 5:")
for i in range(1, 6):
    print(i, end=" ")
print()  # Output: 1 2 3 4 5

print("\n2. Stepping by 2 (-5 to 5):")
for j in range(-5, 6, 2):
    print(j, end=" ")
print()  # Output: -5 -3 -1 1 3 5

print("\n3. Reverse counting (countdown):")
for k in range(5, 0, -1):
    print(k, end=" ")
print()  # Output: 5 4 3 2 1

# Example 2: Iterating Over Sequences (Lists and Strings)
frameworks = ["Django", "FastAPI", "Flask"]
print("\nIterating over elements:")
for fw in frameworks:
    print(f"Framework: {fw}")

word = "PYTHON"
print("\nIterating over characters:")
for char in word:
    print(char, end="-")
print()

# Example 3: Loop Control: break, continue, and pass
print("\nDemonstrating break and continue:")
for num in range(1, 10):
    if num == 3:
        continue  # Skips 3
    if num == 7:
        break     # Stops loop at 7
    print(num, end=" ")
print()  # Output: 1 2 4 5 6

# Example 4: The for-else Construct (Search with Fallback)
def search_target(items, target):
    for item in items:
        if item == target:
            print(f"Target '{target}' FOUND in list!")
            break
    else:
        # Executes only if target was NOT found (no break occurred)
        print(f"Target '{target}' NOT found!")

search_target([10, 20, 30, 40], 30)  # Found
search_target([10, 20, 30, 40], 99)  # Not found
