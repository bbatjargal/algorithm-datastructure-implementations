import random 
import copy

#Running time: T(n)=O(n*n)
#non stable in general
#in-place
def selectionSort(arr):
    
    ln = len(arr)
    iteration = 0
    for i in range(ln):

        min_value = arr[i]
        min_index = i
        for j in range(i+1, ln):
            if arr[j] < min_value:
                min_value = arr[j]
                min_index = j
            iteration+=1
        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp

    print(iteration)
    return arr 



arr = [2,3, 1, 2,4,8,0,3,6,78,3,56,8,19,3,2,57,89,1,2,8]
arr = [2,4,5,3,2,5,76,7,23,2,1,0,0,0,44,33,89]

arr = selectionSort(arr)
print(arr)

ARRAY_SIZE = 500
arr = []
for i in range(ARRAY_SIZE):
    arr.append(random.randint(0,ARRAY_SIZE))

print(selectionSort(arr))


