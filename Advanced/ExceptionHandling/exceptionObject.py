"""
================================================================================
TOPIC: Exception Objects, Inspecting Tracebacks, & Control Flow (else/finally)
================================================================================
SHORT THEORY:
- In Python, exceptions are standard class instances inheriting from `BaseException`.
- Capturing `as e` binds the exception instance to variable `e`:
  - `str(e)`: Human-readable error message.
  - `type(e).__name__`: The exact class name of the exception.
  - `e.args`: Tuple of arguments passed during exception instantiation.
- The `else` block executes only if no exception occurred in `try`.
- The `finally` block ALWAYS executes, guaranteed even across `return`, `break`, or unhandled errors.

SYNTAX REFERENCE:
    except SpecificException as e:
        print(e.args)
        print(type(e).__name__)

KEY TAKEAWAYS / PITFALLS:
- If a `return` statement exists inside both `try` and `finally`, the `finally` block's 
  return statement will OVERWRITE the `try` block's return value!
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

# Example 1: Inspecting Exception Object Attributes
def inspect_exception_properties():
    try:
        data = {"status": "success"}
        print(data["missing_key"])  # Raises KeyError
    except KeyError as err:
        print("--- Exception Object Inspection ---")
        print(f"Error message:      {err}")
        print(f"Exception Class:    {type(err)}")
        print(f"Class Name:         {type(err).__name__}")
        print(f"Arguments (args):   {err.args}")
        print(f"Is instance of Exception? {isinstance(err, Exception)}")

inspect_exception_properties()


# Example 2: Complete Flow: try -> except -> else -> finally
def file_workflow_simulation(should_fail: bool = False):
    print("\n--- Workflow Simulation ---")
    resource_acquired = False
    try:
        print("1. [TRY]: Acquiring resource...")
        resource_acquired = True
        if should_fail:
            raise RuntimeError("Network interrupted while streaming data!")
        print("2. [TRY]: Data processing finished.")
    except RuntimeError as e:
        print(f"3. [EXCEPT]: Caught runtime failure: {e}")
    else:
        print("4. [ELSE]: Executed because TRY had ZERO errors.")
    finally:
        print("5. [FINALLY]: Cleaning up and releasing resource.")
        if resource_acquired:
            resource_acquired = False
            print("   -> Resource cleanly released.")


file_workflow_simulation(should_fail=False)
file_workflow_simulation(should_fail=True)


# Example 3: The Return Value in Finally Gotcha
def tricky_finally() -> str:
    try:
        return "FROM_TRY"
    finally:
        # Warning: Overrides return value from try!
        return "FROM_FINALLY"

print(f"\nTricky return result: {tricky_finally()}")  # Outputs: FROM_FINALLY