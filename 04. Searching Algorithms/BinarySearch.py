def binarySearch(arr, x):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            right = mid - 1
        else:
            left = mid + 1
    return -1

def recursiveBinarySearch(arr, x, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2
    if arr[mid] == x:
        return mid
    elif arr[mid] > x:
        return recursiveBinarySearch(arr, x, left, mid - 1)
    return recursiveBinarySearch(arr, x, mid + 1, right)

arr = [1, 2, 8, 10]
x = 10

index = binarySearch(arr, x)
print(index)

index1 = recursiveBinarySearch(arr, x, 0, len(arr) - 1)
print(index1)
