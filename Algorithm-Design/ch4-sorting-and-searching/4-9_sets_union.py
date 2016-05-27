import math

def merge_helper(array1, array2):
    merged = []
    i1 = 0
    i2 = 0
    while i1 < len(array1) and i2 < len(array2):
        if array1[i1] <= array2[i2]:
            merged.append(array1[i1])
            i1 += 1
        elif array1[i1] > array2[i2]:
            merged.append(array2[i2])
            i2 += 1

    return merged + array1[i1:] + array2[i2:]

def merge_sort(array):
    if len(array) == 0 or len(array) == 1:
        return array

    mid_idx = math.ceil((len(array)-1) / 2)
    left = array[0:mid_idx]
    right = array[mid_idx:]

    return merge_helper(merge_sort(left), merge_sort(right))

def find_union(array1, array2):
    sorted1 = merge_sort(array1)
    sorted2 = merge_sort(array2)
    union = {}

    i1 = 0
    i2 = 0
    while i1 < len(array1) and i2 < len(array2):
        if sorted1[i1] == sorted2[i2]:
            if not sorted1[i1] in union:
                union[sorted1[i1]] = sorted1[i1]
            i1 += 1
            i2 += 1
        elif sorted1[i1] < sorted2[i2]:
            i1 += 1
        elif sorted1[i1] > sorted2[i2]:
            i2 += 1

    return list(union)



print(merge_helper([1, 3, 8], [2, 3, 4]))
print(merge_sort([3, 2, 9, 5]))
print(merge_sort([2, 6, 4, 9, 2]))
print(find_union([4, 5, 3, 2], [3, 6, 2, 9]))
print(find_union([4, 5, 3, 2, 2], [3, 6, 2, 9, 2]))
