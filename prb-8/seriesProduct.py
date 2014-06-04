import sys
import csv
import math

def productList( inputList ):
    output = 1
    for value in inputList:
        output *= int(value)
    return output

def largestProdSeries( filepath, seriesLength ):

    with open(filepath, 'rb') as csvfile:
        csvData = csv.reader( csvfile )
        bigNum = csvData.next()[0]

    largestProduct = 0

    t = len(bigNum) - seriesLength

    for i in range(0, len(bigNum) - seriesLength + 1):
        newProduct = productList( bigNum[i:i+seriesLength] )
        if largestProduct < newProduct:
            largestProduct = newProduct

    return largestProduct

print largestProdSeries( sys.argv[1], int(sys.argv[2]) )

