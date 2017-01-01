import math

def find_in_rotated_array(array, target):
	if len(array) == 0 or (len(array) == 1 and array[0] != target):
		return False

	mid_idx = math.floor(len(array) / 2)
	mid_val = array[mid_idx]
	if mid_val == target:
		return mid_idx
	elif array[0] == target:
		return 0
	elif array[-1] == target:
		return len(array) - 1
	elif mid_val > target and array[0] > target:
		return mid_idx + 1 + find_in_rotated_array(array[mid_idx + 1:], target)
	elif mid_val > target and array[0] < target:
		return find_in_rotated_array(array[0:mid_idx], target)
	elif mid_val < target and array[-1] > target:
		return mid_idx + 1 + find_in_rotated_array(array[mid_idx + 1:], target)
	elif mid_val < target and array[-1] < target:
		return find_in_rotated_array(array[0:mid_idx], target)

nums = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]

print(find_in_rotated_array(nums, 5) == 8)
print(find_in_rotated_array(nums, 15) == 0)
print(find_in_rotated_array(nums, 14) == 11)
print(find_in_rotated_array(nums, 19) == 2)
