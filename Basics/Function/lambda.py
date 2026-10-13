"""
================================================================================
TOPIC: Anonymous Functions (Lambda Expressions)
================================================================================
SHORT THEORY:
- A lambda function is a small, anonymous (unnamed) inline function defined with 
  the `lambda` keyword.
- A lambda function can take any number of arguments, but can only contain 
  a SINGLE expression, which is evaluated and automatically returned.
- Commonly used as short callback functions passed to higher-order functions like 
  `sorted(key=...)`, `map()`, `filter()`, and `min()`/`max()`.

SYNTAX REFERENCE:
    lambda arg1, arg2, ...: expression
    sorted(iterable, key=lambda x: ...)
    map(lambda x: ..., iterable)
    filter(lambda x: ..., iterable)

KEY TAKEAWAYS / PITFALLS:
- Lambdas cannot contain statements (e.g., `print()`, `return`, `pass`, assignments `=`).
- If a function has complex logic or multiple lines, use a standard `def` function 
  instead of forcing a convoluted lambda.
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

# Example 1: Basic Arithmetic Lambdas
square = lambda n: n * n
multiply = lambda a, b: a * b
is_adult = lambda age: age >= 18

print("1. Basic lambda evaluations:")
print(f"square(6) = {square(6)}")             # 36
print(f"multiply(7, 8) = {multiply(7, 8)}")   # 56
print(f"is_adult(20) = {is_adult(20)}")       # True

# Example 2: Lambdas with Custom Sorting (Key Functions)
employees = [
    {"name": "Alice", "age": 30, "salary": 85000},
    {"name": "Bob", "age": 24, "salary": 92000},
    {"name": "Charlie", "age": 28, "salary": 65000}
]

# Sort by age
by_age = sorted(employees, key=lambda emp: emp["age"])
print("\nSorted by Age:")
for e in by_age:
    print(f"  {e['name']}: {e['age']} yrs")

# Sort by salary descending
by_salary = sorted(employees, key=lambda emp: emp["salary"], reverse=True)
print("\nSorted by Salary Descending:")
for e in by_salary:
    print(f"  {e['name']}: ${e['salary']}")

# Example 3: Lambdas with map() and filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"\nFiltered evens: {evens}")

# Map to squares
squared_evens = list(map(lambda x: x ** 2, evens))
print(f"Squared evens: {squared_evens}")

# Example 4: Sorting Tuples by Secondary Elements
pairs = [(1, "one"), (3, "three"), (2, "two"), (4, "four")]
# Sort alphabetically by the string value
sorted_pairs = sorted(pairs, key=lambda pair: pair[1])
print(f"\nPairs sorted by word: {sorted_pairs}")