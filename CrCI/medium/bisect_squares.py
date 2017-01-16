def find_square_center(square):
	# { corner: { x: 1, y: 2 }, s: 5 }
	center = {}
	center['x'] = square['corner']['x'] - square['s'] / 2
	center['y'] = square['corner']['y'] - square['s'] / 2
	return center

def bisect_squares(square1, square2):
	center1 = find_square_center(square1)
	center2 = find_square_center(square2)
	if center1['x'] == center2['x']:
		return 'x = ' +  str(center1['x'])
	if center1['y'] == center2['y']:
		return 'y = ' + str(center1['y'])
	slope = (center1['x'] - center2['x']) / (center1['y'] - center2['y'])
	y_int = center1['y'] - slope * center1['x']
	return str(slope) + ' * x + ' + str(y_int) + ' = y' 

square1 = { 'corner': { 'x': 11, 'y': 2 }, 's': 4 }
square2 = { 'corner': { 'x': -3, 'y': 6.4 }, 's': 5 }
print(bisect_squares(square1, square2))
