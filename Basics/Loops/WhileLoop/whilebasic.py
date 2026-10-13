"""
================================================================================
TOPIC: While Loops & Indefinite Iteration
================================================================================
SHORT THEORY:
- A `while` loop repeatedly executes a block of code as long as a specified condition
  evaluates to `True`.
- It is typically used for indefinite iteration—when the number of iterations 
  is not known in advance (e.g., reading a stream until EOF, waiting for user input, 
  converging algorithms).
- Like `for`, `while` supports `break`, `continue`, and an `else` clause (which executes
  when the loop condition becomes `False`, but not if exited via `break`).

SYNTAX REFERENCE:
    while condition:
        # statement(s)
        # update variable to prevent infinite loops
    else:
        # executed when condition evaluates to False

KEY TAKEAWAYS / PITFALLS:
- Forgetting to increment/update the loop control variable results in an INFINITE LOOP!
- Press `Ctrl + C` in the terminal to interrupt an infinite loop if accidentally triggered.
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

# Example 1: Basic Counter-controlled Loop
counter = 1
print("Counter increment from 1 to 5:")
while counter <= 5:
    print(counter, end=" ")
    counter += 1
print()

# Example 2: Filtering Even Numbers in a Range
start, end = 10, 20
current = start
print(f"\nEven numbers between {start} and {end}:")
while current <= end:
    if current % 2 == 0:
        print(current, end=" ")
    current += 1
print()

# Example 3: Simulating Sentinel-Controlled Loop (Break on Condition)
import random

target = 7
attempts = 0
found = False

print("\nSearching for lucky number 7 via simulated dice rolls:")
while attempts < 10:
    attempts += 1
    roll = random.randint(1, 10)
    print(f"Attempt {attempts}: rolled {roll}")
    if roll == target:
        print(f"Target {target} reached on attempt {attempts}!")
        found = True
        break
else:
    print("Reached max attempts without hitting lucky target.")

# Example 4: Digit Extraction & Manipulation using While Loop
def sum_of_digits(n: int) -> int:
    """Calculates sum of digits using arithmetic modulo without converting to string."""
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10  # extract last digit
        n //= 10         # drop last digit
    return total

print(f"\nSum of digits of 4829: {sum_of_digits(4829)}")  # 4+8+2+9 = 23
