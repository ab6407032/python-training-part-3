"""
08_word_counter.py

Problem Statement:
Count the number of words in a sentence.

Steps:
1. Split the input sentence by spaces.
2. Count and print the number of words.
"""

text = "This is a test sentence."
words = text.split()
print("Number of words:", len(words))