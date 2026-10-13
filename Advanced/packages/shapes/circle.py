"""
================================================================================
SUBMODULE: shapes.circle
================================================================================
SHORT THEORY:
- A submodule represents a specialized domain file inside a package directory.
- This module provides geometric calculations for circular shapes.
================================================================================
"""

import math

def area(radius: float) -> float:
    """Calculates surface area of a circle with radius r."""
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return round(math.pi * (radius ** 2), 2)


def perimeter(radius: float) -> float:
    """Calculates circumference/perimeter of a circle with radius r."""
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return round(2 * math.pi * radius, 2)