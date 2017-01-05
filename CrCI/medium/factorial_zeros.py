import math

def factorial_zeros(n):
	five_count = 0
	m = 5
	while m <= n:
		five_count += math.floor(n / m)
		m *= 5
	return five_count

print(factorial_zeros(10) == 2)
print(factorial_zeros(14) == 2)
print(factorial_zeros(15) == 3)
print(factorial_zeros(24) == 4)
print(factorial_zeros(25) == 6)
print(factorial_zeros(26) == 6)
