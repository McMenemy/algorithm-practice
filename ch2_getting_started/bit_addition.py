def bit_addition(array1, array2):
    carry_over = 0
    result = []

    for i, num in enumerate(array1):
        ind = len(array1) - 1 - i
        sum = array1[ind] + array2[ind] + carry_over
        if sum >= 10:
            carry_over = 1
            sum -= 10
        else:
            carry_over = 0
            
        result.insert(0, sum)

    result.insert(0, carry_over)
    return result

print bit_addition([3, 4, 3], [7, 3, 9]) # 1082
print 343 + 739
