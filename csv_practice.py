# ISM2411 Lab 12 — Read a Sales CSV, Write a Cleaned Report
# Name: Mateo Urrea
# Run from the ism2411-lab12 folder:  python3 csv_practice.py

import csv
import os

SALES_FILE = "data/sales.csv"
CLEANED_FILE = "data/cleaned.csv"
LOG_FILE = "data/run_log.txt"

# ---------------------------------------------------------------
# Exercise 1 · Get the file
# ---------------------------------------------------------------
print("=== Exercise 1: Get the file ===")
print(f"{SALES_FILE} exists: {os.path.exists(SALES_FILE)}")
with open(SALES_FILE, "r") as f:
    line_count = len(f.readlines())
print(f"Lines in file (header + data): {line_count}")
print()

# ---------------------------------------------------------------
# Exercise 2 · Read and print raw rows
# ---------------------------------------------------------------
print("=== Exercise 2: Raw rows ===")
with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)  # every value is a string, e.g. ['Widget A', '9.99', '50']
print()

# ---------------------------------------------------------------
# Exercise 3 · Skip the header
# ---------------------------------------------------------------
print("=== Exercise 3: Skip the header ===")
with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    print("Header:", header)
    for row in reader:
        print(row)
print()
