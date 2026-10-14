grocery_dict = {}

while True:
    try:
        item = input().strip().upper()
        if item in grocery_dict:
            grocery_dict[item] += 1
        else:
            grocery_dict[item] = 1
    except EOFError:
        print()
        break


for item in sorted(grocery_dict):
    print(f"{grocery_dict[item]} {item}")

