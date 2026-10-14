month_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        user_date = input("Date: ").strip()
        if "/" in user_date:
            month, day, year = user_date.split("/")
            month = int(month.strip())
            day = int(day.strip())
            year = int(year.strip())
        elif ", " in user_date:
            month_day, year = user_date.split(", ")
            month_name, day = month_day.split(" ")
            month_name = month_name.title()
            if month_name in month_list:
                month = month_list.index(month_name) + 1
            else:
                continue
            day = int(day.strip())
            year = int(year.strip())
        else:
            continue

        if month > 12 or day > 31:
            continue

        break
            
    except ValueError:
        pass
    
print(f"{year}-{month:02}-{day:02}")