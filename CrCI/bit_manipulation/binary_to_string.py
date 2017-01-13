def double_to_binary(double):
	current = double
	bits = '.'
	for i in range(0, 32):
		if current >= 0.5:
			bits += '1'
		else:
			bits += '0'
		current = (current % 0.5) * 2
		if current == 0:
			return bits
	return 'ERROR'

print(double_to_binary(0.72))
print(double_to_binary(0.5))
print(double_to_binary(0.25))
print(double_to_binary(0.36))
print(double_to_binary(0.36))
print(double_to_binary(0.859375))
