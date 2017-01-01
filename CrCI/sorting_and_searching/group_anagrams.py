def group_anagrams(words):
	return sorted(words, key=lambda word: sorted(word))

print(group_anagrams(['cinema', 'howdy', 'cinema', 'cinemb', 'dowhy', 'iceman']))
