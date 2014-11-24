
def doSearch(array, targetValue):
    min = 0;
    max = len(array) - 1;
    mid = 0;
    while (max >= min):
        mid = int(round((min+max)/2))
        if (array[mid] == targetValue):
            return mid
        elif (array[mid] < targetValue):
            min = mid + 1
        else:
            max = mid - 1
    return -1

if __name__ == '__main__':
    array = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 
        41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    targetValue = int(raw_input("Enter the number you want to find:"))
    print "Number is at index:", doSearch(array, targetValue)