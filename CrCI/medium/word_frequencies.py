from collections import defaultdict

def make_text_dict(text):
	word_dict = defaultdict(int)
	for word in text:
		word_dict[word] += 1
	return word_dict

def word_frequencies(target, text):
	if type(text) == 'str':
		count = 0
		for word in text:
			if word == target:
				count += 1
		return count
	return text[word]

text = "I took the road less traveled and that has made all the difference"
print(word_frequencies("the", text) == 2)
text_dict = make_text_dict(text)
print(word_frequencies("all", text_dict) == 1)
