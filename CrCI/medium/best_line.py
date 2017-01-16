def calc_line(point1, point2):
	slope = (point2['x'] - point1['x']) / (point2['y'] - point1['y'])
	y_int = point1['y'] - (slope * point1['x'])
	return { 'y_int': y_int, 'slope': slope }

def is_point_on_line(point, line):
	return line['slope'] * point['x'] + line['y_int'] == point['y']

def best_line(points):
	max_point_count = 0
	best_line = {}
	for i, point1 in enumerate(points):
		for point2 in points[i + 1:]:
			line = calc_line(point1, point2)
			point_count = 0
			for point in points:
				if is_point_on_line(point, line):
					point_count += 1
			if point_count > max_point_count:
				max_point_count = point_count
				best_line = line
	return best_line

points = [{'x':3, 'y':4}, {'x':2, 'y':3}, {'x':2, 'y':-2}, {'x':5, 'y':6}] 
print(best_line(points))
