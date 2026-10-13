"""
================================================================================
TOPIC: Functional Programming in Python (map, filter, reduce)
================================================================================
SHORT THEORY:
- Python supports functional programming paradigms: treating computation as 
  the evaluation of mathematical functions without mutable state.
- Core Higher-Order Functions:
  1. `map(func, iterable)`: Applies `func` to every element in `iterable` lazily.
  2. `filter(predicate, iterable)`: Filters elements, yielding only those for 
     which `predicate(item)` evaluates to `True`.
  3. `functools.reduce(func, iterable[, initial])`: Cumulatively applies a binary function 
     to reduce an iterable down to a SINGLE scalar result.

SYNTAX REFERENCE:
    list(map(func, iterable))
    list(filter(lambda x: x > 0, iterable))
    from functools import reduce
    reduce(lambda acc, x: acc + x, iterable, 0)

KEY TAKEAWAYS / PITFALLS:
- In modern Python, List Comprehensions `[func(x) for x in iterable if cond]` are often 
  preferred over `map()` and `filter()` for readability.
- However, `map()` and `filter()` return lazy iterators without allocating full lists in memory.
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Example 1: map() - Transforming elements
celsius_temps = [0.0, 10.0, 20.0, 35.0, 100.0]
fahrenheit = list(map(lambda c: round((c * 9/5) + 32, 1), celsius_temps))
print("1. Celsius to Fahrenheit with map():")
print(f"   Celsius:    {celsius_temps}")
print(f"   Fahrenheit: {fahrenheit}")


# Example 2: filter() - Selecting elements based on a condition
def is_even(n: int) -> bool:
    return n % 2 == 0

evens = list(filter(is_even, numbers))
print("\n2. Filtering even numbers:")
print(f"   Original: {numbers}")
print(f"   Evens:    {evens}")


# Example 3: functools.reduce() - Aggregating to a single value
# Calculate product of all numbers (Factorial style)
data = [1, 2, 3, 4, 5]
product = reduce(lambda acc, val: acc * val, data, 1)
print(f"\n3. Product of {data} using reduce: {product}")  # 120

# Finding maximum value with reduce
find_max = reduce(lambda a, b: a if a > b else b, [45, 12, 89, 34, 76])
print(f"   Max using reduce: {find_max}")


# Example 4: Comparing Functional Pipeline vs List Comprehension
# Task: Sum the squares of all even numbers
even_square_sum_fn = reduce(
    lambda acc, x: acc + x, 
    map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)), 
    0
)

even_square_sum_comp = sum(x**2 for x in numbers if x % 2 == 0)

print(f"\n4. Pipeline result:      {even_square_sum_fn}")
print(f"   Comprehension result: {even_square_sum_comp}")
