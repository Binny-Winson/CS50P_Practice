def main():
    time = input("What time is it? ").strip()
    time = convert(time)
    
    if  7.0 <= time <= 8.0:
        print("breakfast time")
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    elif 18.0 <= time <= 19.0:
        print("dinner time")
    else:
        print("")

def convert(time):
    if " " in time:
        time, meridiem = time.split()
        hr, min = time.split(":")
        hr = int(hr)
        min = int(min)/60
        meridiem = meridiem.replace(".", "").lower()

        if meridiem == "pm" and hr < 12:
            hr += 12
        elif meridiem == "am" and hr == 12:
            hr = 0
    else:        
        hr, min = time.split(":")
        hr = int(hr)
        min = int(min)/60
    return (hr + min)

if __name__ == "__main__":
    main()