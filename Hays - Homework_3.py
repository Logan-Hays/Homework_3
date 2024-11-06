# Logan Hays 
# Lab Section: 13
# Submission Date: 11/5/2024
# Sources, help given to/received from


def is_it_a_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def how_many_days_in_month(month, year):
    days_in_month = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    if month == 2 and is_it_a_leap_year(year):
        return 29

    return days_in_month.get(month, 0)

def jan_1_day(year):
    y = year - 1
    day_of_week = (36 + y + (y // 4) - (y // 100) + (y // 400)) % 7
    return day_of_week

def is_date_real(month, day, year):
    if month < 1 or month > 12:
        return False
    if day < 1 or day > how_many_days_in_month(month, year):
        return False
    return True

def get_day_of_week_for_date(month, day, year):
    if not is_date_real(month, day, year):
        return "date that doesn't exist"

    jan_1_weekday = jan_1_day(year)

    days_in_previous_months = sum(how_many_days_in_month(m, year) for m in range(1, month))
    days_since_jan_1 = days_in_previous_months + (day - 1)

    day_of_week = (jan_1_weekday + days_since_jan_1) % 7

    weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    return weekdays[day_of_week]

date = input("Enter a date (MM/DD/YYYY): ").strip()

try:
    date_parts = date.split("/")
    month = int(date_parts[0])
    day = int(date_parts[1])
    year = int(date_parts[2])
except (ValueError, IndexError):
    print("date that doesn't exist")
else:
    result = get_day_of_week_for_date(month, day, year)
    print(f"On {date} the day of the week was a {result}")