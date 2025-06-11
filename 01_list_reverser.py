"""
01_list_reverser.py

Problem Statement:
Write a program to reverse a list using slicing.

Steps:
1. Define a list with elements.
2. Use slicing [::-1] to reverse the list.
3. Print the original and reversed list.
"""

lst = [1, 2, 3, 4, 5]
reversed_lst = lst[::-1]

print("Original List:", lst)
print("Reversed List:", reversed_lst)