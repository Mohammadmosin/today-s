def merge(a, b):
    l = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            l.append(a[i])
            i += 1
        elif a[i] > b[j]:
            l.append(b[j])
            j += 1
    while i < len(a):
        l.append(a[i])
        i += 1
    while j < len(b):
        l.append(b[j])
        j += 1
    return l

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        left = merge_sort(left)
        right = merge_sort(right)
        return merge(left, right)


arr = [12, 123, 2, 3435, 65, 5767, 6677, 12123]
print(merge_sort(arr))
