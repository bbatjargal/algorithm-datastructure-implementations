import random
import copy

def insertionSort(arr):
    ln = len(arr)
    iteration = 0
    
    for i in range(1,ln):

        j = i
        temp = arr[j]
        while j>0 and temp < arr[j-1]:
            arr[j] = arr[j-1]
            j-=1
            iteration +=1

        arr[j]=temp
    print(iteration)
    return arr

arr = [2,4,5,3,2,5,76,7,23,2,1,0,0,0,44,33,89]
print(insertionSort(arr))

ARRAY_SIZE = 500
arr = []
for i in range(ARRAY_SIZE):
    arr.append(random.randint(0, ARRAY_SIZE))

print(insertionSort(arr))

