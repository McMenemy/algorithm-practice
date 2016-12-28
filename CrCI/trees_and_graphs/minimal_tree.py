class Node:
	def __init__(self, value):
		self.value = value
		self.children = []
		
	def add_children(self, nodes):
		self.children += nodes

def make_min_tree(sorted_array):
	nodes = [Node(value) for value in sorted_array]
	for i, node in enumerate(nodes):
		child1_idx = 2 * i + 1
		child2_idx = 2 * i + 2
		children = []
		if child1_idx < len(nodes):
			children.append(nodes[child1_idx])
		if child2_idx < len(nodes):
			children.append(nodes[child2_idx])
		node.add_children(children)
	return nodes[0]


min_tree = make_min_tree([0, 1, 2, 3, 4, 5, 6, 7])
print(min_tree.children[0].value == 1)
print(min_tree.children[1].value == 2)
print(min_tree.children[0].children[1].value == 4)
print(min_tree.children[1].children[0].value == 5)
print(min_tree.children[0].children[0].children[0].value == 7)
