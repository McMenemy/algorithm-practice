def calc_line(segment):
	if segment['x1'] == segment['x2']:
		slope = 0
	else:
		slope = (segment['y2'] - segment['y1']) / (segment['x2'] - segment['x1'])
	y_int = segment['y1'] - slope * segment['x1']
	return slope, y_int

def is_on_segment(segment, point):
	if segment['x1'] >= segment['x2']:
		left_most = segment['x2']
		right_most = segment['x1']
	else:
		left_most = segment['x1']
		right_most = segment['x2']
	
	if segment['y1'] >= segment['y2']:
		up_most = segment['y1']
		down_most = segment['y2']
	else:
		up_most = segment['y2']
		down_most = segment['y1']
	
	x = point['x']
	y = point['y']
	return x >= left_most and x <= right_most and y >= down_most and y <= up_most

def intersection(segment1, segment2):
	slope1, y_int1 = calc_line(segment1)
	slope2, y_int2 = calc_line(segment2)
	if slope1 == slope2:
		return 'parallel'
	x = slope1 - slope2
	remainder = y_int2 - y_int1
	x = remainder / x
	y = x * slope1 + y_int1
	intercept = { 'x': x, 'y': y }
	if is_on_segment(segment1, intercept) and is_on_segment(segment2, intercept):
		return intercept
	return None

seg1 = { 'x1': 1, 'y1': 2, 'x2': 3, 'y2': 4}
seg2 = { 'x1': 0, 'y1': 4, 'x2': 3, 'y2': 0}
seg3 = { 'x1': 0, 'y1': 1, 'x2': 1, 'y2': 0}
print(intersection(seg1, seg2))
print(intersection(seg1, seg3))
	
