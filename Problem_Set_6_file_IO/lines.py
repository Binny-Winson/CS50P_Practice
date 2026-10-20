import os
import sys

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

elif sys.argv[1][-3:] != '.py':
    sys.exit("Not a Python file")

elif not os.path.isfile(sys.argv[1]):
    sys.exit("File does not exist")

python_file = sys.argv[1]

with open(python_file, "r") as file:
    number_of_lines = 0
    for line in file:
        if line.strip() == "" or line.strip().startswith(("#", '"""', "'''")):
            continue
        else:
            number_of_lines += 1
    print(number_of_lines)
