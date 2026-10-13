amount_due = 50
coins = [25, 10, 5]

while amount_due > 0:
    change = int(input("Insert Coin: "))
    if change in coins:
        amount_due -= change
        if amount_due == 0:
            print(f"Change Owed: {amount_due}")
            break
        elif amount_due < 0:
            change_owed = amount_due * -1
            print(f"Change Owed: {change_owed}")
        else:
            print(f"Amount Due: {amount_due}")
            continue
    else:
        print(f"Amount Due: {amount_due}")
        continue