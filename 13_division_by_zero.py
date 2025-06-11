"""
13_division_by_zero.py

Problem Statement:
Catch and handle division by zero error.

Steps:
1. Attempt a division by zero.
2. Catch and print appropriate message.
"""

try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")