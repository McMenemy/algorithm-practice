# brute force O(n^2) 
def two_count(num):
	count = 0
	for i in range(num+1):
		count += str(i).count('2')
	return count

# optimized O(n)
def two_count_o(num):
	count = 0
	str_num = str(num)
	for i, digit in enumerate(str_num):
		power = 10**(i)
		nextPower = power * 10
		under = num - num % nextPower
		over = under + nextPower
		if int(digit) < 2:
			count += under / 10   
		elif int(digit) > 2:
			count += over / 10
		elif int(difit) == 2:
			right = num % power
			count += under + right + 1
	return int(count)

print(two_count(555))
print(two_count(111))
print(two_count(55))
print(two_count(99))
print(two_count(555))
print(two_count(999))
print(two_count(5555))
print(two_count(9999))

print('--')

print(two_count_o(555))
print(two_count_o(111))
print(two_count_o(55))
print(two_count_o(99))
print(two_count_o(555))
print(two_count_o(999))
print(two_count_o(5555))
print(two_count_o(9999))
