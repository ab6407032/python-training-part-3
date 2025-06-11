"""
14_invalid_input.py

Problem Statement:
Handle invalid input using exception handling.

Steps:
1. Ask user for number input.
2. Use try-except to catch ValueError.
"""

try:
    number = int(input("Enter a number: "))
    print("You entered:", number)
except ValueError:
    print("Invalid input. Not a number.")