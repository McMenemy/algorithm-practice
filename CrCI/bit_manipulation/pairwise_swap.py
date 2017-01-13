def pairwise_swap(number):
	odd_mask = (int('10' * int(number.bit_length() / 2), 2) & number) >> 1
	even_mask = (int('01' * int(number.bit_length() / 2), 2) & number) << 1
	return odd_mask + even_mask

print(pairwise_swap(12))
print(pairwise_swap(23))
print(pairwise_swap(47))
print(pairwise_swap(890))
