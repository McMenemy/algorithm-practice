def most_living_people(people_list):
	population_dict = {i: 0 for i in range(1900, 2001)}
	for dates in people_list.values():
		for i in range(dates[0], dates[1] + 1):
			population_dict[i] += 1
	return max(population_dict, key=lambda key: population_dict[key])

people = {
		'bob': [1901, 1920],
		'jim': [1920, 1969],
		'jeff': [1908, 1933],
		'stacey': [1920, False],
		'bernie': [1964, 2000]
		}

print(most_living_people(people))
