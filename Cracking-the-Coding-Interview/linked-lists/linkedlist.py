class Node:
	def __init__(self, value):
		self.value = value
		self.child = None
		self.parent = None

class LinkedList():
	def __init__(self, values=None):
		self.values = values
		self.head = None
		self.tail = None
		self.len = 0
		if type(values) is list:
			self.add_many(values)
		elif values:
			self.add_(values)

	def add(self, value):
		new_node = Node(value)
		self.len += 1
		if self.head:
			self.tail.child = new_node
			self.tail = new_node
		else:
			self.head = new_node
			self.tail = new_node

	def add_many(self, values):
		for value in values:
			self.add(value)

	def display(self):
		node = self.head
		i = 0
		while node:
			print("node {} : {}".format(i, node.value))
			i += 1
			node = node.child

class DoublyLinkedList(LinkedList):
	def add(self, value):
		new_node = Node(value)
		if self.head:
			self.tail.child = new_node
			new_node.parent = self.tail
			self.tail = new_node
		else:
			self.head = new_node
			self.tail = new_node
