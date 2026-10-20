import csv
import os
import sys

from tabulate import tabulate

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

elif not os.path.isfile(sys.argv[1]):
    sys.exit("File does not exist")

elif sys.argv[1][-4:] != ".csv":
    sys.exit("Not a CSV file")

csv_file = sys.argv[1]

with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    print(tabulate(reader, tablefmt="grid"))