def number_swap(num1, num2):
	num2 = num1 + num2
	num1 = num2 - num1
	num2 = num2 - num1
	return num2

print(number_swap(5, 8) == 5)
print(number_swap(5, -3) == 5)
