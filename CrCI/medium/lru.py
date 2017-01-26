# adds item in constant time
# gets item in n time
class Node:
	def __init__(self, key, value, child, parent):
		self.value = value
		self.child = child
		self.key = key
		self.parent = parent

class LRU:
	def __init__(self, key, value, max_size):
		self.max_size = max_size
		self.head = Node(key, value, None, None)
		self.tail = Node('tail', None, None, self.head)
		self.head.child = self.tail
		self.items = {}
		self.items[key] = self.head
		self.items['tail'] = self.tail

	def add_item(self, key, value):
		new_node = Node(key, value, self.head, None)
		self.head.parent = new_node
		self.head = new_node
		self.items[key] = new_node
		if len(self.items) > self.max_size:
			print('removing item')
			removed_key = self.tail.key
			self.tail = self.tail.parent
			self.tail.child = None
			del self.items[removed_key]
		return value

	def get_item(self, key):
		current_node = self.items[key]
		current_node.child.parent = current_node.parent
		current_node.parent = None
		current_node.child = self.head
		self.head.parent = current_node
		self.head = current_node
		return current_node.value

	def print_status(self):
		print('head: ', self.head.key, 'tail: ', self.tail.key)

	def print_lru(self):
		for key, node in self.items.items():
			print(node)
			print(node.key, node.value)

lru = LRU('a', 1, 3)
lru.add_item('b', 2)
lru.add_item('c', 3)
lru.print_status()
print(lru.get_item('b') == 2)
lru.add_item('d', 4)
lru.get_item('b')
lru.print_status()
lru.print_lru()
