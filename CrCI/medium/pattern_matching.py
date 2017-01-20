import math

def pattern_does_match(pattern, value, a, b):
	i = 0
	for letter in value:
		if letter == 'a':
			if pattern[i:i+len(a)] != a:
				return False
			i += len(a)
		elif letter == 'b':
			if pattern[i:i+len(b)] != b:
				return False
			i += len(b)
	return True

def pattern_matching(pattern, value):
	a_count = value.count('a')
	b_count = value.count('b')
	max_a_len = int((len(pattern) - b_count) / a_count)
	as_before_b = 0
	for letter in value:
		if letter == 'a':
			as_before_b += 1
		else:
			break
	
	for a_len in range(1, max_a_len + 1):
		a = pattern[0:a_len]
		b_len = (len(pattern) - a_count * a_len) / b_count
		if b_len.is_integer():
			b_start = as_before_b * a_len
			b = pattern[b_start:b_start+int(b_len)]
			if pattern_does_match(pattern, value, a, b):
				return True
	return False

print(pattern_matching('catcatgocatgo', 'aabab'))
print(pattern_matching('catcatgocatgo', 'abab'))
print(pattern_matching('catkatgocatgo', 'abab'))
