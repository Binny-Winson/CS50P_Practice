import operator
import sys
from datetime import datetime

import inflect

p = inflect.engine()

def main():
    input_date = input("Date of Birth: ")
    birthday = get_date(input_date)
    print(min_to_words(birthday))

def get_date(birthday):
    try:
        return datetime.strptime(birthday, "%Y-%m-%d")
    except ValueError:
        sys.exit("Invalid date")

def min_to_words(birthday):
    today = datetime.now()
    midnight_today = today.replace(hour=0, minute=0, second=0, microsecond=0)

    time_delta = operator.sub(midnight_today, birthday)

    minutes_ = round(time_delta.total_seconds()/60)
    
    minutes_of_my_life = (f"{p.number_to_words(minutes_, andword="")} minutes").capitalize()
    return minutes_of_my_life


if __name__ == "__main__":
    main()