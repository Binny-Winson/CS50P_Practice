import re

name = input("What's your name? ").strip()

if matches := re.search(r"^(.+), ?(.+)$", name):
    print("Hello, " + matches.group(2) + " " + matches.group(1))