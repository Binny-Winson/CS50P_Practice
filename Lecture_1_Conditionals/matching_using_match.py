name = input("What's your name? ")

"""
match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
"""

# further improving the above code by using the logical operator 'or', we can also use the single vertical bar | as 'or' in python

match name:
    case "Harry" | "Hernione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Syltherin")
    case _:
        print("Who?")