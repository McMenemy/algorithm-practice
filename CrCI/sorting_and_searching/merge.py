def merge(arr1, arr2):
	merged = []
	while arr1 and arr2:
		if arr1[0] <= arr2[0]:
			merged.append(arr1.pop(0))
		elif arr1[0] > arr2[0]:
			merged.append(arr2.pop(0))
	return merged + arr1 + arr2

print(merge([1, 4, 5, 9], [1, 3, 6, 8, 10]))
