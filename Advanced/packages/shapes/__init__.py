"""
================================================================================
PACKAGE: shapes
================================================================================
SHORT THEORY:
- A Python package is simply a directory containing an `__init__.py` file (and submodules).
- The `__init__.py` file initializes the package when imported.
- It can:
  1. Execute package-level setup.
  2. Expose specific submodule symbols to elevate the public API.
  3. Define `__all__` to restrict what `from shapes import *` exposes.

SYNTAX REFERENCE:
    __all__ = ["circle"]
================================================================================
"""

from . import circle

__all__ = ["circle"]
