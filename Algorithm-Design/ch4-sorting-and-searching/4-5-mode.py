import random

def quicksort(array):
    if len(array) == 0 or len(array) == 1:
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

def mode(array):
    sorted_array = quicksort(array)

    greatest_count = 0
    mode = 0

    i = 0
    j = 1
    while i < len(array) - 1:
        current_count = 0
        while array[i] == array[j] and i < len(array) - 2:
            current_count += 1
            i += 1
            j += 1

        if current_count > greatest_count:
            greatest_count = current_count
            mode = array[i]
        i += 1
        j += 1

    return mode

print(mode([1, 5, 6, 6, 9, 10, 4, 4, 6, 6]))
