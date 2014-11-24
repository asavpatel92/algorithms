#===============================================================================
# implementation for insertionSort
#===============================================================================
import random

def insert(array, rightIndex, value):
    refIndex = rightIndex
    while refIndex >= 0 and array[refIndex] > value:
        array[refIndex + 1] = array[refIndex]
        refIndex = refIndex -1
    array[refIndex + 1] = value

def insertionSort(array):
    for i in range(1, len(array)):
        insert(array, i-1, array[i])
    return array

if __name__ == '__main__':
    n = 10
    array = [random.randint(0, 100) for _ in range(n)] 
    print "Unsorted array is: ", array
    insertionSort(array)
    print "Sorted array is: ", array
