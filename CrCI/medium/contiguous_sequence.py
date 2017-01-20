def contig_seq(nums):
	current_sum = nums[0]
	max_sum = float('-inf')
	prev_sum = nums[0]
	for i, num in enumerate(nums[1:]):
		if num >= 0:
			current_sum += num
		elif num < 0 and nums[i] >= 0:
			if prev_sum < current_sum:
				prev_sum = current_sum
			current_sum = 0

		if prev_sum > max_sum:
			max_sum = prev_sum
		if current_sum > max_sum:
			max_sum = current_sum
		if num > max_sum:
			max_sum = num
		prev_sum += num

	return max_sum

print(contig_seq([2, -8, 3, -2, 4, -10]))
print(contig_seq([4, -1, -2, 5, 2, -10]))
print(contig_seq([-11, -2, -10]))
