def exlude_cumalative_product_array(array):
    forward_cumulative_product = [1]

    for num in reversed(array[1:]):
        next_value = forward_cumulative_product[-1] * num
        forward_cumulative_product.append(next_value)

    backward_cumulative_product = [1]

    for num in array[0:-1]:
        next_value = backward_cumulative_product[-1] * num
        backward_cumulative_product.append(next_value)

    answer = []

    j = len(forward_cumulative_product) - 1
    for i in range(0, len(forward_cumulative_product)):
        answer.append(forward_cumulative_product[j] * backward_cumulative_product[i])
        j -= 1

    return answer

print(exlude_cumalative_product_array([2, 3, 4, 5]))
