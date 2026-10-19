# Day 11: Python Date and Time

from datetime import datetime, date

today = date.today()
current_time = datetime.now()

print("Today's date:", today)
print("Current date and time:", current_time)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)

formatted_date = current_time.strftime("%d-%m-%Y %H:%M:%S")
print("Formatted date and time:", formatted_date)
