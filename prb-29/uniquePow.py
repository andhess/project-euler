import math

powers = []

for i in range(2,101):
    for j in range(2,101):
        powers.append( math.pow(i,j) )

powers = sorted(set(powers))

print len(powers)

