def dictionary_counter(array, fraction):
    counts = {}
    cutoff = len(array) * fraction

    for num in array:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    results = []
    for num, count in counts.items():
        if count >= cutoff:
            results.append(num)

    return results

print(dictionary_counter([2, 2, 4, 4], .5))
print(dictionary_counter([3, 5, 6, 3, 8], .25))
