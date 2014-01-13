def countCoins(desiredValue, currentValue):
    numWays = 0
    if currentValue == desiredValue:
        numWays += 1

    if currentValue <= desiredValue:
        numWays += countCoins(desiredValue, currentValue + 200)
    if currentValue <= desiredValue:
        numWays += countCoins(desiredValue, currentValue + 100)
    if currentValue <= desiredValue:
        numWays += countCoins(desiredValue, currentValue + 50)
    if currentValue <= desiredValue:
        numWays += countCoins(desiredValue, currentValue + 20)
    if currentValue <= desiredValue:
        numWays += countCoins(desiredValue, currentValue + 10)
    if currentValue <= desiredValue:
        numWays += countCoins(desiredValue, currentValue + 5)
    if currentValue <= desiredValue:
        numWays += countCoins(desiredValue, currentValue + 2)
    if currentValue <= desiredValue:
        numWays += countCoins(desiredValue, currentValue + 1)




    return numWays

#print countCoins(10, 0)


# this is wrong!


def countCoints(remaining):
    if remaining == 0:
        return 1
    if remaining < 0:
        return 0

    count = 0

    count += countCoints(remaining - 200)
    count += countCoints(remaining - 100)
    count += countCoints(remaining - 50)
    count += countCoints(remaining - 20)
    count += countCoints(remaining - 10)
    count += countCoints(remaining - 5)
    count += countCoints(remaining - 2)
    count += countCoints(remaining - 1)

    return count

print countCoints(100)