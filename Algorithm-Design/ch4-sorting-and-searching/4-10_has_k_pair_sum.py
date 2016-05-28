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

def is_k_sum(array, k, sum):
    array = sorted(array)
    if k == 2:
        return has_sum_pair_sorted(array, sum)

    i = 0
    while i < len(array):
        target = sum - array[i]
        current_array = []
        current_k = k - 1
        for i2, num in enumerate(array):
            if i != i2:
                current_array.append(num)
        if is_k_sum(current_array, current_k, target):
            return True
        i += 1

    return False

print(is_k_sum([1, 2, 3, 4, 5], 3, 12))
print(is_k_sum([1, 2, 3, 4, 5], 3, 13))
