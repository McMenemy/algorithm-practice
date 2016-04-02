def find_max_sub_array(array):
    if len(array) == 1:
        return array
    else:
        mid = len(array) / 2
        left = find_max_sub_array(array[0:mid])
        right = find_max_sub_array(array[mid:])
        crossover = find_max_crossover_sum(array[0:mid], array[mid:])
        left_sum = sum(left)
        right_sum = sum(right)
        crossover_sum = sum(crossover)

        if left_sum > right_sum and left_sum > crossover_sum:
            return left
        elif right_sum > left_sum and right_sum > crossover_sum:
            return right
        else:
            return crossover

def find_max_crossover_sum(left, right):
    left_sum = 0
    left_sum_max = float("-inf")
    start = len(left)
    right_sum = 0
    right_sum_max = float("-inf")
    end = 0

    for i, num in enumerate(left[::-1]):
        left_sum += num
        if left_sum > left_sum_max:
            left_sum_max = left_sum
            start = len(left) - 1 - i

    for i, num in enumerate(right):
        right_sum += num
        if right_sum > right_sum_max:
            right_sum_max = right_sum
            end = 1 + i

    combined_sum = left_sum + right_sum
    if left_sum > right_sum and left_sum > combined_sum:
        return left[start:]
    elif right_sum > left_sum and right_sum > combined_sum:
        return right[0:end]
    else:
        return left[start:] + right[0:end]

print find_max_sub_array([3, -2, 0, -1, 5, 3])
print find_max_sub_array([5, -2, -4])
print find_max_sub_array([-1, -2, -3, 5])
print find_max_sub_array([-1, 2, 3, 4, -5])

print find_max_crossover_sum([3, -2], [5, 3])
print find_max_crossover_sum([-1, 2], [-1, 3, 4, -5])
