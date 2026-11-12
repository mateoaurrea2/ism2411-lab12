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

# ---------------------------------------------------------------
# Exercise 4 · Compute totals
# ---------------------------------------------------------------
print("=== Exercise 4: Compute totals ===")
total_revenue = 0
with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])
        line_total = price * quantity
        total_revenue += line_total
        print(f"{product}: {quantity} units × ${price:.2f} = ${line_total:.2f}")
print(f"Total revenue: ${total_revenue:.2f}")
print()

# ---------------------------------------------------------------
# Exercise 5 · Filter and write
# ---------------------------------------------------------------
print("=== Exercise 5: Filter and write ===")
original_count = 0
written_count = 0
with open(SALES_FILE, "r") as infile, open(CLEANED_FILE, "w", newline="") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    next(reader)  # skip header
    writer.writerow(["Product", "Price", "Qty", "Total"])
    for row in reader:
        original_count += 1
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])
        line_total = price * quantity
        if line_total > 100:
            writer.writerow([product, f"{price:.2f}", quantity, f"{line_total:.2f}"])
            written_count += 1
print(f"Wrote {written_count} of {original_count} rows to {CLEANED_FILE} (orders > $100)")
print()
