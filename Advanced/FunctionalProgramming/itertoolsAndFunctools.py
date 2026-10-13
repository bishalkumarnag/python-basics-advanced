"""
================================================================================
TOPIC: Advanced Utilities: itertools & functools Standard Libraries
================================================================================
SHORT THEORY:
- `itertools`: Provides memory-efficient building blocks for iterator algebra.
  - `chain(*iterables)`: Chains multiple iterables sequentially without creating a combined list.
  - `cycle(iterable)`: Cycles infinitely through an iterable.
  - `combinations(iterable, r)`: Generates unordered combinations of length r.
  - `permutations(iterable, r)`: Generates ordered permutations of length r.
  - `accumulate(iterable[, func])`: Generates running totals/accumulations.
- `functools`: Higher-order functions that act on or return other functions.
  - `@lru_cache(maxsize=128)`: Memoizes function call results (caching) to eliminate redundant calculations.
  - `partial(func, *args, **kwargs)`: Freezes a portion of a function's arguments to produce a new callable.

SYNTAX REFERENCE:
    import itertools
    from functools import lru_cache, partial

    itertools.chain(list1, list2)
    itertools.combinations("ABC", 2)
    @lru_cache(maxsize=None)
    partial(func, fixed_arg)

KEY TAKEAWAYS / PITFALLS:
- `@lru_cache` only works for functions whose arguments are hashable! 
  Passing a mutable `list` to an `@lru_cache` function raises `TypeError: unhashable type: 'list'`.
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

import itertools
from functools import lru_cache, partial

# Example 1: Memoization with @lru_cache (Eliminating Exponential O(2^N) Recursion)
@lru_cache(maxsize=128)
def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("1. Fast Fibonacci via @lru_cache:")
print(f"   fibonacci(50) = {fibonacci(50)}")
print(f"   Cache info:     {fibonacci.cache_info()}")


# Example 2: Partial Function Application with functools.partial
def compute_power(base: float, exponent: float) -> float:
    return base ** exponent

# Pre-bind exponent to 2 (Square) and 3 (Cube)
square_fn = partial(compute_power, exponent=2)
cube_fn = partial(compute_power, exponent=3)

print("\n2. Partial Functions:")
print(f"   square_fn(8) = {square_fn(8)}")  # 64.0
print(f"   cube_fn(4)   = {cube_fn(4)}")    # 64.0


# Example 3: itertools.chain (Zero-overhead sequence merging)
list_a = [1, 2, 3]
list_b = ["a", "b", "c"]
chained_stream = itertools.chain(list_a, list_b)
print("\n3. Chained stream without memory copy:")
print(f"   {list(chained_stream)}")


# Example 4: Combinatorics: Permutations & Combinations
team_members = ["Alice", "Bob", "Charlie"]
print("\n4. Combinatorics:")
# Combinations of 2 (order does NOT matter)
combos = list(itertools.combinations(team_members, 2))
print(f"   Combinations (n=2): {combos}")

# Permutations of 2 (order DOES matter)
perms = list(itertools.permutations(team_members, 2))
print(f"   Permutations (n=2): {perms}")


# Example 5: Running Accumulation
revenues = [100, 250, 80, 400]
running_totals = list(itertools.accumulate(revenues))
print("\n5. Running Totals with itertools.accumulate:")
print(f"   Monthly revenue: {revenues}")
print(f"   Cumulative:      {running_totals}")
