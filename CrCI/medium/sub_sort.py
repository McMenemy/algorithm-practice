def sub_sort(nums):
	front_pivot = -1
	for i, num in enumerate(nums[::-1]):
		next_ind = len(nums) - 2 - i
		if next_ind >= 0 and num < nums[next_ind]:
			front_pivot = num
			break
	back_pivot = -1
	for i, num in enumerate(nums[:-1]):
		if nums[i] > nums[i+1]:
			back_pivot = nums[i]
			break
	if front_pivot == -1 and back_pivot == -1:
		return 'already sorted'
	start_idx = 0
	while nums[start_idx] <= front_pivot:
		start_idx += 1
	end_idx = len(nums) - 1
	while nums[end_idx] > back_pivot:
		end_idx -= 1
	return [start_idx, end_idx]

print(sub_sort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]))
print(sub_sort([1, 2, 4, 7, 10, 11]))
print(sub_sort([1, 2, 4, 3, 2, 7, 10, 11]))
