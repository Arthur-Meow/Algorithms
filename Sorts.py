### Bubble sort: compare 2 elements and switch them into correct order
### n^2
def bubbleSort(alist):
    for i in range(len(alist)-1, 0, -1):
        for j in range(i):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
                
    return alist


### Improved bubble sort: if no switch happens, stop the program        
def shortBubbleSort(alist):
    exchange = True
    passnum = len(alist)-1
    
    while passnum > 0 and exchange:
        exchange = False
        for j in range(passnum):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
                exchange = True
    
    return alist


### Select sort: find the largest one and place it at the end
### n^2
def selectSort(alist):
    for i in range(len(alist)-1, 0, -1):
        position = 0
        
        for j in range(1,i+1):
            if alist[j] > alist[position]:
                position = j
        
        alist[i], alist[position] = alist[position], alist[i]
    
    return alist


### Insert sort: treat the left part as a list, insert the number into the correct place
### n^2
def insertSort(alist):
    for i in range(1, len(alist)):
        pos = i
        value = alist[i]
        while pos > 0 and alist[pos-1] > value:
            alist[pos] = alist[pos-1]
            pos -= 1
        
        alist[pos] = value
    
    return alist


### Merge sort: Keep breaking down the list into two parts, sort the sublist then merge the sorted sublists
### nlog(n)
def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        leftpart = alist[:mid]
        rightpart = alist[mid:]
        mergeSort(leftpart)
        mergeSort(rightpart)

        i = 0
        j = 0
        k = 0

        while i < len(leftpart) and j < len(rightpart):
            if leftpart[i] < rightpart[j]:
                alist[k] = leftpart[i]
                i += 1
            else:
                alist[k] = rightpart[j]
                j += 1
            k += 1

        while i < len(leftpart):
            alist[k] = leftpart[i]
            i += 1
            k += 1

        while j < len(rightpart):
            alist[k] = rightpart[j]
            j += 1
            k += 1
    return alist
            

#################    Quick Sort   #############################
### Quick sort (use middle number): find the 2nd largest number in three numbers that are picked from the most left, middle,
### and most right of the list, place it to the most left position, then perform quick sort.
### nlog(n)
def setPivot(alist, first, last):
    # first and last are positions
    mid = (first + last) // 2
    if alist[mid] > alist[last]:
        alist[mid], alist[last] = alist[last], alist[mid]

    if alist[first] > alist[last]:
        alist[first], alist[last] = alist[last], alist[first]

    if alist[first] < alist[mid]:
        alist[first], alist[mid] = alist[mid], alist[first]

    return alist[first]

def partition(alist, first, last):
    pivot = setPivot(alist, first, last)
    leftpos = first + 1
    rightpos = last
    done = False

    while not done:
        while leftpos <= rightpos and alist[leftpos] <= pivot:
            leftpos += 1

        while leftpos <= rightpos and alist[rightpos] >= pivot:
            rightpos -= 1

        if leftpos > rightpos:
            done = True
        else:
            alist[leftpos], alist[rightpos] = alist[rightpos], alist[leftpos]

    alist[first], alist[rightpos] = alist[rightpos], alist[first]

    return rightpos

def quickSortHelper(alist, first, last):
    if first < last:
        splitPoint = partition(alist, first, last)
        quickSortHelper(alist, first, splitPoint-1)
        quickSortHelper(alist, splitPoint+1, last)

def quickSort(alist):
    quickSortHelper(alist, 0, len(alist)-1)
    return alist


####
