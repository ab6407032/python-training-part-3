"""
11_line_counter.py

Problem Statement:
Count the number of lines in a text file.

Steps:
1. Open the file.
2. Use readlines() to get all lines.
3. Count and print number of lines.
"""

with open("sample.txt") as f:
    lines = f.readlines()
    print("Number of lines:", len(lines))