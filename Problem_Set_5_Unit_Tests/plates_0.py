import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not s[:2].isalpha():
        return False

    if not 2 <= len(s) <= 6:
        return False

    for i in range(len(s)):
        if s[i] in string.punctuation or s[i].isspace():
            return False

    for i in range(2, len(s)):
        if s[i].isdigit():
            if s[i] == '0':
                return False
            break

    for i in range(2, len(s)):
        if s[i].isdigit():
            for j in range(i+1, len(s)):
                if s[j].isalpha():
                    return False

    return True

if __name__ == "__main__":
    main()