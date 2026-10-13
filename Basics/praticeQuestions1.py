"""
================================================================================
PRACTICE QUESTIONS SET 1: Fundamentals, Arithmetic, & Conditionals
================================================================================
"""

# ==============================================================================
# PROBLEM 1: Comprehensive Arithmetic Calculator
# Given two numbers, return their sum, difference, product, division, and modulo.
# ==============================================================================
def arithmetic_operations(num1: float, num2: float) -> dict[str, float]:
    results = {
        "sum": num1 + num2,
        "difference": num1 - num2,
        "product": num1 * num2,
        "division": num1 / num2 if num2 != 0 else float("inf"),
        "modulo": num1 % num2 if num2 != 0 else float("nan")
    }
    return results

print("--- Problem 1: Arithmetic Operations (15, 4) ---")
for op, val in arithmetic_operations(15, 4).items():
    print(f"  {op.capitalize()}: {val}")


# ==============================================================================
# PROBLEM 2: Even or Odd Checker
# ==============================================================================
def check_even_odd(n: int) -> str:
    return "EVEN" if n % 2 == 0 else "ODD"

print("\n--- Problem 2: Even or Odd ---")
print(f"14 -> {check_even_odd(14)}")
print(f"27 -> {check_even_odd(27)}")


# ==============================================================================
# PROBLEM 3: Voting & Senior Citizen Eligibility Checker
# ==============================================================================
def check_civic_status(age: int) -> str:
    if age >= 60:
        return "ELIGIBLE (SENIOR CITIZEN)"
    elif age >= 18:
        return "ELIGIBLE (ADULT)"
    else:
        return "NOT ELIGIBLE (MINOR)"

print("\n--- Problem 3: Civic Status ---")
print(f"Age 16 -> {check_civic_status(16)}")
print(f"Age 35 -> {check_civic_status(35)}")
print(f"Age 72 -> {check_civic_status(72)}")


# ==============================================================================
# PROBLEM 4: Total Sum and Average of 3 Numbers
# ==============================================================================
def sum_and_average(n1: float, n2: float, n3: float) -> tuple[float, float]:
    total = n1 + n2 + n3
    avg = total / 3
    return total, round(avg, 2)

print("\n--- Problem 4: Sum and Average ---")
tot, avg = sum_and_average(10, 25, 40)
print(f"Numbers: 10, 25, 40 -> Sum: {tot}, Average: {avg}")