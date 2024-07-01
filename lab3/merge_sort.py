def merge(a, b):
    c = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    if i < len(a):
        c += a[i:]
    if j < len(b):
        c += b[j:]
    return c

def mergeSort(array):
    if len(array) == 1:
        return array
    mid = len(array) // 2
    left = mergeSort(array[:mid])
    right = mergeSort(array[mid:])
    return merge(left, right)

array = [6, 5, 12, 10, 9, 1]

print(mergeSort(array))