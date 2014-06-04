import math
import sys


def getNthPrime( num ):
    number = num -1
    knownPrimes = [2]

    counter = 3

    while number >= len(knownPrimes):

        for prime in knownPrimes:
            isPrime = True
            if counter % prime == 0:
                isPrime = False
                break

        if isPrime:
            knownPrimes.append(counter)
        counter += 1

    print len(knownPrimes)
    print knownPrimes

    return knownPrimes[number]

print getNthPrime( int(sys.argv[1]) )