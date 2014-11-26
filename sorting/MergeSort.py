#===============================================================================
# implementation of mergesort
#===============================================================================
from math import floor
import random

#===============================================================================
# Takes in an array that has two sorted subarrays,
# from [startIndex..joinIndex] and [joinIndex+1..endIndex], and merges the array
#===============================================================================
def merge(array, startIndex, endIndex, joinIndex):
    lowHalf = []
    highHalf = []
    k = startIndex
    i = 0
    j = 0
    while ( k <= joinIndex):
        lowHalf.append(array[k])
        i += 1
        k += 1
    
    while ( k <= endIndex):
        highHalf.append(array[k])
        j += 1
        k += 1
    
    k = startIndex
    i = 0
    j = 0
    while( i < len(lowHalf) and j< len(highHalf)):
        if ( lowHalf[i] < highHalf[j]):
            array[k] = lowHalf[i]
            i += 1
        else:
            array[k] = highHalf[j]
            j += 1
        k += 1
    while ( i < len(lowHalf)):
        array[k] = lowHalf[i]
        i += 1
        k += 1
    
    while ( j < len(highHalf)):
        array[k] = highHalf[j]
        j += 1
        k += 1

#Takes in an array and recursively merge sorts it
def mergeSort(array, startIndex, endIndex):
    if ( startIndex < endIndex):
        midPoint = int(floor((startIndex + endIndex)/ 2))
        mergeSort(array, startIndex, midPoint)
        mergeSort(array, midPoint + 1, endIndex)
        merge(array, startIndex, endIndex, midPoint)
        
def main():
    n = 100
    array = [random.randint(0, 100) for _ in range(n)] 
    print "Unsorted array is: ", array
    mergeSort(array, 0, len(array) - 1)
    print "Sorted array is: ", array
    
if __name__ == '__main__':
    main()