def insertion_sort(array):
    sorted_array = [array[0]]
    for num in array[1:]:
        for index, sorted_num in enumerate(sorted_array):
            if num <= sorted_num:
                sorted_array.insert(index, num)
                break
            if num > sorted_array[-1]:
                sorted_array.append(num)
                break

    return sorted_array

print insertion_sort([2, 1, 3, 4])
print insertion_sort([2, 1, 3, 4, 4, 3, 9, 10, 2, 1])
