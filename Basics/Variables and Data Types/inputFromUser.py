"""
================================================================================
TOPIC: User Input & Standard I/O in Python
================================================================================
SHORT THEORY:
- The built-in `input([prompt])` function pauses program execution and waits 
  for the user to type text and press Enter.
- `input()` ALWAYS returns a string (`str`), regardless of whether the user typed 
  numbers, text, or symbols.
- To use the input as an integer, float, or list, explicit type conversion is required.

SYNTAX REFERENCE:
    user_string = input("Enter prompt: ")
    user_int = int(input("Enter integer: "))
    user_float = float(input("Enter decimal: "))
    multiple_values = input().split()        # Splits by space into list of strings
    numbers = list(map(int, input().split())) # Reads space-separated integers

KEY TAKEAWAYS / PITFALLS:
- Never assume user input is valid; wrap `int(input())` in `try...except ValueError`
  to handle malformed input gracefully in production code.
- In automated test environments or scripts without a terminal, `input()` will raise
  an `EOFError` if stdin is closed.
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

# Example 1: Standard Single Input (Demonstration)
def demonstrate_single_input():
    # Prompting the user
    # sample_name = input("Enter your name: ")
    sample_name = "Alex"  # Simulated default for non-interactive execution
    print(f"Hello, {sample_name}! Type: {type(sample_name)}")


# Example 2: Numeric Input with Safe Casting
def get_safe_integer(user_input_str: str) -> int:
    """Safely parse integer inputs without crashing."""
    try:
        val = int(user_input_str)
        return val
    except ValueError:
        print(f"Warning: '{user_input_str}' is not a valid integer. Defaulting to 0.")
        return 0


# Example 3: Parsing Space-Separated Multi-Inputs (Common in competitive programming)
simulated_cli_input = "10 20 30 40 50"
# Splitting by whitespace and mapping each token to int
parsed_integers = list(map(int, simulated_cli_input.split()))
print(f"Parsed numbers: {parsed_integers}")
print(f"Sum of numbers: {sum(parsed_integers)}")

# Example 4: Unpacking Multiple Inputs Directly
coords_input = "15 25"
x_str, y_str = coords_input.split()
x, y = int(x_str), int(y_str)
print(f"Point coordinates: x={x}, y={y}")

if __name__ == "__main__":
    demonstrate_single_input()
    print("Safe int parse (valid):", get_safe_integer("42"))
    print("Safe int parse (invalid):", get_safe_integer("abc"))