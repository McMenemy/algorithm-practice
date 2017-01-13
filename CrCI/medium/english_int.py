import math

def convert(number):
	str_num = str(number)
	ones_teens = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
				'eleven', 'twelve', 'thirteen', 'fourteen', 'fifthteen', 'sixteen', 'seventeen',
				'eighteen', 'nineteen']
	tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
	if number <= 19:
		return ones_teens[number - 1]
	elif number > 19 and number <= 99:
		ten = int(str_num[0])
		one_teen = int(str_num[1])
		if one_teen == 0:
			return tens[ten - 2]
		else:
			return tens[ten - 2] + '-' + ones_teens[one_teen - 1]
	else:
		hundred = int(str_num[0])
		remainder = int(str_num[1:])
		return ones_teens[hundred - 1] + ' hundred' + ' ' + convert(remainder)	

def english_int(integer):
	groupings = ['', ' thousand ', ' million ', ' billion ']
	str_num = str(integer)
	group_range = math.ceil(len(str_num) / 3)
	result = ''
	for i in range(0, group_range):
		start = i * 3
		result = convert(int(str_num[start:start+3])) + groupings[i] + result
	return result


print(english_int(1))
print(english_int(12))
print(english_int(42))
print(english_int(190))
print(english_int(198536142))
