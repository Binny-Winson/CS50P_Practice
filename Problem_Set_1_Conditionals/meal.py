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
    hr, min = time.split(":")
    hr = int(hr)
    min = (int(min)/6)/10
    time = round(float(hr+min),1)
    return time


if __name__ == "__main__":
    main()