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
print path(20,20)