from collections import deque

def baby_names(count_dict, name_pairs):
	combined_counts = {}
	checked_names = []
	for name in count_dict.keys():
		if name not in checked_names:
			que = deque([name])
			count = 0
			while len(que) > 0:
				current_name = que.popleft()
				checked_names.append(current_name)
				if current_name in count_dict:
					count += count_dict[current_name]
				for pair in name_pairs:
					if pair[0] == current_name and pair[1] not in checked_names:
						que.append(pair[1])
					elif pair[1] == current_name and pair[0] not in checked_names:
						que.append(pair[0])
			combined_counts[name] = count
	return combined_counts

count_dict = { "John": 15, "Jon": 12, "Chris": 13, "Kris": 4, "Christopher": 19 }
name_pairs = [("Jon", "John"), ("John", "Johnny"), ("Chris", "Kris"), ("Chris", "Christopher")]
print(baby_names(count_dict, name_pairs))
