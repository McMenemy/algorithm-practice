import math

def b_search(nums, target):
	if len(nums) == 0:
		return False
	
	mid_ind = math.floor(len(nums) / 2)
	mid_val = nums[mid_ind]

	if mid_val == target:
		return True
	elif mid_val > target:
		return b_search(nums[0:mid_ind], target)
	elif mid_val < target:
		return b_search(nums[mid_ind+1:], target)


def sum_swap(arr1, arr2):
	target_diff = (sum(arr1) - sum(arr2)) / 2
	arr2_sorted = sorted(arr2)
	for num in arr1:
		target = num - target_diff
		result = b_search(arr2_sorted, target)
		if result:
			return [num, int(target)]
	return False

arr1 = [4, 1,2, 1, 1, 2]
arr2 = [3, 6, 3, 3]

print(sum_swap(arr1, arr2))


