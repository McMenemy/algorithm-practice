class Node:
	def __init__(self, value):
		self.value = value
		self.children = []

class Trie:
	def __init__(self, words):
		self.root = Node('')
		self.add_children(words)

	def add_children(self, words):
		for word in words:
			current_node = self.root
			for letter in word:
				if letter not in [node.value for node in current_node.children]:
					new_node = Node(letter)
					current_node.children.append(new_node)
					current_node = new_node
			if 'end' not in [node.value for node in current_node.children]:
				current_node.children.append('end')

def t9(digits, word_trie, mappings):
	possibilities = [{ 'path': '', 'node': word_trie.root }]
	for digit in digits:
		new_possibilities = []
		for p in possibilities:
			for letter in mappings[digit]:
				for node in p['node'].children:
					if node.value == letter:
						new_possibilities.append({ 'path': p['path'] + letter, 'node': node })
						break
		possibilities = new_possibilities
	return list([p['path'] for p in possibilities])

word_trie = Trie(['tree', 'used', 'useful'])
digits = '8733'
mappings = {
		'1': '',
		'2': 'abc',
		'3': 'def',
		'4': 'ghi',
		'5': 'jkl',
		'6': 'mno',
		'7': 'pqrs',
		'8': 'tuv',
		'9': 'wxyz'
	}
print(t9(digits, word_trie, mappings))




