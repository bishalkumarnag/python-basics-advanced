"""
================================================================================
TOPIC: Pass by Object Reference: Immutable Objects ("Pass by Value" Illusion)
================================================================================
SHORT THEORY:
- Python uses "Call by Sharing" / "Pass by Object Reference".
- When an immutable object (e.g., `int`, `float`, `str`, `tuple`, `bool`, `frozenset`) 
  is passed to a function:
  1. The function parameter receives a reference to the same object in memory.
  2. Because the object is immutable, any modification operation (such as `x = x + 1` 
     or string concatenation) does NOT mutate the object in place.
  3. Instead, Python allocates a NEW object in memory and rebinds the local variable 
     name to point to it.
  4. The caller's original variable outside the function remains completely unaffected.
- This creates the exact behavioral appearance of "Pass by Value".

SYNTAX REFERENCE:
    def modify_immutable(num: int, text: str):
        num += 10          # Rebinds local 'num' to new int object
        text += " World"   # Rebinds local 'text' to new str object

KEY TAKEAWAYS / PITFALLS:
- Use `id(obj)` to inspect the memory addresses and prove that rebinding occurred!
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

def attempt_increment(val: int) -> None:
    print(f"Inside function (before modification): val={val}, id={id(val)}")
    val = val + 1  # Rebinds local 'val' to a new integer object
    print(f"Inside function (after modification):  val={val}, id={id(val)}")


original_num = 100
print(f"Outside function (initial): original_num={original_num}, id={id(original_num)}")

attempt_increment(original_num)

print(f"Outside function (final):   original_num={original_num}, id={id(original_num)}")
# Notice: Outside value remains 100!


# Example 2: Strings and Tuples
def append_string(greeting: str, coordinates: tuple) -> None:
    greeting += " Everyone!"
    coordinates += (99.0,)
    print(f"Inside: greeting='{greeting}', coords={coordinates}")

msg = "Hello"
coords = (12.5, 45.8)
append_string(msg, coords)

print(f"Outside: msg='{msg}', coords={coords}")
# Both remain unchanged in caller scope