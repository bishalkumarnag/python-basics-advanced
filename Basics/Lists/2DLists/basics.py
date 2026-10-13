"""
================================================================================
TOPIC: 2D Lists (Matrices & Nested Lists) in Python
================================================================================
SHORT THEORY:
- A 2D list is a list whose elements are themselves lists (nested lists).
- Commonly used to represent tables, grids, boards, and mathematical matrices.
- Row-major format: `matrix[row_index][column_index]`.
- CRITICAL INITIALIZATION TRAP: Never initialize a 2D matrix using `[[0] * cols] * rows`.
  The multiplication operator shallow-copies the inner list reference, meaning 
  modifying one row will inadvertently modify all rows!
  Always initialize using list comprehension: `[[0 for _ in range(cols)] for _ in range(rows)]`.

SYNTAX REFERENCE:
    matrix = [[1, 2], [3, 4]]
    matrix[r][c]              # Access element at row r, column c
    len(matrix)               # Number of rows
    len(matrix[0])            # Number of columns

KEY TAKEAWAYS / PITFALLS:
- `[[0] * 3] * 3` creates 3 references pointing to the EXACT SAME list in memory!
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

# Example 1: Traversal and Printing of a Matrix
grid = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

rows = len(grid)
cols = len(grid[0])

print("Traversing 3x3 Matrix:")
for r in range(rows):
    for c in range(cols):
        print(f"{grid[r][c]:>4}", end=" ")
    print()


# Example 2: The Shallow Copy Matrix Trap vs Safe Initialization
print("\nDemonstrating the Initialization Trap:")
# WRONG WAY:
flawed_matrix = [[0] * 3] * 3
flawed_matrix[0][0] = 99
print("Flawed initialization output (all rows affected):")
print(flawed_matrix)  # [[99, 0, 0], [99, 0, 0], [99, 0, 0]]

# CORRECT PYTHONIC WAY (List Comprehension):
safe_matrix = [[0 for _ in range(3)] for _ in range(3)]
safe_matrix[0][0] = 99
print("Correct initialization output (only row 0 affected):")
print(safe_matrix)    # [[99, 0, 0], [0, 0, 0], [0, 0, 0]]


# Example 3: Matrix Transposition (Swapping Rows and Columns)
matrix_a = [
    [1, 2, 3],
    [4, 5, 6]
]
# Transpose using zip(*matrix)
transposed = [list(col) for col in zip(*matrix_a)]
print(f"\nOriginal: {matrix_a}")
print(f"Transposed: {transposed}")


# Example 4: Flattening a 2D Matrix to a 1D List
flattened = [val for row in grid for val in row]
print(f"\nFlattened grid: {flattened}")