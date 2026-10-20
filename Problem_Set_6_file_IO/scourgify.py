import csv
import os
import sys

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

if sys.argv[1][-4:] != ".csv":
    sys.exit(f"Could not read {sys.argv[1]}")

if not os.path.isfile(sys.argv[1]):
    sys.exit(f"{sys.argv[1]} not found")

original_csv = sys.argv[1]
sorted_csv = sys.argv[2]

with open(original_csv, 'r') as file, open(sorted_csv, 'w', newline="") as file_1:
    reader = csv.DictReader(file)
    fieldnames = ['first_name', 'last_name', 'house']
    writer = csv.DictWriter(file_1, fieldnames=fieldnames)
    writer.writeheader()

    for line in reader:
        last_name, first_name = line['name'].split(", ")
        house = line['house']
        writer.writerow({'first_name': first_name, 'last_name': last_name, 'house': house})