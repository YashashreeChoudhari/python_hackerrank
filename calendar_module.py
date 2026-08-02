#Que. Given a date in MM DD YYYY format, determine the day of the week for that date and print it in uppercase (e.g., MONDAY).

import calendar

month, day, year = map(int, input().split())

print(calendar.day_name[calendar.weekday(year, month, day)].upper())