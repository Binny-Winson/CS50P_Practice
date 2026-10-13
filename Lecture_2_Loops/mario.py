def main():
    square(get_number())

def get_number():
    number = int(input("What's the number? "))
    return number

def square(n):
    for i in range(n):
        for j in range(n):
            print("#", end="")
        print()

if __name__ == "__main__":
    main()