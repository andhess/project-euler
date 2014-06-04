import sys
import math

num = str( math.factorial( int(sys.argv[1]) ) )

sum = 0
for char in num:
    sum += int(char)

print sum
