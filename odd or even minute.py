# this program will tell whether your system's minute is "odd" or "even"
from datetime import datetime


odds = list(range(1, 60, 2))
right_this_minute = datetime.today().minute
if right_this_minute in odds:
    print("odd")
else:
    print("even")
