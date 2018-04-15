import random
import copy

#Average case: T(n) = O(nlogn)
#Worst case: T(n) = O(n*n)
#not stable
#not in-place
#leftmost pivot
def quickSort(arr):
    ln = len(arr)
    if ln <= 1:
        return arr, 1
    p = 0 # pivot index
    
    L,E,G, iteration = partition(arr, p)
    L,t1 = quickSort(L)
    G,t2 = quickSort(G)
    
    L.extend(E)
    L.extend(G)
    return L,t1+t2+iteration

def partition(arr, p):
    pivot = arr[p]
    L = []
    E = []
    G = []
    iteration = 0
    for x in arr:
        if x < pivot:
            L.append(x)
        elif x == pivot:
            E.append(x)
        else: # x > pivot
            G.append(x)
        iteration +=1
    return L, E, G, iteration

#Average case: T(n) = O(nlogn)
#Worst case: T(n) = O(n*n)
#not stable
#in-place; if partition is in-place
#random pivot
def quickSortInPlace(arr, l, r):
    if l >= r:
        return 1

    k = r #random.randint(l, r) #a random integer between l and r
    swap(arr, k, r)  #place pivot at the rigth
    i,iteration = partitionInPlace(arr, l, r) #new position of pivot
    t1 = quickSortInPlace(arr,l,i-1)
    t2 = quickSortInPlace(arr,i+1,r)
    return t1+t2+iteration

def partitionInPlace(arr, l, r):
    i=l
    j= r -1
    pivot = arr[r] #pivot

    iteration = 0
    while i <= j:
        
        while i<=j and arr[i] <= pivot:
            iteration +=1
            i+=1

        while i <= j and arr[j] >= pivot:
            iteration +=1
            j-=1
        
        if i < j:
            swap(arr, i,j)
        iteration +=1
    swap(arr, i, r) #place pivot in proper location
    return i,iteration

def partitionInPlace2(arr, l, r):
    pivot = arr[r]
    i = l - 1    
    iteration = 0
    for j in range(l, r):
        if arr[j] < pivot:
            i = i + 1
            swap(arr,i,j)
        iteration +=1
    swap(arr,i + 1,r)
    return i + 1, iteration

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

ARRAY_SIZE = 30
arr = []
for i in range(ARRAY_SIZE):
    arr.append(random.randint(0, ARRAY_SIZE))

arr1 = copy.deepcopy(arr)
print(arr)
print(quickSort(arr))
print(quickSortInPlace(arr1, 0, len(arr1)-1))
print(arr1)

