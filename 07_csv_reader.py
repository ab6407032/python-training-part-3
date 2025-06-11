"""
07_csv_reader.py

Problem Statement:
Read data from a CSV file.

Steps:
1. Import csv module.
2. Open and read the CSV file.
3. Print each row.
"""

import csv

with open("data.csv", newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)