def selection_sort(array):
    for i in range(0, len(array) - 1):
        smallest = min(array[i:])
        smallest_ind = array[i:].index(smallest) + i
        temp = array[i]
        array[smallest_ind] = temp
        array[i] = smallest

    return array

print selection_sort([4, 3, 2, 5, 2, 6])
