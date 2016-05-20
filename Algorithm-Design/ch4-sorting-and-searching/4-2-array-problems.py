# (a) Let S be an unsorted array of n integers. Give an algorithm that finds the pair x, y ∈ S that maximizes |x − y|. Your algorithm must run in O(n) worst-case time.
# (b) Let S be a sorted array of n integers. Give an algorithm that finds the pair x, y ∈ S that maximizes |x − y|. Your algorithm must run in O(1) worst-case time.
# (c) Let S be an unsorted array of n integers. Give an algorithm that finds the pair x, y ∈ S that minimizes |x − y|, for x ̸= y. Your algorithm must run in O(n log n) worst-case time.
# (d) Let S be a sorted array of n integers. Give an algorithm that finds the pair x, y ∈ S that minimizes |x − y|, for x ̸= y. Your algorithm must run in O(n) worst-case time.

# a
def max_difference_pair(array):
    smallest = float('inf')
    largest = float('-inf')
    smallest_i = 0
    largest_i = 0

    for i, num in enumerate(array):
        if num < smallest:
            smallest = num
            smallest_i = i
        elif num > largest:
            largest = num
            largest_i = i

    return [smallest_i, largest_i]

# print(max_difference_pair([1, 5, 9, 3, 11, 2]))

# b
def sorted_max_difference_pair(array):
    return [0, len(array) - 1]

# print(sorted_max_difference_pair([1, 2, 3, 4, 5, 6, 9]))

# c
def merge_sort(array):
    if len(array) == 1 or len(array) == 0:
        return array

    mid = int(len(array) / 2)
    left = array[0:mid]
    right = array[mid:]

    return merge_helper(merge_sort(left), merge_sort(right))

def merge_helper(array1, array2):
    merged = []
    i1 = 0
    i2 = 0
    while i1 < len(array1) and i2 < len(array2):
        if array1[i1] < array2[i2]:
            merged.append(array1[i1])
            i1 += 1
        else:
            merged.append(array2[i2])
            i2 += 1

    return merged + array1[i1:] + array2[i2:]

def min_pair(array):
    sorted_array = merge_sort(array)
    min = float('inf')
    pair = []

    for i, num in enumerate(sorted_array[0:-1]):
        difference = abs(num - sorted_array[i+1])
        if difference < min:
            min = difference
            pair = [i, i+1]

    return pair

# print(merge_sort([6, 5, 9, 3, 2]))
print(min_pair([1, 2, 3, 7, 7, 9]))
print(min_pair([1, 4, 3, 90, 7, 19]))

# d
def min_pair_sorted(sorted_array):
    min = float('inf')
    pair = []

    for i, num in enumerate(sorted_array[0:-1]):
        difference = abs(num - sorted_array[i+1])
        if difference < min:
            min = difference
            pair = [i, i+1]

    return pair
