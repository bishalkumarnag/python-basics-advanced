"""
================================================================================
TOPIC: Functions in Python (Definition, Parameters, Return, Docstrings)
================================================================================
SHORT THEORY:
- A function is a reusable block of organized code that performs a single action.
- Functions provide modularity, avoid code duplication (DRY principle), and improve maintainability.
- Functions are defined using the `def` keyword, followed by the function name, parentheses `()`, and a colon `:`.
- Functions are first-class citizens in Python: they can be assigned to variables, 
  passed as arguments to other functions, and returned from functions.
- If a function does not specify an explicit `return` statement, it returns `None` by default.

SYNTAX REFERENCE:
    def function_name(param1: type, param2: type) -> return_type:
        \"\"\"Docstring explaining purpose, parameters, and returns.\"\"\"
        # body
        return result

KEY TAKEAWAYS / PITFALLS:
- `parameter`: The variable listed inside parentheses in the function definition.
- `argument`: The actual value sent to the function when it is called.
- Functions can return multiple values separated by commas, which Python packs into a single `tuple`.
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

# Example 1: Basic Function with Parameter and Docstring
def greet_user(name: str) -> str:
    """Returns a personalized greeting message."""
    return f"Hello, {name}! Welcome to Python."

message = greet_user("Bishal")
print(message)
# Inspect docstring via __doc__ or help()
print(f"Docstring: {greet_user.__doc__}")

# Example 2: Returning Multiple Values (Tuple Packing and Unpacking)
def calculate_circle_metrics(radius: float) -> tuple[float, float]:
    """Calculates both area and circumference of a circle."""
    import math
    area = math.pi * (radius ** 2)
    circumference = 2 * math.pi * radius
    return round(area, 2), round(circumference, 2)

circle_area, circle_circum = calculate_circle_metrics(5.0)
print(f"Radius 5 -> Area: {circle_area}, Circumference: {circle_circum}")

# Example 3: Function Returning None Implicitly vs Explicitly
def log_event(event: str) -> None:
    print(f"[LOG]: {event}")

res = log_event("Database connection established")
print(f"Return value of log_event: {res}")  # Output: None

# Example 4: Functions as First-Class Citizens
def square(n: int) -> int:
    return n * n

def cube(n: int) -> int:
    return n * n * n

# Assign function to variable
operation = square
print(f"Operation(4) via alias: {operation(4)}")  # 16

# Pass function as an argument
def apply_math(func, val):
    return func(val)

print(f"Apply cube to 3: {apply_math(cube, 3)}")   # 27