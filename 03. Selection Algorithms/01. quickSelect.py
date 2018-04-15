import random
import copy

# To find k-th smallest element in an unordered list.
# arr: unordered array
# k: position of element, [1 <= k <= n-1]

# Average running time: T(n) = O(n)
def quickSelect(arr, k):

    ln = len(arr)
    if ln == 0:
        return None
    if ln == 1:
        return arr[0]

    p = ln//2 # pivot index

    L, E, G = partition(arr, p)
    
    lnL = len(L)
    lnE = len(E)

    
    if k <= lnL:
        return quickSelect(L, k)
    elif lnL < k <= lnL + lnE: # lnL < k <= lnL + lnE
        return E[0]
    else: # k > lnL + lnE
        k = k - lnL - lnE
        return quickSelect(G, k)

def partition(arr, p):
    pivot = arr[p]

    L = []
    E = []
    G = []

    for x in arr:
        if x < pivot:
            L.append(x)
        elif x == pivot:
            E.append(x)
        else: # x > pivot
            G.append(x)

    return L, E, G

ARRAY_SIZE = 10
arr = []
for i in range(ARRAY_SIZE):
    arr.append(random.randint(0, ARRAY_SIZE))

k = random.randint(1, ARRAY_SIZE-1)
print((arr, k))
print(quickSelect(arr, k))

