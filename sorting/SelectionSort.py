#===============================================================================
# implementation for selection sort
#===============================================================================
import random

def swapIndex(array, firstIndex, secondIndex):
    temp = array[firstIndex]
    array[firstIndex] = array[secondIndex]
    array[secondIndex] = temp

def findMinValue(array, startIndex):
    minIndex = startIndex
    minValue = array[startIndex]
    for i in range(startIndex + 1, len(array)):
        if(array[i] < minValue):
            minIndex = i
            minValue = array[i]
    return minIndex

def selectionSort(array):
    for i in range(len(array)):
        refIndex = findMinValue(array, i)
        swapIndex(array, i, refIndex)
    return array
        


if __name__ == '__main__':
    n = 10
    array = [random.randint(0, 100) for _ in range(n)] 
    print "Unsorted array is: ", array
    selectionSort(array)
    print "Sorted array is: ", array