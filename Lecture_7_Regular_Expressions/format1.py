import re

name = input("What's your name? ").strip()

matches = re.search(r"^(.+), ?(.+)$", name)

if matches:
    # last, first = matches.groups()
    # name = first + " " + last

# a better alternative would be to use matches.group() and combine the above two lines to one
    name = matches.group(2) + " " + matches.group(1)

print(f"Hello, {name}")
