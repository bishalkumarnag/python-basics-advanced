"""
================================================================================
TOPIC: *args & **kwargs (Variable-Length Arguments)
================================================================================
SHORT THEORY:
- `*args` (Positional variable arguments): Allows a function to accept an arbitrary
  number of positional arguments. Inside the function, `args` is accessed as a `tuple`.
- `**kwargs` (Keyword variable arguments): Allows a function to accept an arbitrary
  number of keyword arguments. Inside the function, `kwargs` is accessed as a `dict`.
- The `*` and `**` operators can also be used during function invocation to unpack
  iterables and dictionaries into function arguments.

SYNTAX REFERENCE:
    def func(*args, **kwargs):
        # args is a tuple: (arg1, arg2, ...)
        # kwargs is a dict: {'key1': val1, ...}

    # Order of parameters in signature:
    # 1. Positional -> 2. *args -> 3. Keyword-only -> 4. **kwargs

KEY TAKEAWAYS / PITFALLS:
- The names `args` and `kwargs` are conventions; the single `*` and double `**` 
  symbols do the actual unpacking.
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

# Example 1: Using *args for Variable Positional Arguments
def calculate_sum(*numbers: float) -> float:
    """Accepts any quantity of numbers and returns their total sum."""
    print(f"Received args tuple: {numbers}")
    return sum(numbers)

print(calculate_sum(1, 2))              # 3
print(calculate_sum(10, 20, 30, 40, 50)) # 150
print(calculate_sum())                  # 0


# Example 2: Using **kwargs for Variable Keyword Arguments
def build_user_profile(user_id: int, **attributes) -> dict:
    """Builds a user record accepting arbitrary profile attributes."""
    profile = {"id": user_id}
    profile.update(attributes)
    return profile

user = build_user_profile(101, username="bishal_nag", role="Developer", location="India", active=True)
print("\nConstructed Profile:")
for k, v in user.items():
    print(f"  {k}: {v}")


# Example 3: Combining Positional, *args, and **kwargs
def master_logger(level: str, *messages, **metadata):
    combined_msg = " | ".join(str(m) for m in messages)
    print(f"[{level.upper()}] {combined_msg}")
    if metadata:
        print(f"  Metadata: {metadata}")

master_logger("info", "Server started", "Listening on port 8000", timestamp="2026-10-13", environment="prod")


# Example 4: Unpacking Sequences and Dictionaries at Call Site
def connect(host, port, timeout):
    return f"Connected to {host}:{port} with timeout {timeout}s"

config_tuple = ("db.internal", 5432, 10)
print("\nUnpacking tuple with *:", connect(*config_tuple))

config_dict = {"host": "cache.internal", "port": 6379, "timeout": 5}
print("Unpacking dict with **:", connect(**config_dict))
