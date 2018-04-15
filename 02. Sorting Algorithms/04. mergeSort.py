import copy
import random

#Running time: T(n) = O(nlogn)
#not in-place
#stable
def mergeSort(arr):

    ln = len(arr)
    if ln <= 1:
        return arr

    mid = ln//2
    left = mergeSort(arr[0:mid])
    right = mergeSort(arr[mid:ln])
    arr = merge(left, right)
    return arr

def merge(arr1, arr2):

    arr = []
    i = 0 # index for arr1
    j = 0 # index for arr2
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr.append(arr1[i])
            i +=1
        else:
            arr.append(arr2[j])
            j +=1

    while i < len(arr1):
        arr.append(arr1[i])
        i+=1
    while j < len(arr2):
        arr.append(arr2[j])
        j+=1

    return arr



ARRAY_SIZE = 30
arr = []
for i in range(ARRAY_SIZE):
    arr.append(random.randint(0, ARRAY_SIZE))

print(arr)
print(mergeSort(arr))
