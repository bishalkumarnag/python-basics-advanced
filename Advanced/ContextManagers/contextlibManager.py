"""
================================================================================
TOPIC: @contextlib.contextmanager (Generator-Based Context Managers)
================================================================================
SHORT THEORY:
- Writing class-based context managers with `__enter__` and `__exit__` can be verbose.
- The `contextlib` standard library provides the `@contextmanager` decorator, 
  which turns a simple generator function into a full context manager!
- How it works:
  1. Code before `yield`: Executes on entering the `with` block (Setup / `__enter__`).
  2. The value yielded by `yield`: Bound to the `as target` variable.
  3. Code in `finally` after `yield`: Executes on exiting the `with` block (Teardown / `__exit__`).

SYNTAX REFERENCE:
    from contextlib import contextmanager

    @contextmanager
    def manage_resource():
        # Setup
        resource = acquire()
        try:
            yield resource
        finally:
            # Teardown
            release(resource)

KEY TAKEAWAYS / PITFALLS:
- ALWAYS wrap the `yield` statement in a `try...finally` block. 
  If an exception occurs inside the user's `with` block, the `finally` block guarantees 
  that cleanup code runs!
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

from contextlib import contextmanager
import os

# Example 1: Temporary Working Directory Switcher
@contextmanager
def temporary_working_directory(target_path: str):
    """Safely switches current working directory and reverts back on exit."""
    previous_directory = os.getcwd()
    print(f"[CD]: Switching from '{previous_directory}' to '{target_path}'")
    os.chdir(target_path)
    try:
        yield target_path
    finally:
        print(f"[CD]: Reverting working directory back to '{previous_directory}'")
        os.chdir(previous_directory)


with temporary_working_directory("/tmp") as current_tmp:
    print(f"  Inside context: active cwd is {os.getcwd()}")

print(f"Outside context: restored cwd is {os.getcwd()}")


# Example 2: Temporary Flag Modifier (e.g., debug mode)
class AppConfig:
    debug_mode = False

@contextmanager
def temporary_debug_mode(config: AppConfig):
    original_state = config.debug_mode
    config.debug_mode = True
    print("\n[CONFIG]: Debug mode ENABLED.")
    try:
        yield config
    finally:
        config.debug_mode = original_state
        print("[CONFIG]: Debug mode reverted to original state.")


cfg = AppConfig()
print(f"Initial debug: {cfg.debug_mode}")

with temporary_debug_mode(cfg):
    print(f"  Processing request with verbose traces: debug={cfg.debug_mode}")

print(f"Post context debug: {cfg.debug_mode}")
