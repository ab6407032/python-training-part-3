"""
05_word_frequency_counter.py

Problem Statement:
Count frequency of each word in a string.

Steps:
1. Define a text string.
2. Split it into words.
3. Use a dictionary to count occurrences.
4. Print the word frequencies.
"""

text = "hello world hello again world"
words = text.split()
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print("Word Frequencies:", freq)