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

def insertion_sort_adv(array, sort_funct):
    sorted_array = [array[0]]
    for num in array[1:]:
        if not sort_funct(sorted_array[-1], num):
            sorted_array.append(num)
        else:
            for index, sorted_num in enumerate(sorted_array):
                if sort_funct(sorted_num, num):
                    sorted_array.insert(index, num)
                    break

    return sorted_array

def inverse_sort(sorted_num, num):
    return sorted_num <= num

print insertion_sort_adv([2, 1, 3, 4], inverse_sort)
