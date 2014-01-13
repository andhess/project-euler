import datetime

day = datetime.date(1901,1,1)
sundays = 0
thirtyO = [1,3,5,7,8,10,12]
thirty = [4,6,9,11]

for i in range(0, 1200):

    if day.weekday() == 6:
        sundays += 1

    # add 30
    if thirty.count(day.month):
        day += datetime.timedelta(days=30)

    # add 31
    elif thirtyO.count(day.month):
        day += datetime.timedelta(days=31)

    # add 28
    else:
        day += datetime.timedelta(days=28)

        # leap year
        if day.year % 100 == 0:
            if day.year % 400 == 0:
                day += datetime.timedelta(days=1)   

        else:
            if day.year % 4 == 0:
                day += datetime.timedelta(days=1)

print sundays
print day