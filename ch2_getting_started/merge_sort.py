def merge_short(array):
    length = len(array)
    if length == 1 or length == 0:
        return array
    else:
        mid = length / 2
        left = array[0:mid]
        right = array[mid:length]
        return merge(merge_short(left), merge_short(right))

def merge(array1, array2):
    result = []
    while len(array1) != 0 and len(array2) != 0:
        if array1[0] < array2[0]:
            result.append(array1.pop(0))
        else:
            result.append(array2.pop(0))

    return result + array1 + array2

print merge_short([1, 2, 3, 6, 4, 3, 12])
