"""
10_write_read_file.py

Problem Statement:
Write content to a file and read it back.

Steps:
1. Open file in write mode and add lines.
2. Reopen in read mode and display content.
"""

with open("notes.txt", "w") as f:
    f.write("Line one\nLine two\n")

with open("notes.txt") as f:
    print(f.read())