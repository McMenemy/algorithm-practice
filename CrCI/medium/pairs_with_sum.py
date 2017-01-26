from collections import defaultdict

def pairs_with_sum(nums, target):
	nums_hash_map = defaultdict(int)
	pair_sums = []
	for num in nums:
		nums_hash_map[num] += 1
	for num in nums_hash_map:
		current_target = target - num
		if current_target == num and nums_hash_map[num] > 1: # special case if num is half of target
			pair_sums.append([num, num])
			nums_hash_map[num] -= 2
		elif current_target in nums_hash_map and nums_hash_map[current_target] > 0:
			pair_sums.append([num, current_target])
			nums_hash_map[num] -= 1
			nums_hash_map[current_target] -= 1
	return pair_sums

arr = [1, 0, 5, 9, 11, -2, 7, 7, 13]
print(pairs_with_sum(arr, -2))
print(pairs_with_sum(arr, 14))
print(pairs_with_sum(arr, 10))


