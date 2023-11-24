import calendar
from datetime import date, timedelta

def last_day_of_month(year, month):
    last_day = calendar.monthrange(year, month)[1]
    last_day_of_month = date(year, month, last_day)

    while last_day_of_month.weekday() > 4:
        last_day_of_month -= timedelta(days=1)

    return last_day_of_month

def payment():
    year = int(input("Enter the year: "))

    print("\nMonths and payment dates:\n")

    for month in range(1, 13):
        last_day = last_day_of_month(year, month)
        month_name = last_day.strftime("%B")
        payment_date = last_day.strftime("%d.%m.%Y")

        print(f"{month_name}: {payment_date}")

payment()