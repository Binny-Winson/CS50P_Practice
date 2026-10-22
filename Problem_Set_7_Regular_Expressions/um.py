import re


def main():
    print(count(input("Text: ")))


def count(s):
    fillers = re.findall(r'\bum\b', s, re.IGNORECASE)
    return len(fillers)
    
    
    # total = 0
    
    # for i in range(len(fillers)):
    #     total += 1
    # return total

if __name__ == "__main__":
    main()