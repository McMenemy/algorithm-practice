def selection_sort(array):
    for i in range(0, len(array) - 1):
        smallest = find_min_and_ind(array[i:])
        temp = array[i]
        array[smallest['ind'] + i] = temp
        array[i] = smallest['num']

    return array

def find_min_and_ind(array):
    smallest = float('Inf')
    smallest_ind = 0;
    for i, num in enumerate(array):
        if num < smallest:
            smallest = num
            smallest_ind = i

    return { 'num': smallest, 'ind': smallest_ind }



print selection_sort([4, 3, 2, 5, 2, 6])
