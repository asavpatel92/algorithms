#===============================================================================
# implementation of quicksort
#===============================================================================
import random
#===============================================================================
#  Swaps two items in an array, changing the original array
#===============================================================================
def swap(array, firstIndex, secondIndex):
    temp = array[firstIndex];
    array[firstIndex] = array[secondIndex]
    array[secondIndex] = temp
    

#===============================================================================
#  This function partitions given array and returns the index of the pivot.
#===============================================================================
def partition(array, firstIndex, lastIndex):
    
    #===========================================================================
    # #=========================================================================
    # #   Compare array[j] with array[r], for j = p, p+1,...r-1
    # #   maintaining that:
    # #   array[p..q-1] are values known to be <= to array[r]
    # #   array[q..j-1] are values known to be > array[r]
    # #   array[j..r-1] haven't been compared with array[r]
    # #   If array[j] > array[r], just increment j.
    # #   If array[j] <= array[r], swap array[j] with array[q],
    # #   increment q, and increment j. 
    # #   Once all elements in array[p..r-1]
    # #   have been compared with array[r],
    # #   swap array[r] with array[q], and return q.
    # #=========================================================================
    #===========================================================================
    
    q = firstIndex
    p = firstIndex
    for p in range(firstIndex, lastIndex):
        if(array[p] <= array[lastIndex]):
            swap(array, p, q)
            q += 1
        p += 1
    swap(array, lastIndex, q)
    return q

def quickSort(array, firstIndex, lastIndex):
    if(firstIndex < lastIndex):
        pivot  = partition(array, firstIndex, lastIndex)
        quickSort(array, firstIndex, pivot - 1)
        quickSort(array, pivot + 1, lastIndex)
    
def main():
    n = 10
    array = [random.randint(0, 100) for _ in range(n)] 
    print "Unsorted array is: ", array
    quickSort(array, 0, len(array) - 1)
    print "Sorted array is: ", array
    
if __name__ == '__main__':
    main()
    