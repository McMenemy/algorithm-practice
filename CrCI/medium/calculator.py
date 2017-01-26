def solve(num1, num2, operation):
	if operation == '+':
		return str(int(num1) + int(num2))
	elif operation == '-':
		return str(int(num1) - int(num2))
	elif operation == '/':
		return str(round(int(num1) / int(num2)))
	elif operation == '*':
		return str(int(num1) * int(num2))

def calc(equation):
	if '*' not in equation and '/' not in equation and '+' not in equation and '-' not in equation:
		return int(equation)

	digits = '0123456789'
	operators = '+-/*'
	left_num = ''
	right_num = ''
	is_left_side = True
	operation = ''
	start = 0
	for i, char in enumerate(equation):
		if left_num == '':
			left_num += char
			start = i
		elif is_left_side and char in digits:
			left_num += char
		elif is_left_side and (char == '*' or char == '/'):
			operation = char
			is_left_side = False
		elif is_left_side and (char == '+' or char == '-'):
			left_num = ''
		elif char in digits:
			right_num += char
		else: # mean an operator was hit and right num is finished
			left = equation[0:start]
			right = equation[i:]
			return calc(left + solve(left_num, right_num, operation) + right)
	if left_num and right_num and operation:
		left = equation[0:start]
		right = ''
		return calc(left + solve(left_num, right_num, operation) + right)
		
	
	left_num = ''
	right_num = ''
	is_left_side = True
	for i, char in enumerate(equation):
		if left_num == '':
			left_num += char
			start = i
		elif is_left_side and char in digits:
			left_num += char
		elif is_left_side and (char == '+' or char == '-'):
			operation = char
			is_left_side = False
		elif char in digits:
			right_num += char
		else: 
			left = equation[0:start]
			right = equation[i:]
			return calc(left + solve(left_num, right_num, operation) + right)
	if left_num and right_num and operation:
		left = equation[0:start]
		right = ''
		return calc(left + solve(left_num, right_num, operation) + right)

print(calc('2*3+5/6*3+15'))
