import math

def bsearch(array, target):
    length = len(array)

    if length  == 0:
        return float('nan')

    mid = length / 2
    mid_val = array[mid]

    if mid_val == target:
        return mid
    if length == 1 and mid_val != target:
        return float('nan')

    left = array[0:mid]
    right = array[mid:]

    if mid_val > target:
        return bsearch(left, target)
    elif mid_val < target:
        return mid + bsearch(right, target)

array = [1, 2, 5, 6, 17, 22]
print bsearch(array, 5)
print bsearch(array, 1)
print bsearch(array, 22)
print bsearch(array, 13)
