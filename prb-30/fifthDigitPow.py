numbers = []
for i in range(2,1000001):
    a  = list(str(i))
    s = 0
    for j in a:
        s += int(j)**5
    if s == i:
        numbers.append(i)

print numbers
print sum(numbers)