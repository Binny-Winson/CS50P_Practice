def main():
    meow(get_number())

def meow(n):
    for _ in range(n):
        print("meow")

def get_number():
    x = int(input("What's x? "))
    if x > 0:
        return x

main()