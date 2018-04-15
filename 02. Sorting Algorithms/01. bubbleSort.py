import random
import copy

#Running time: T(n) = O(n*n)
#in general, not stable (depend on <= vs <)
#in-place
def bubbleSort1(arr):
    ln = len(arr)
    
    temp = None # to store value to order to swap
    isSorted = False # in the inner loop, if there is no swap operation, it means that array is already sorted 
    iteration = 0
    for i in range(ln):
        isSorted = True
        for j in range(0, ln-i-1):            
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
                isSorted = False
            iteration+=1
        if isSorted:
            break

    print(iteration)
    return arr

def bubbleSort2(arr):
    ln = len(arr)
    temp = None
    isSorted = False
    lastSwapIndex = ln-1
    iteration = 0

    for i in range(ln):
        isSorted = True
        for j in range(0,lastSwapIndex):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                isSorted = False
                lastSwapIndex = j
                iteration +=1

        if isSorted:
            break
    
    print(iteration)
    return arr


arr = [2,4,5,3,2,5,76,7,23,2,1,0,0,0,44,33,89]
arr = bubbleSort1(arr)
print(arr)

arr = [2,4,5,3,2,5,76,7,23,2,1,0,0,0,44,33,89]
arr = bubbleSort2(arr)
print(arr)


ARRAY_SIZE = 500
arr = []
for i in range(ARRAY_SIZE):
    arr.append(random.randint(0,ARRAY_SIZE))

arr1 = copy.deepcopy(arr)

print(bubbleSort1(arr))
print(bubbleSort2(arr1))

