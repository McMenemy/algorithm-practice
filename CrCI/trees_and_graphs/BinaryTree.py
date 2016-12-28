from linkedlist import LinkedList
from que_via_stack import Que

class Node:
	def __init__(self, value):
		self.value = value
		self.children = []

	def add_children(self, children):
		self.children += children
	
class BinaryTree:
	def __init__(self, values):
		self.root = self.make_tree(values)

	def make_tree(self, values):
		nodes = [Node(value) for value in values]
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

	def get_layers(self):
		layers = []
		layer = LinkedList([])
		que = Que([self.root])
		i = 0
		layer_idx = 0
		end = 2 ** (layer_idx + 1) - 1
		while not que.is_empty():
			node = que.remove()
			for child in node.children:
				que.add(child)
			if i < end:
				layer.add(node.value)
			else:
				layers.append(layer)
				layer = LinkedList([])
				layer_idx += 1
				end = 2 ** (layer_idx + 1) - 1
			i += 1
		if not layer.is_empty():
			layers.append(layer)
		return layers
