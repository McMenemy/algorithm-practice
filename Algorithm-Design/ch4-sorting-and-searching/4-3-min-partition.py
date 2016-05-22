import random

def quicksort(array):
    if len(array) == 1 or len(array) == 0:
        return array

    pivot = array.pop(random.randint(0, len(array) - 1))
    left = []
    right = []

    for num in array:
        if num <= pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)

    return quicksort(left) + [pivot] + quicksort(right)

def min_max_pair(array):
    sorted_array = quicksort(array)

    mid = int(len(sorted_array) / 2)
    pairs = []
    for i, num1 in enumerate(sorted_array[0:mid]):
        num2 = sorted_array[len(sorted_array) - 1 - i]
        pairs.append([num1, num2])

    max_pair_sum = float('-inf')

    for pair in pairs:
        current_sum = pair[0] + pair[1]
        if current_sum > max_pair_sum:
            max_pair_sum = current_sum

    return max_pair_sum

print(min_max_pair([1, 3, 5, 9]))
