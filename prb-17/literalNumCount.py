def countPlace(number):
    reference = {'1': 3, '2': 3, '3': 5, '4': 4, '5': 4, '6': 3, '7': 5, '8': 5, '9': 4, '10': 3, '11': 6, '12': 6, '13': 8, '14': 8, '15': 7, '16': 7, '17': 9, '18': 8, '19': 8, '20': 6, '30': 6, '40': 5, '50': 5, '60': 5, '70': 7, '80': 6, '90': 6, '100': 10, '1000': 11, 'and': 3, 'hundred': 7, 'thousand': 8}
    refKeys = reference.keys()

    string = str(number)
    st = list(string)

    if string in refKeys:
        return reference[string]

    else:

        if len(st) == 3:

            count = reference[st[0]] + reference['hundred']
            remainder = number - int(st[0])*100
            if remainder > 0:
                count += reference['and']
                remainString = str(remainder)
                
                if remainString in refKeys:
                    count += reference[remainString]
                else:
                    lookup = int(st[1])*10
                    count += reference[str(lookup)] + reference[st[2]]
            
            return count


        if len(st) == 2:
            lookup = int(st[0])*10
            return reference[str(lookup)] + reference[st[1]]


totalCount = 0
for i in range(1,1001):
    totalCount += countPlace(i)

print totalCount

#print countPlace(115)