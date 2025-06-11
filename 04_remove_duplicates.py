"""
04_remove_duplicates.py

Problem Statement:
Remove duplicates from a list.

Steps:
1. Create a list with duplicate values.
2. Convert the list to a set and back to list.
3. Print the unique list.
"""

lst = [1, 2, 2, 3, 4, 4, 5]
unique_lst = list(set(lst))
print("List without duplicates:", unique_lst)