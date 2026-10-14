while True:
    try:
        x = int(input("What's x? "))
    except ValueError, NameError:
        print("x must be an integer")
    else: 
        break
print(f"x is {x}")

