def find_pond_size(start, layout, memo):
	que = [start]
	size = 0
	rows = len(layout)
	cols = len(layout[0])
	while que:
		size += 1
		coord = que.pop()
		r = coord[0]
		c = coord[1]
		deltas = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
		for delta in deltas:
			new_r = r + delta[0]
			new_c = c + delta[1]
			if new_r >= 0 and new_r < rows and new_c >= 0 and new_c < cols and memo[new_r][new_c]:
				memo[new_r][new_c] = False
				if layout[new_r][new_c] == 0:
					que.append([new_r, new_c])
	return size

def pond_sizes(layout):
	rows = len(layout)
	cols = len(layout[0])
	memo = list([[True for i in range(0, cols)] for j in range(0, rows)])
	sizes = []
	for r, row in enumerate(layout):
		for c, plot in enumerate(row):
			if memo[r][c]:
				memo[r][c] = False
				if plot == 0:
					sizes.append(find_pond_size([r, c], layout, memo))
	return sizes

pond = [[0, 2, 1, 0],
		[0, 1, 0, 1],
		[1, 1, 0, 1],
		[0, 1, 0, 1]]

print(pond_sizes(pond))
