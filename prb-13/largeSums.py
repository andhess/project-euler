import sys
import math
import csv
import numpy as np


def getBigSum( arrayOfNums ):
    return sum( arrayOfNums )

def txtToArray( filepath ):
    data = []

    with open(filepath, 'rb') as csvfile:
        csvData = csv.reader( csvfile )

        # toss into 1 array
        for row in csvData:
            data.append( int(row[0]) )

        #data = np.array( data )

        return data


print getBigSum( txtToArray( sys.argv[1] ) )
