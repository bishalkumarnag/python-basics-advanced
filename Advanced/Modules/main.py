"""
================================================================================
TOPIC: Importing Modules (import, from ... import ..., as alias)
================================================================================
SHORT THEORY:
- Modules are loaded using the `import` statement.
- Python search path for modules (`sys.path`):
  1. The directory containing the input script.
  2. PYTHONPATH environment variable directories.
  3. Standard library directories.
  4. Installed site-packages (pip libraries).
- Forms of Import:
  1. `import module_name`: Imports entire module into its own namespace.
  2. `from module_name import func1, func2`: Imports specific symbols directly.
  3. `import module_name as alias`: Imports with alias (e.g., `import numpy as np`).
  4. `from module_name import *`: Wildcard import (Anti-pattern: pollutes namespace).

SYNTAX REFERENCE:
    import module_name
    from module_name import specific_func as alias_func
    import sys; print(sys.path)

KEY TAKEAWAYS / PITFALLS:
- Avoid circular imports (Module A imports Module B, and Module B imports Module A).
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

import sys
import os

# Ensure local module directory is in sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Form 1: Standard import
import calculator

# Form 2: Direct symbol import with alias
from calculator import add as calc_sum, PI

print("1. Accessing via module namespace:")
print(f"   calculator.multiply(6, 7) = {calculator.multiply(6, 7)}")
print(f"   calculator.PI             = {calculator.PI}")

print("\n2. Accessing via imported alias:")
print(f"   calc_sum(100, 250)        = {calc_sum(100, 250)}")
print(f"   PI directly               = {PI}")

# Demonstrating sys.path inspection
print("\nFirst entry of Python module search path (sys.path[0]):")
print(f"   {sys.path[0]}")