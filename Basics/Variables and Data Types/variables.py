"""
================================================================================
TOPIC: Variables & Assignment in Python
================================================================================
SHORT THEORY:
- A variable is a named reference/pointer to an object stored in memory.
- Python is dynamically typed: variable types do not need to be explicitly 
  declared; type is bound at runtime based on the value assigned.
- Python variables are case-sensitive and must start with a letter (a-z, A-Z)
  or an underscore (_), followed by letters, numbers, or underscores.
- Python allows multiple assignment, value unpacking, and dynamic reassignment.

SYNTAX REFERENCE:
    variable_name = value
    var1, var2 = val1, val2          # Multiple assignment
    x = y = z = 0                    # Chained assignment
    type(variable_name)              # Check data type at runtime
    id(variable_name)                # Memory address of the referenced object

KEY TAKEAWAYS / PITFALLS:
- Keywords (e.g., `for`, `class`, `def`) cannot be used as variable names.
- Assigning `b = a` points `b` to the same object as `a`.
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

# Example 1: Basic Variable Declarations
name = "Rahul"        # str (string)
age = 21              # int (integer)
gpa = 8.5             # float (floating-point number)
is_student = True     # bool (boolean)

print(f"Name: {name}, Age: {age}, GPA: {gpa}, Student: {is_student}")
# Output: Name: Rahul, Age: 21, GPA: 8.5, Student: True

# Example 2: Inspecting Types and Memory IDs
print(type(name))        # Output: <class 'str'>
print(type(age))         # Output: <class 'int'>
print(type(gpa))         # Output: <class 'float'>
print(type(is_student))  # Output: <class 'bool'>
print(f"Memory address of age: {id(age)}")

# Example 3: Multiple Assignment & Swapping Variables (Pythonic Way)
x, y, city = 10, 20, "Bengaluru"
print(f"x={x}, y={y}, city={city}")  # Output: x=10, y=20, city=Bengaluru

# Swapping without a temporary third variable
x, y = y, x
print(f"After swap: x={x}, y={y}")  # Output: After swap: x=20, y=10

# Example 4: Chained Assignment
a = b = c = 100
print(f"a={a}, b={b}, c={c}")  # Output: a=100, b=100, c=100

# Example 5: Dynamic Reassignment (Type Mutation of Variable Name)
data = 42
print(f"data is {type(data)}")  # Output: <class 'int'>
data = "Now I am a string"
print(f"data is {type(data)}")  # Output: <class 'str'>