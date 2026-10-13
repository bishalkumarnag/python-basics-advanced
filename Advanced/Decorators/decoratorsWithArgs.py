"""
================================================================================
TOPIC: Decorators with Arguments (Decorator Factories) & Chaining
================================================================================
SHORT THEORY:
- Standard decorators only take `func` as an argument (`@my_dec`).
- If you want a decorator to accept configuration parameters (e.g., `@repeat(num_times=3)` 
  or `@retry(max_attempts=5)`), you must create a Decorator Factory.
- A Decorator Factory requires THREE levels of nested functions:
  1. Outer function: Accepts decorator configuration arguments and returns the decorator.
  2. Middle function: Accepts the target `func` and returns the wrapper.
  3. Inner wrapper: Accepts `*args, **kwargs`, executes target, and returns result.
- Decorator Stacking (Chaining): Multiple decorators can be stacked on top of a single 
  function. They execute from the BOTTOM UP (innermost first).

SYNTAX REFERENCE:
    def repeat(times):
        def decorator(func):
            def wrapper(*args, **kwargs):
                for _ in range(times):
                    res = func(*args, **kwargs)
                return res
            return wrapper
        return decorator

    @dec1
    @dec2
    def my_func(): ...  # Equivalent to: my_func = dec1(dec2(my_func))

KEY TAKEAWAYS / PITFALLS:
- Stacking order matters: `@dec1 \n @dec2 \n def f()` runs `dec2` closest to `f`, 
  then wraps the result with `dec1`.
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

# Example 1: Decorator Factory with Arguments (@repeat)
def repeat(times: int):
    """Executes the decorated function 'times' times."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            last_result = None
            for i in range(1, times + 1):
                print(f"[Iteration #{i}/{times}]:")
                last_result = func(*args, **kwargs)
            return last_result
        return wrapper
    return decorator


@repeat(times=3)
def send_ping(host: str) -> str:
    print(f"  Pinging {host}... [ACK]")
    return "OK"

send_ping("192.168.1.1")


# Example 2: Stacking Multiple Decorators
def make_bold(func):
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper

def make_italic(func):
    def wrapper(*args, **kwargs):
        return f"<i>{func(*args, **kwargs)}</i>"
    return wrapper


@make_bold
@make_italic
def format_announcement(msg: str) -> str:
    return msg

# Executed as: make_bold(make_italic(format_announcement))
print(f"\nStacked HTML formatting: {format_announcement('Important System Update')}")
# Output: <b><i>Important System Update</i></b>
