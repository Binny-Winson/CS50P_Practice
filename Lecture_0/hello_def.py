def main():
    name = input("What's your name? ")
    hello(name)
    hello()

def hello(to = "World"):
    print("Hello,", to)

main()