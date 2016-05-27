# a
import random
import math

def quicksort(array):
    if len(array) == 1 or len(array) == 0:
        return array

    mid_idx = random.randint(0, len(array)-1)
    pivot = array.pop(mid_idx)
    left = []
    right = []

    for num in array:
        if num <= pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)

    return quicksort(left) + [pivot] + quicksort(right)

def does_include(array, target):
    if len(array) == 0:
        return False

    mid_idx = math.ceil((len(array)-1) / 2)
    mid = array[mid_idx]
    left = array[0:mid_idx]
    right = array[mid_idx+1:]

    if mid == target:
        return True
    elif mid < target:
        return does_include(right, target)
    elif mid > target:
        return does_include(left, target)

def has_sum_pair(array, sum):
    sorted_array = quicksort(array)

    for num in sorted_array:
        target = sum - num
        if does_include(sorted_array, target):
            return True

    return False

# b
def has_sum_pair_sorted(array, sum):
    num_dict = {}

    for num in array:
        if num in num_dict:
            num_dict[num] += 1
        else:
            num_dict[num] = 1

    for num in array:
        target = sum - num
        if target in num_dict:
            # to not count the same num twice
            if target != num:
                return True
            elif num_dict[target] > 1:
                return True

    return False


print(quicksort([1, 6, 3, 0, 9, 4]))
print(quicksort([6, 9, 8, 4, 3]))
print(does_include([1, 2, 5, 8, 9], 9))
print(does_include([1, 2, 5, 8, 9], 5))
print(does_include([1, 2, 5, 8, 9], 1))
print(does_include([1, 2, 5, 8, 9], 11))
print(has_sum_pair([1, 4, 9, 11, 3], 10))
print(has_sum_pair([1, 4, 9, 11, 3], 111))
print(has_sum_pair_sorted([1, 2, 3, 4, 5], 4))
print(has_sum_pair_sorted([1, 2, 3, 4, 5], 42))
print(has_sum_pair_sorted([1, 2, 3, 4, 5], 2))
