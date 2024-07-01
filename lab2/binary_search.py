def binarySearch(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return None

arr = [1, 3, 4, 8, 9, 11, 12]
x = 11
result = binarySearch(arr, x)
if result:
    print("Index of element: ", result)
else: 
    print("Index was not found")