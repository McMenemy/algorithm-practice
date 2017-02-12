def height(person):
	return person['height']

def circus_tower(people):
	people_by_height = sorted(people, key=height)
	stacks = [[people[0]]]
	for person in people_by_height:
		have_stacked = False
		for stack in stacks:
			if stack[-1]['weight'] < person['weight']:
				stack.append(person)
				have_stacked = True
		if not have_stacked:
			stacks.append([person])
	max_stack = []
	for stack in stacks:
		if len(stack) > len(max_stack):
			max_stack = stack
	return max_stack

people = [{'height': 65, 'weight': 100}, {'height': 70, 'weight': 150}, {'height': 56, 'weight': 90},
		{'height': 75, 'weight': 190}, {'height': 60, 'weight': 96}, {'height': 68, 'weight': 110}]

print(circus_tower(people))
