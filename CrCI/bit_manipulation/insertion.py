def bit_insertion(int1, int2, i, j):
	mask = '1' * (int1.bit_length() - 1 - j) + '0' * (j - i + 1) + '1' * i
	mask = int(mask, 2)
	cleared_int = int1 & mask
	return cleared_int | (int2 << i)

print(bit_insertion(1024, 19, 2, 6))
