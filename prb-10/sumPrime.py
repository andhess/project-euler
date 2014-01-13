import math

def count(x): return x

def calcPrimeToRange(number):

    primes = [0,0] + map( count, range(2,number+1) )
    p = 2

    while math.pow(p,2) <= number:

        n=2

        while p*(n) <= number:
            primes[p*n] = 0
            n+=1

        p+=1
        while primes[p] == 0:
            p+=1

    return primes


primes = calcPrimeToRange(2000000)
#print primes
print sum(primes)