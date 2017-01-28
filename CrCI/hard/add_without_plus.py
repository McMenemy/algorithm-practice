# only handles positive numbers a few more if statements would fix this
def add(num1, num2):
	if num1 >= num2:
		bits1 = '{0:b}'.format(num1)[::-1]
		bits2 = '{0:b}'.format(num2)[::-1]
	else:
		bits1 = '{0:b}'.format(num2)[::-1]
		bits2 = '{0:b}'.format(num1)[::-1]
	
	carry = '0'
	result = ''
	for i, bit1 in enumerate(bits1):
		if i >= len(bits2):
			bit2 = '0'
		else:
			bit2 = bits2[i]

		current = "{}{}{}".format(bit1, bit2, carry)
		if current.count('1') == 0:
			carry = '0'
			result = "{}{}".format('0', result)
		elif current.count('1') == 1:
			carry = '0'
			result = "{}{}".format('1', result)
		elif current.count('1') == 2:
			carry = '1'
			result = "{}{}".format('0', result)
		elif current.count('1') == 3:
			carry = '1'
			result = "{}{}".format('1', result)

	result = "{}{}".format(carry, result)
	return int(result, 2)

print(add(10, 11))
print(add(1214, 13))
