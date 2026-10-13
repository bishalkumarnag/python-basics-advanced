"""
================================================================================
PRACTICE QUESTIONS: Functions & Modular Programming
================================================================================
"""

# ==============================================================================
# PROBLEM 1: Palindrome String Checker
# Check if a given string is a palindrome (ignoring spaces and casing).
# ==============================================================================
def is_palindrome(text: str) -> bool:
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]

print("Problem 1: Palindrome tests:")
print("A man a plan a canal Panama:", is_palindrome("A man a plan a canal Panama")) # True
print("Hello World:", is_palindrome("Hello World"))                             # False


# ==============================================================================
# PROBLEM 2: Factorial (Iterative vs Recursive)
# Calculate n! for any non-negative integer n.
# ==============================================================================
def factorial_iterative(n: int) -> int:
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_recursive(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

print(f"\nProblem 2: 5! iterative: {factorial_iterative(5)}")
print(f"5! recursive: {factorial_recursive(5)}")


# ==============================================================================
# PROBLEM 3: Character Frequency Counter
# Return a dictionary counting how many times each character appears in a string.
# ==============================================================================
def count_char_frequencies(s: str) -> dict[str, int]:
    freq_map = {}
    for char in s:
        freq_map[char] = freq_map.get(char, 0) + 1
    return freq_map

print("\nProblem 3: Character frequencies:")
sample_str = "programming"
print(f"'{sample_str}' -> {count_char_frequencies(sample_str)}")


# ==============================================================================
# PROBLEM 4: Find Maximum of Three Numbers
# ==============================================================================
def find_largest_of_three(a: float, b: float, c: float) -> float:
    largest = a
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    return largest

print(f"\nProblem 4: Largest of (14, 89, 42): {find_largest_of_three(14, 89, 42)}")