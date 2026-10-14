while True:
    try:
        fuel_level = input("Fraction: ").strip()
        num, denom = fuel_level.split("/")
        num = int(num)
        denom = int(denom)
        if num > denom:
            continue
        elif num/denom < 0:
            continue
        
        level = round((num/denom)*100)
        
        if level <=1:
            print("E")
        elif level >= 99:
            print("F")
        else:
            print(f"{level}%")
    except (ValueError, ZeroDivisionError):
        pass
    else:
        break

