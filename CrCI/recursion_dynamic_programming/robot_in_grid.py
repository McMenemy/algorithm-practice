def path_finder(maze, path=[], i=0, j=0):
	rows = len(maze)
	cols = len(maze[0])
	if maze[i][j] == 'blocked' or i >= rows or j >= cols:
		return False
	if maze[i][j] == 'finished':
		return True
	if i + 1 < rows and path_finder(maze, path, i+1, j):
		path.append('down')
	elif j + 1 < cols and path_finder(maze, path, i, j+1): 
		path.append('left')
	return path[::-1]

print(path_finder([['open', 'blocked'], ['open', 'finished']]))
maze = [['opened ', 'opened ', 'opened ', 'opened '],
		['opened ', 'blocked', 'blocked', 'blocked'],
		['opened ', 'opened ', 'opened ', 'blocked'],
		['opened ', 'blocked', 'opened ', 'finished']]

print(path_finder(maze, path=[], i=0, j=0))
