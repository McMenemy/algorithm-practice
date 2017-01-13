def conversion(start_int, end_int):
	return ('{0:b}'.format(start_int ^ end_int)).count('1')

print(conversion(29, 15))
