### Bubble sort: compare 2 elements and switch them into correct order
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
def selectSort(alist):
    for i in range(len(alist)-1, 0, -1):
        position = 0
        
        for j in range(1,i+1):
            if alist[j] > alist[position]:
                position = j
        
        alist[i], alist[position] = alist[position], alist[i]
    
    return alist


### Insert sort: treat the left part as a list, insert the number into the correct place
def insertSort(alist):
    for i in range(1, len(alist)):
        pos = i
        value = alist[i]
        while pos > 0 and alist[pos-1] > value:
            alist[pos] = alist[pos-1]
            pos -= 1
        
        alist[pos] = value
    
    return alist
