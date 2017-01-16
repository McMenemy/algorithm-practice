def flip_sign(num):
	if num < 0:
		return int(str(num)[1:])
	else:
		return int('-' + str(num))

def subtract(num1, num2):
	return num1 + flip_sign(num2)

def multiply(num1, num2):
	if num2 < 0:
		num1 = flip_sign(num1)
	result = 0
	end = num2 if num2 >= 0 else flip_sign(num2)
	for i in range(0, end):
		result += num1
	return result

def divide(num1, num2):
	if num2 == 0:
		return 'divide by zero error'
	result = 0
	remainder = num1 if num1 >= 0 else flip_sign(num1)
	while remainder >= num2:
		result += 1
		remainder = subtract(remainder, num2)
	if (num1 <= 0 and num2 < 0) or (num1 >= 0 and num2 > 0):
		return result
	if (num1 <= 0 and num2 > 0) or (num1 >= 0 and num2 < 0):
		return flip_sign(result)

print(flip_sign(-1) == 1)
print(flip_sign(5) == -5)
print(subtract(5, 8) == -3)
print(subtract(8, 5) == 3)
print(multiply(5, 4) == 20)
print(multiply(3, -4) == -12)
print(multiply(-5, -5) == 25)
print(multiply(-2, 1) == -2)
print(divide(8, 4) == 2)
print(divide(-12, 3) == -4)
print(divide(3, 12) == 0)
