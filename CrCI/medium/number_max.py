def number_max(num1, num2):
	return ((num1 + num2) + abs(num1 - num2) ) / 2;

print(number_max(5, 4) == 5)
print(number_max(4, 5) == 5)
print(number_max(-12, -11) == -11)
print(number_max(-10, 0) == 0)
print(number_max(2, 2) == 2)
