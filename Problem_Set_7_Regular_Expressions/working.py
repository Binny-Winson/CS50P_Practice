import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # 1. Fixed Regex: Captures hours (1-12), optional minutes (:00-:59), and either AM or PM for both sides
    pattern = r"^([1-9]|1[0-2])(?::([0-5][0-9]))?\s(AM|PM)\sto\s([1-9]|1[0-2])(?::([0-5][0-9]))?\s(AM|PM)$"
    matches = re.search(pattern, s)

    # 2. If no match is found, CS50P expects a ValueError to be RAISED, not caught and printed
    if not matches:
        raise ValueError

    # Extract match groups safely
    start_hr = int(matches.group(1))
    start_min = matches.group(2) if matches.group(2) else "00"
    start_period = matches.group(3)

    end_hr = int(matches.group(4))
    end_min = matches.group(5) if matches.group(5) else "00"
    end_period = matches.group(6)


    # 3. Corrected 24-hour conversion logic
    # Start Hour Conversion
    if start_period == "AM":
        if start_hr == 12:
            starting_hour = 0

        else:
            starting_hour = start_hr
    else: # PM
        if start_hr == 12:
            starting_hour = 12
        else:
            starting_hour = start_hr + 12

    # End Hour Conversion
    if end_period == "AM":
        if end_hr == 12:
            ending_hour = 0
        else:
            ending_hour = end_hr
    
    else: # PM
        if end_hr == 12:
            ending_hour = 12
        else:
            ending_hour = end_hr + 12

    # 4. Format output with zfill
    return f"{str(starting_hour).zfill(2)}:{start_min} to {str(ending_hour).zfill(2)}:{end_min}"


if __name__ == "__main__":
    main()