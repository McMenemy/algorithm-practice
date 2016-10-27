# find the median in constant time of an array of integers
# only works for odd numbers, changing to work for even would require a refactor to pivot around
# two numbers at a time
import random

def median(numbers, offcenter = 0):
    print('numbers', numbers)
    pivot_index = random.randrange(0, len(numbers))
    pivot = numbers[pivot_index]
    left = []
    right = []

    for i, num in enumerate(numbers):
        if num <= pivot and i != pivot_index:
            left.append(num)
        elif num > pivot and i != pivot_index:
            right.append(num)

    # offcenter keeps track of numbers on either side of median from prev rounds
    difference = len(right) - len(left) + offcenter
    print(offcenter)
    print('left', left)
    print('right', right)
    print('diff', difference)
    if difference == 0:
        return pivot 
    elif difference < 0:
        return median(left, len(right) + 1 + offcenter)
    elif difference > 0:
        return median(right, offcenter - len(left) - 1)

print(median([1, 1, 2, 3, 4, 5, 6]))
 
