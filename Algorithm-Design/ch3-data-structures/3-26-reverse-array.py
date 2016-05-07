def reverse_array(array):
    rev = []
    for el in reversed(array):
        rev.append(el)

    return rev


print(reverse_array([1, 2, 3, 4, 5]))
