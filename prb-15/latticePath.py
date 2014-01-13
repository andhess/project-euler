def path(d,r):

    count = 0

    if d == 0 and r == 0:
        count += 1

    if d > 0:
        count += path(d-1,r)
    if r>0:
        count += path(d,r-1)

    return count

# cannot compute anything over 12,12 :(
print path(1,1)
print path(2,2)
print path(3,3)
print path(4,4)
print path(5,5)
print path(6,6)
print path(7,7)
print path(8,8)
print path(9,9)
print path(10,10)
print path(11,11)
print path(12,12)

# each of these follows a series

# a.n = 2n choose n

# therefor for (20,20) it is merely 40 choose 20 = 137846528820