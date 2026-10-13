"""
================================================================================
PRACTICE QUESTIONS: While Loops
================================================================================
"""

# ==============================================================================
# PROBLEM 1: Multiples of 3 and 5 (FizzBuzz range generator)
# Find and collect all numbers divisible by both 3 and 5 from 1 up to N.
# ==============================================================================
def find_divisible_by_3_and_5(limit: int = 100) -> list[int]:
    results = []
    current = 1
    while current <= limit:
        if current % 3 == 0 and current % 5 == 0:
            results.append(current)
        current += 1
    return results

print("Problem 1: Multiples of 3 and 5 up to 100:")
print(find_divisible_by_3_and_5(100))


# ==============================================================================
# PROBLEM 2: Sum of First N Natural Numbers
# Calculate 1 + 2 + ... + N using a while loop.
# ==============================================================================
def sum_first_n(n: int) -> int:
    i = 1
    total = 0
    while i <= n:
        total += i
        i += 1
    return total

print(f"\nProblem 2: Sum 1..100: {sum_first_n(100)}")  # 5050


# ==============================================================================
# PROBLEM 3: Reverse an Integer (e.g., 1234 -> 4321)
# ==============================================================================
def reverse_integer(num: int) -> int:
    is_neg = num < 0
    num = abs(num)
    reversed_num = 0
    while num > 0:
        remainder = num % 10
        reversed_num = (reversed_num * 10) + remainder
        num //= 10
    return -reversed_num if is_neg else reversed_num

print(f"\nProblem 3: Reverse 12345: {reverse_integer(12345)}")
print(f"Reverse -987: {reverse_integer(-987)}")


# ==============================================================================
# PROBLEM 4: Greatest Common Divisor (GCD) using Euclidean Algorithm
# ==============================================================================
def compute_gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a

print(f"\nProblem 4: GCD(48, 18): {compute_gcd(48, 18)}")  # 6