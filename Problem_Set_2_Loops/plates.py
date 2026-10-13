import string 

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not 2 <= len(s) <=6:
        return False

    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    for i in range(len(s)):
        if s[i] in string.punctuation or s[i].isspace():
            return False

    for i in range(2,len(s)-1):
        if s[i].isdigit() and s[i+1].isalpha():
            return False

    for i in range(2,len(s)):
            if s[i].isdigit():
                if s[i] == "0":
                    return False
                break

    return True

main()