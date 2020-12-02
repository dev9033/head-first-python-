import datetime

# tell the current date and time
print(datetime.datetime.today())

# current date
print(datetime.datetime.today().day)

# current month
print(datetime.datetime.today().month)

# current year
print(datetime.datetime.today().year)

# give a user-friendly version of today's date
print(datetime.date.isoformat(datetime.date.today()))
