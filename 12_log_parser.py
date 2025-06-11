"""
12_log_parser.py

Problem Statement:
Count the number of lines containing 'ERROR' in a log file.

Steps:
1. Read each line of the log file.
2. Check if 'ERROR' is in the line.
3. Count how many such lines exist.
"""

with open("log.txt") as f:
    errors = [line for line in f if "ERROR" in line]

print("Number of ERROR lines:", len(errors))