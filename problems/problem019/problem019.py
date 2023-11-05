#!/usr/bin/python3
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
        else:
            return True
    return False

def main():
    # Initialize variables
    sundays_on_first = 0
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_of_week = 3  # 0 = Sunday, 1 = Monday, ..., 6 = Saturday

    # Iterate through years from 1901 to 2000
    for year in range(1901, 2001):
        for month in range(12):
            if day_of_week == 0:  # If it's a Sunday
                sundays_on_first += 1

            # Calculate the day of the week for the first day of the next month
            if is_leap_year(year) and month == 1:
                day_of_week = (day_of_week + 29) % 7
            else:
                day_of_week = (day_of_week + days_in_month[month]) % 7
    return sundays_on_first

if __name__ == '__main__':
    sundays_on_first = main()
    print(sundays_on_first)
