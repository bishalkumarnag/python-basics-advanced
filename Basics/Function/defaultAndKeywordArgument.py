"""
================================================================================
TOPIC: Default, Keyword, Positional-Only, & Keyword-Only Arguments
================================================================================
SHORT THEORY:
- Positional Arguments: Arguments passed to a function in correct positional order.
- Keyword Arguments: Arguments identified by parameter name during call (`func(age=25)`).
- Default Arguments: Parameters initialized with default fallback values.
  If not supplied by caller, default is used.
- Positional-only (`/`): Enforces that parameters before `/` MUST be passed positionally.
- Keyword-only (`*`): Enforces that parameters after `*` MUST be passed by keyword.

SYNTAX REFERENCE:
    def func(pos1, /, standard, *, kw_only=default):
        ...

KEY TAKEAWAYS / PITFALLS:
- CRITICAL BUG WARNING: NEVER use mutable objects (`[]`, `{}`) as default argument values!
  Default parameter values are evaluated ONCE at function definition time, NOT at call time.
  Always use `None` as default, then initialize inside: `if lst is None: lst = []`.
- Positional arguments must ALWAYS come before keyword arguments in a call.
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

# Example 1: Default & Keyword Arguments
def calculate_grade(maths: int, hindi: int, english: int = 50) -> float:
    """Calculates average mark, with English defaulting to 50 if unspecified."""
    total = maths + hindi + english
    return round(total / 3, 2)

# Calling positionally
print("1. Default value used:", calculate_grade(75, 85))

# Calling with keyword arguments in arbitrary order
print("2. Keyword arguments:", calculate_grade(english=80, maths=90, hindi=70))

# Mixing positional and keyword (positional must come first)
print("3. Mixed call:", calculate_grade(85, english=95, hindi=65))


# Example 2: THE MUTABLE DEFAULT ARGUMENT TRAP (Common Interview Gotcha)
# BAD PRACTICE:
def append_to_bad(item, target_list=[]):
    target_list.append(item)
    return target_list

print("\nBad mutable default behavior:")
print(append_to_bad(1))  # [1]
print(append_to_bad(2))  # [1, 2] -- The list persisted across calls!

# PYTHONIC CORRECT PRACTICE:
def append_to_good(item, target_list=None):
    if target_list is None:
        target_list = []
    target_list.append(item)
    return target_list

print("\nCorrected default behavior:")
print(append_to_good(1))  # [1]
print(append_to_good(2))  # [2] -- Fresh list each call!


# Example 3: Positional-Only (/) and Keyword-Only (*) Parameters (Python 3.8+)
def configure_server(host: str, port: int, /, *, timeout: int = 30, debug: bool = False):
    """
    host and port: MUST be positional (before /)
    timeout and debug: MUST be keyword-only (after *)
    """
    return f"Connecting to {host}:{port} (timeout={timeout}s, debug={debug})"

# Valid call:
print("\nPositional-only & Keyword-only syntax:")
print(configure_server("127.0.0.1", 8080, timeout=60, debug=True))
# configure_server(host="127.0.0.1", port=8080) -> Raises TypeError!
