def main():
    x = get_num()
    print(f"x is {x}")

def get_num():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            print("x is not an integer")

if __name__ == "__main__":
    main()
