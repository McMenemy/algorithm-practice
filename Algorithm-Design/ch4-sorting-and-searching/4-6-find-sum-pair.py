import math

def bsearch(array, target):
    if len(array) == 0:
        return False

    mid_idx = math.ceil((len(array)-1) / 2)
    mid_val = array[mid_idx]

    if mid_val == target:
        return True
    elif mid_val < target:
        return bsearch(array[mid_idx+1:], target)
    elif mid_val > target:
        return bsearch(array[0:mid_idx], target)


def merge_sort(array):
    if len(array) == 1 or len(array) == 0:
        return array

    mid = math.ceil(len(array) / 2)
    left = array[0:mid]
    right = array[mid:]

    return(merge_helper(merge_sort(left), merge_sort(right)))

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

def is_sum_pair(array1, array2, sum):
    array2_sorted = merge_sort(array2)

    for num1 in array1:
        target = sum - num1
        if bsearch(array2_sorted, target):
            return True

    return False

print(bsearch([1,2,3,4,5], 4))
print(bsearch([1,2,3,4,5], 1))
print(bsearch([1,2,3,4,5], 3))
print(bsearch([1,2,3,4,5], 7))
print(merge_helper([1, 3, 4, 5], [1, 2, 4, 6]))
print(merge_sort([1, 6, 8, 3, 9, 2]))
print(is_sum_pair([2, 6, 4, 9, 3], [3, 9, 3, 7], 13))
print(is_sum_pair([2, 6, 4, 9, 3], [3, 9, 3, 7], 44))
