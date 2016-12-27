class LinkedList:
	def __init__(self, node):
		self.head = node
	
	def render(self):
		node = self.head
		while node:
			print(node.value)
			node = node.child

class Node:
	def __init__(self, value):
		self.value = value
		self.child = None
		self.parent = None

def remove_dups(linked_list):
	seen = { linked_list.head.value: linked_list.head.value }

	node = linked_list.head.child
	while node:
		if node.value in seen:
			node.parent.child = node.child

			if node.child:
				node.child.parent = node.parent

		seen[node.value] = node.value
		node = node.child

	return linked_list

def remove_dups_2(linked_list):
	node = linked_list.head
	while node:
		current_val = node.value
		runner = node.child
		while runner:
			if runner.value == node.value:
				runner.parent.child = runner.child
				if runner.child:
					runner.child.parent = node.parent

			runner = runner.child

		node = node.child

	return linked_list
		

head = Node(1)
head.child = Node(2)
head.child.parent = head
head.child.child = Node(2)
head.child.child.parent = head.child

l_list = LinkedList(head)
l_list.render()
print('----')
new_list = remove_dups_2(l_list)
new_list.render()
