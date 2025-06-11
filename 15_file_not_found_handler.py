"""
15_file_not_found_handler.py

Problem Statement:
Handle missing file error using exception handling.

Steps:
1. Try to open a non-existent file.
2. Catch FileNotFoundError and print message.
"""

try:
    with open("nofile.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found.")