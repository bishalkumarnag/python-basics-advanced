"""
================================================================================
TOPIC: Consuming Python Packages & Relative vs Absolute Imports
================================================================================
SHORT THEORY:
- Consuming packages requires ensuring that the parent folder containing the 
  package directory is present on Python's `sys.path`.
- Absolute imports: `from shapes import circle` or `import shapes.circle` (Preferred).
- Relative imports: `from . import submodule` (used exclusively INSIDE package files).

SYNTAX REFERENCE:
    from package_name import submodule
    from package_name.submodule import function_name
================================================================================
"""

import sys
import os

# Ensure the package's parent folder is in the search path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from shapes import circle

radius = 7.0
print(f"--- Computing circle metrics for radius = {radius} ---")
print(f"Area:      {circle.area(radius)}")
print(f"Perimeter: {circle.perimeter(radius)}")