def smallest_difference(list1, list2):
	sorted1 = sorted(list1)
	sorted2 = sorted(list2)
	smallest_diff = float('inf')
	i1 = 0
	i2 = 0
	while i1 < len(sorted1) and i2 < len(sorted2):
		if sorted1[i1] == sorted2[i2]:
			return 0
		elif sorted1[i1] > sorted2[i2]:
			diff = sorted1[i1] - sorted2[i2]
			i2 += 1
			if diff < smallest_diff:
				smallest_diff = diff
		elif sorted1[i1] < sorted2[i2]:
			diff = sorted2[i2] - sorted1[i1]
			i1 += 1
	return smallest_diff
	
print(smallest_difference([1, 3, 15, 11, 2], [21, 127, 235, 19, 8]) == 3)
