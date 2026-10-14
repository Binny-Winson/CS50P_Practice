grocery_list = {}

while True:
    try:
        item = input().strip().upper()
        try:
            grocery_list[item] += 1
        except KeyError:
            grocery_list[item] = 1
    except EOFError:
        print()
        break

for item in sorted(grocery_list):
    print(f"{grocery_list[item]} {item}")