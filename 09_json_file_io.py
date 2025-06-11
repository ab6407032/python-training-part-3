"""
09_json_file_io.py

Problem Statement:
Write data to a JSON file and read it back.

Steps:
1. Use the json module.
2. Write a dictionary to a file.
3. Read and print it.
"""

import json

data = {"name": "Alice", "age": 25}

# Write
with open("data.json", "w") as f:
    json.dump(data, f)

# Read
with open("data.json") as f:
    loaded = json.load(f)
    print("Loaded data:", loaded)