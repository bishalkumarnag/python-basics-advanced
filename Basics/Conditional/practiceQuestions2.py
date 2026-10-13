"""
================================================================================
PRACTICE QUESTIONS: Conditionals & Logic
================================================================================
This module contains solved problems with complete logic and test runs.
================================================================================
"""

# ==============================================================================
# PROBLEM 1: Number Sign Checker
# Description: Write a function that determines whether a number is positive, 
# negative, or zero.
# ==============================================================================
def check_number_sign(n: float) -> str:
    if n > 0:
        return "POSITIVE"
    elif n < 0:
        return "NEGATIVE"
    else:
        return "ZERO"

# Solved Test Cases:
print("--- Problem 1 Test Cases ---")
print(f"10 -> {check_number_sign(10)}")      # POSITIVE
print(f"-5 -> {check_number_sign(-5)}")      # NEGATIVE
print(f" 0 -> {check_number_sign(0)}")       # ZERO


# ==============================================================================
# PROBLEM 2: Compare Two Numbers
# Description: Given two numbers, return the greater one or state equality.
# ==============================================================================
def compare_two_numbers(a: int, b: int) -> str:
    if a == b:
        return f"Both numbers are equal ({a})"
    elif a > b:
        return f"{a} is greater than {b}"
    else:
        return f"{b} is greater than {a}"

print("\n--- Problem 2 Test Cases ---")
print(compare_two_numbers(15, 20))
print(compare_two_numbers(50, 50))


# ==============================================================================
# PROBLEM 3: Leap Year Checker
# Rule: A year is a leap year if:
# - It is divisible by 4 AND NOT divisible by 100, OR
# - It is divisible by 400.
# ==============================================================================
def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print("\n--- Problem 3 Test Cases ---")
test_years = [2000, 2020, 2024, 1900, 2023]
for y in test_years:
    status = "LEAP YEAR" if is_leap_year(y) else "NOT LEAP YEAR"
    print(f"Year {y}: {status}")


# ==============================================================================
# PROBLEM 4: E-Commerce Discount Calculator
# Rule:
# - Bill >= 1000: 20% discount
# - Bill >= 500:  10% discount
# - Premium member gets an extra 5% discount on remaining amount
# ==============================================================================
def calculate_final_bill(amount: float, is_premium: bool = False) -> float:
    if amount >= 1000:
        discount = 0.20
    elif amount >= 500:
        discount = 0.10
    else:
        discount = 0.00
    
    discounted_amount = amount * (1 - discount)
    if is_premium:
        discounted_amount *= 0.95  # Extra 5% off
    return round(discounted_amount, 2)

print("\n--- Problem 4 Test Cases ---")
print(f"Regular $1200: ${calculate_final_bill(1200, False)}")   # $960.0
print(f"Premium $1200: ${calculate_final_bill(1200, True)}")    # $912.0
print(f"Regular $300:  ${calculate_final_bill(300, False)}")    # $300.0