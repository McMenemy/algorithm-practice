# brute force O(N^2)
def letters_and_nums_brute(arr):
	max_sub_len = 0
	indexes = [0, 0]
	for i in range(len(arr)):
		letter_count = 0
		num_count = 0
		length = 0
		for j, char in enumerate(arr[i:]):
			length += 1
			if isinstance(char, str):
				letter_count += 1
			else:
				num_count += 1

			if num_count == letter_count and length > max_sub_len:
				max_sub_len = length
				indexs = [i, j+i]
	return indexs

# optimal(N)
def letters_and_nums(arr):
	diff_hash = { 0: { 'min_ind': 0 } }
	letter_count = 0
	num_count = 0
	inds = [0, 0]
	max_length = 0
	for i, char in enumerate(arr):
		if isinstance(char, str):
			letter_count += 1
		else:
			num_count += 1
		diff =  letter_count - num_count
		if diff in diff_hash:
			length = i - diff_hash[diff]['min_ind']
			if length > max_length:
				max_length = length
				inds = [diff_hash[diff]['min_ind'], i]
		else:
			diff_hash[diff] = { 'min_ind': i+1 }
	return inds

arr1 = [1, 2, 3, 'c', 1, 'g', 1, 'a', 'b', 4, 'f', 4, 9, 'c',    'd', 1, 1, 1, 1, 1]
arr2 = ['a', 1, 1, 1, 'a', 1, 'a', 'a', 'a', 1, 1]
print(letters_and_nums_brute(arr1))
print(letters_and_nums(arr1))
print(letters_and_nums_brute(arr2))
print(letters_and_nums(arr2))
