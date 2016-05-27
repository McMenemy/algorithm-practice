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
    for num in array:
        target = sum - num
        if does_include(array, target):
            return True

    return False

def update_loop_idxs(loop_idxs, array_len):
    # this will find the current loop that needs iterated (aka cutoff_loop)
    cutoff_loop = 0
    for i, current_idx in enumerate(loop_idxs[::-1]):
        max_idx = array_len - i
        if current_idx < max_idx:
            cutoff_loop = i
            loop_idxs[i] += 1
    # this will reset all inner loop counters inside the cutoff_loop
    for loop_idx in loop_idxs[::-1]

def has_k_pair_sum(array, k, sum):
    sorted_array = array.sort()

    loop_idxs = []
    for i in range(k-1):
        idx.append(i)

    current_loop_idx = len(loop_idxs)-1
    while loop_idxs[0] < len(array) - k
        most_inner_idx = loop_idxs[-1]
        while most_inner_idx < len(array)
            current_sum = 0
            for i in loop_idxs:
                current_sum += array[loop_idxs[i]]
            target_sum = sum - current_sum
            if has_sum_pair(array[loop_idxs[-1]:], target_sum): # log(n) bsearch
                return True
            most_inner_idx += 1

        update_loop_idxs(loop_idxs, len(array))
