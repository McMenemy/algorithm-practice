import random

def imbalanced_teams(array):
    sorted_array = quicksort(array)
    mid = int(len(array) / 2)
    worse_team = sorted_array[0:mid+1]
    better_team = sorted_array[mid+1:]

    return [worse_team, better_team]

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

print(quicksort([1, 2, 3, 4, 5, 6]))
print(imbalanced_teams([1, 2, 3, 4, 5, 6]))
