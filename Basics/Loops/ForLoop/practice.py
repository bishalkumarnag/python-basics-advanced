"""
================================================================================
PRACTICE QUESTIONS: For Loops & Iteration
================================================================================
"""

# ==============================================================================
# PROBLEM 1: Element-wise Sum of Two Lists
# Given two equal-length lists, return a new list containing the sum of elements
# at each corresponding index.
# ==============================================================================
def elementwise_sum(list1: list[int], list2: list[int]) -> list[int]:
    # Method 1: Using zip (Pythonic)
    return [a + b for a, b in zip(list1, list2)]

nums1 = [1, 2, 3, 45, 6]
nums2 = [-1, 9, 0, 10, 11]
print("Problem 1: Element-wise sum:")
print(f"{nums1} + {nums2} = {elementwise_sum(nums1, nums2)}")


# ==============================================================================
# PROBLEM 2: Prime Number Checker
# Check if an integer n > 1 is prime using a for loop with early break.
# ==============================================================================
def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    # Check divisors up to square root of n
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            return False
    return True

print("\nProblem 2: Prime verification:")
test_nums = [2, 3, 4, 17, 25, 29, 31, 35]
for val in test_nums:
    print(f"Is {val} prime? {is_prime(val)}")


# ==============================================================================
# PROBLEM 3: Matrix Row and Column Sums
# Given a 2D matrix, calculate the sum of each row and each column.
# ==============================================================================
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("\nProblem 3: Matrix Sums:")
for r_idx, row in enumerate(matrix):
    print(f"Row {r_idx} sum: {sum(row)}")

col_sums = [sum(matrix[r][c] for r in range(len(matrix))) for c in range(len(matrix[0]))]
print(f"Column sums: {col_sums}")