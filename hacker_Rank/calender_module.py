import calendar

MONTH, DAY, YEAR = map(int, input().split())

print(calendar.day_name[calendar.weekday(YEAR, MONTH, DAY)].upper())