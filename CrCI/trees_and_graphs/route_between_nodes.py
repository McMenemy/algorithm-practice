from que_via_stack import Que

class Node:
	def __init__(self, value, children):
		self.value = value
		self.children = children

	def add_children(self, nodes):
		self.children += nodes

def is_route(node1, node2):
	que = Que(node1.children)
	while not que.is_empty():
		currentNode = que.remove()
		if currentNode == node2:
			return True
		for node in currentNode.children:
			que.add(node)
	return False
		
n0 = Node(0, [])
n1 = Node(1, [])
n2 = Node(2, [])
n3 = Node(3, [])
n4 = Node(4, [])
n5 = Node(5, [])
n0.add_children([n5, n4, n1])
n1.add_children([n4, n3])
n2.add_children([n1])
n3.add_children([n2, n4])

print(is_route(n0, n5) == True)
print(is_route(n5, n0) == False)
print(is_route(n0, n3) == True)
