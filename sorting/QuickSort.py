#===============================================================================
# implementation of quicksort
#===============================================================================
import random
#===============================================================================
#  Swaps two items in an array, changing the original array
#===============================================================================
def swap(array, index1, index2):
    array[index1], array[index2] = array[index2], array[index1]
    return array    

#===============================================================================
#  This function partitions given array and returns the index of the pivot.
#===============================================================================
 
def partition(array, start_index, end_index):
    
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
    
    current_index = start_index
    for i in range(start_index, end_index):
        if array[i] <= array[end_index]:
            swap(array, i, current_index)
            current_index += 1
    swap(array, current_index, end_index)
    return current_index
 
 
def quick_sort(array, start_index, end_index):
    if start_index < end_index:
        pivot = partition(array, start_index, end_index)
        quick_sort(array, start_index, pivot - 1)
        quick_sort(array, pivot + 1, end_index)
    
def main():
    n = 10
    array = [random.randint(0,100) for _ in range(n)]
    print "Unsorted Array is : %s" %(array)
    quick_sort(array, 0, len(array) - 1)
    print "Sorted Array is : %s" %(array) 
    
if __name__ == '__main__':
    main()
    