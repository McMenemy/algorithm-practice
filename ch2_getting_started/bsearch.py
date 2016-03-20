import math

def bsearch(arrray, target):
    length = len(array)

    if len(array) == 0:
        return float('nan')

    mid = length / 2
    mid_val = array[mid]

    if mid_val == target:
        return mid

    left = array[0:mid]
    right = array[mid:]

    if mid_val > target:
        return bsearch(left, target)
    elif mid_val < target:
        return mid_val + bsearch(right, target)

array = [1, 2, 5, 6, 17, 22]
print bsearch(array, 5)
print bsearch(array, 1)
print bsearch(array, 22)
print bsearch(array, 13)
