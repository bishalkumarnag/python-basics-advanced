"""
================================================================================
TOPIC: Variable Scope & Namespaces (LEGB Rule, global, nonlocal)
================================================================================
SHORT THEORY:
- Scope defines the region of a program where a variable is accessible.
- Python resolves variable names using the LEGB Rule (in order of search):
  1. L - Local: Defined inside the current function/lambda.
  2. E - Enclosing: Defined in the enclosing/outer function (nested functions/closures).
  3. G - Global: Defined at the top level of the module/script.
  4. B - Built-in: Built-in names pre-assigned in Python (e.g., `len`, `range`, `print`).
- Modifying Scopes:
  - `global`: Declares that a variable inside a function refers to the module-level global variable.
  - `nonlocal`: Declares that a variable inside a nested function refers to the nearest enclosing (outer) function's variable.

SYNTAX REFERENCE:
    global variable_name     # Binds to global scope
    nonlocal variable_name   # Binds to enclosing outer function scope

KEY TAKEAWAYS / PITFALLS:
- Attempting to read and then modify a global variable without the `global` keyword
  causes `UnboundLocalError: local variable referenced before assignment`.
- Use global variables sparingly; heavy mutation of globals makes debugging hard.
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

# Example 1: Local Scope vs Global Scope
app_name = "InventorySystem"  # Global variable

def print_app_info():
    version = "1.0.0"         # Local variable
    print(f"Inside function: {app_name} v{version}")

print_app_info()
# print(version) -> NameError: name 'version' is not defined (local to function)


# Example 2: Modifying Global Variables using `global`
counter = 0

def increment_counter():
    global counter
    counter += 1

print(f"\nInitial counter: {counter}")
increment_counter()
increment_counter()
print(f"Counter after calls: {counter}")  # Output: 2


# Example 3: Enclosing Scope & `nonlocal` in Nested Functions
def outer_counter():
    count = 0
    
    def inner_step():
        nonlocal count  # Targets 'count' in outer_counter, not global
        count += 1
        return count
        
    return inner_step

step_fn = outer_counter()
print(f"\nNonlocal step 1: {step_fn()}")  # 1
print(f"Nonlocal step 2: {step_fn()}")    # 2
print(f"Nonlocal step 3: {step_fn()}")    # 3


# Example 4: The UnboundLocalError Trap Explained
x = 10
def faulty_increment():
    # If Python sees assignment `x = ...` anywhere in the function,
    # it marks `x` as local for the entire function!
    # print(x) -> Would fail with UnboundLocalError if uncommented before `x = 20`
    local_x = x + 5  # Reading without rebinding is fine
    return local_x

print(f"\nSafe read from global: {faulty_increment()}")