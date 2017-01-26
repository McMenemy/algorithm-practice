import random

def rand5():
	return random.uniform(0, 4)

def rand7():
	return rand5() / 4 * 6
	
for i in range(20):
	print(rand7())
