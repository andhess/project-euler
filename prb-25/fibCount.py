def fibCount(digitLen):

    fibs = [1,1]

    while len(str(fibs[-1])) < digitLen:
        fibs.append(fibs[-1]+fibs[-2])

    # need the Nth value, not the number itself!
    return len(fibs)

print fibCount(1000)
