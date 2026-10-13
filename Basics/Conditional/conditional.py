"""
================================================================================
TOPIC: Conditional Statements & Pattern Matching
================================================================================
SHORT THEORY:
- Conditionals execute specific blocks of code depending on whether a boolean
  expression evaluates to `True` or `False`.
- Python uses indentation (standard 4 spaces) to define code blocks (no curly braces `{}`).
- Constructs:
  1. `if`: Executes block if condition is True.
  2. `elif`: Evaluated only if preceding `if` and `elif` checks were False.
  3. `else`: Catch-all fallback executed when all preceding conditions are False.
  4. Ternary Expression: One-line conditional expression `value_if_true if condition else value_if_false`.
  5. Structural Pattern Matching (`match-case` introduced in Python 3.10+): 
     More expressive and powerful than traditional `switch-case`.

SYNTAX REFERENCE:
    if condition1:
        # block 1
    elif condition2:
        # block 2
    else:
        # fallback block

    variable = val_true if condition else val_false   # Ternary syntax

    match subject:
        case pattern1:
            ...
        case pattern2:
            ...
        case _:
            ... # default wildcard

KEY TAKEAWAYS / PITFALLS:
- Avoid redundant boolean checks: write `if is_active:` instead of `if is_active == True:`.
- Order matters in `if-elif`: conditions are evaluated sequentially from top to bottom.
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

# Example 1: if-elif-else Grading System
score = 85

if score >= 90:
    grade = "A+"
elif score >= 80:
    grade = "A"
elif score >= 70:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    grade = "Fail"

print(f"Score: {score} -> Grade: {grade}")  # Grade: A

# Example 2: Nested Conditionals (Eligibility & Category)
age = 65
has_citizenship = True

if has_citizenship:
    if age >= 60:
        status = "Eligible: Senior Citizen Benefits Apply"
    elif age >= 18:
        status = "Eligible: Standard Adult Voter"
    else:
        status = "Ineligible: Under 18"
else:
    status = "Ineligible: Non-citizen"

print(f"Citizen Status: {status}")

# Example 3: Ternary Operator (Inline Conditional Expression)
cart_total = 120
shipping_cost = 0.0 if cart_total >= 100 else 9.99
print(f"Cart: ${cart_total} | Shipping: ${shipping_cost:.2f}")

# Example 4: Structural Pattern Matching (Python 3.10+ match-case)
def handle_http_status(status_code: int) -> str:
    match status_code:
        case 200:
            return "OK: Request succeeded"
        case 301 | 302:
            return "Redirection: Resource moved"
        case 400:
            return "Bad Request: Malformed syntax"
        case 401 | 403:
            return "Unauthorized / Forbidden"
        case 404:
            return "Not Found: Resource missing"
        case 500 | 502 | 503:
            return "Server Error: Failure on upstream"
        case _:
            return f"Unknown status code: {status_code}"

print(handle_http_status(200))
print(handle_http_status(404))
print(handle_http_status(500))