def main():
    x = get_num()
    print(f"x is {x}")

def get_num():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            pass

main()