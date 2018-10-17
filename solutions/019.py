"""This is Problem 19 of ProjectEuler

Find how many Sundays fell on the first of the month in the 20th century"""

__author__ = "Andrew Phoenix"

import datetime

today = datetime.date(1901, 1, 1)
millenium = datetime.date(2001, 1, 1)
next = datetime.timedelta(days=1)
sundays = 0
while today < millenium:
    if today.day == 1:
        if today.weekday() == 6:
            sundays = sundays + 1
    today = today + next
print
sundays
