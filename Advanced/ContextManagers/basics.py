"""
================================================================================
TOPIC: Custom Context Managers (__enter__ and __exit__)
================================================================================
SHORT THEORY:
- Context Managers manage resources safely using the `with` statement (RAII pattern).
- Guarantee that setup and teardown actions are always performed, even if exceptions occur.
- An object becomes a Context Manager by implementing the context management protocol:
  1. `__enter__(self)`: Prepares the resource. Its return value is bound to the `as variable`.
  2. `__exit__(self, exc_type, exc_val, exc_tb)`: Cleans up the resource.
- Exception Handling in `__exit__`:
  - If `__exit__` returns `True`, Python suppresses the exception that occurred inside the `with` block!
  - If `__exit__` returns `False` (or `None`), the exception propagates normally.

SYNTAX REFERENCE:
    class ManagedResource:
        def __enter__(self):
            # setup resource
            return resource

        def __exit__(self, exc_type, exc_val, exc_tb):
            # cleanup resource
            return False # True suppresses exception

    with ManagedResource() as res:
        ...

KEY TAKEAWAYS / PITFALLS:
- Returning `True` from `__exit__` swallows all exceptions; ensure you only return `True` 
  for exceptions you deliberately intend to catch and handle.
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

import time

# Example 1: Execution Timer Context Manager
class ExecutionTimer:
    def __init__(self, description: str) -> None:
        self.description = description
        self.start_time = 0.0

    def __enter__(self):
        print(f"[{self.description}] Started timer...")
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.perf_counter() - self.start_time
        print(f"[{self.description}] Finished in {elapsed:.6f} seconds.")
        # Return False to let any unexpected exception propagate
        return False


with ExecutionTimer("Matrix Multiplication Simulation"):
    total = sum(i * i for i in range(500000))
    print(f"  Calculation complete. Total: {total}")


# Example 2: Database Connection Session with Auto-Rollback on Error
class MockDatabaseSession:
    def __init__(self, db_name: str) -> None:
        self.db_name = db_name

    def __enter__(self):
        print(f"\n[DB]: Connecting to '{self.db_name}' and beginning transaction...")
        return self

    def query(self, sql: str) -> None:
        print(f"  [EXEC]: {sql}")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f"[DB]: Exception detected ({exc_val}). Rolling back transaction!")
            # Suppress exception for graceful handling: return True
            return True
        print("[DB]: Transaction committed successfully. Closing connection.")
        return False


# Success scenario:
with MockDatabaseSession("ProductionDB") as session:
    session.query("INSERT INTO users (name) VALUES ('Bishal');")

# Failure scenario (Error suppressed and rolled back):
with MockDatabaseSession("ProductionDB") as session:
    session.query("INSERT INTO orders (id) VALUES (101);")
    raise ValueError("Inventory check failed during order placement!")

print("Program continued smoothly after context manager handled rollback!")
