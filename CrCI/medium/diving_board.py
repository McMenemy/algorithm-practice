def diving_board(k, long_length, short_length):
	length = k * long_length
	lengths = []
	lengths.append(length)
	diff = long_length - short_length
	for i in range(0, k):
		length -= diff
		lengths.append(length)
	return lengths

print(diving_board(10, 5, 3))
