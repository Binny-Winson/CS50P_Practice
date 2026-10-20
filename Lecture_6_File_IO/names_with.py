# The keyword with allows you to automate the  closing of a file.

name = input("What's your name? ")

with open("names_with.txt", "a") as file:
    file.write(f"{name}\n")