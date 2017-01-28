import random

def random_set(m, array):
	result = []
	for i, item in enumerate(array):
		if i < m:
			result.append(item)
		else:
			k = random.randint(0, i)
			if k < m:
				result[k] = item
	return result

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(5):
	print(random_set(i, arr))
