def linear_search(array, target):
    for i, el in enumerate(array):
        if el == target:
            return i
            break

    return '{} not found'.format(target)

print linear_search([1, 2, 3, 4], 4)
print linear_search([1, 2, 3, 4], 5)
