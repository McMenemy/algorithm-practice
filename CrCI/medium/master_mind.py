def master_mind(actual, guess):
	actual_dict = { 'R': 0, 'G': 0, 'Y': 0, 'B': 0 } 
	guess_dict = { 'R': 0, 'G': 0, 'Y': 0, 'B': 0 } 
	hits = 0
	for i, color in enumerate(actual):
		current_guess = guess[i]
		if color == current_guess:
			hits += 1
		else:
			actual_dict[color] += 1
			guess_dict[current_guess] += 1
	pseudo_hits = 0
	for color, actual_value in actual_dict.items():
		if actual_value >= guess_dict[color]:
			pseudo_hits += guess_dict[color]
		else:
			pseudo_hits += actual_value
	return [hits, pseudo_hits]

print(master_mind('YBGR', 'GBRB'))
