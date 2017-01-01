import math

def magic_number(arr):
	if len(arr) == 0:
		return False
	mid_idx = math.floor(len(arr) / 2)
	mid_val = arr[mid_idx]
	if mid_val == mid_idx:
		return mid_val
	elif mid_val < mid_idx:
		return mid_idx + 1 + magic_number(arr[mid_idx + 1:])
	elif mid_val > mid_idx:
		return magic_number(arr[0:mid_idx])

print(magic_number([-2, -1, 0, 3, 5]) == 3)
