def flip_bit(number):
	bits = '{0:b}'.format(number)
	max_count = 0
	current_count = 0
	prev_count = 0
	for bit in bits:
		if bit == '0':
			if prev_count > max_count: max_count = prev_count
			prev_count = current_count + 1
			current_count = 0
		else:
			current_count += 1
			prev_count += 1
	return max(max_count, current_count, prev_count)
		
print(flip_bit(1775))
