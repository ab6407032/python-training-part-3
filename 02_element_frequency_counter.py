"""
02_element_frequency_counter.py

Problem Statement:
Count the frequency of each element in a list.

Steps:
1. Create a list with duplicate elements.
2. Use a dictionary to count occurrences.
3. Print the frequency dictionary.
"""

lst = ['a', 'b', 'a', 'c', 'b', 'a']
freq = {}

for item in lst:
    freq[item] = freq.get(item, 0) + 1

print("Element Frequencies:", freq)