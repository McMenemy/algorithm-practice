def next_number(number):
	bits = list('{0:b}'.format(number))

	zero_idx = -1
	one_idx = -1
	for i, bit in enumerate(bits[::-1]):
		if bit == '0':
			zero_idx = len(bits) - 1 - i
		elif zero_idx != -1 and bit == '1':
			one_idx = len(bits) - 1 - i
			break
	
	smallest = ''
	if zero_idx == -1 or one_idx == -1:
		smallest = 'NA'
	else:
		smallest = bits[:]
		smallest[zero_idx] = '1'
		smallest[one_idx] = '0'
		smallest = ''.join(smallest)

	zero_idx = -1
	one_idx = -1
	for i, bit in enumerate(bits[::-1]):
		if bit == '1':
			one_idx = len(bits) - 1 - i
		elif one_idx != -1 and bit == '0':
			zero_idx = len(bits) - 1 - i
			break
	largest = ''
	if zero_idx == -1 or one_idx == -1:
		largest == ''.join(bits[:] + ['0'])
	else:
		largest = bits[:]
		largest[one_idx] = '0'
		largest[zero_idx] = '1'
		largest = ''.join(largest)
	return(smallest, largest)
			
	
print(next_number(8))
print(next_number(184))
print(next_number(10345))
print(next_number(0))
print(next_number(1))
print(next_number(8383388))

