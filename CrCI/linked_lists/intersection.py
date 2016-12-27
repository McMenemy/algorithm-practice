from LinkedList import LinkedList

def find_intersecting_node(longer, shorter):
	diff = longer.len - shorter.len
	longer_node = longer.head
	shorter_node = shorter.head

	for i in range(0, diff):
		longer_node = longer_node.child
	
	while longer_node is not shorter_node:
		longer_node = longer_node.child
		shorter_node = shorter_node.child

	return longer_node

def intersection(lList1, lList2):
	if lList1.tail != lList2.tail:
		return False

	if lList1.len >= lList2.len:
		return find_intersecting_node(lList1, lList2)
	else:
		return find_intersecting_node(lList2, lList1)
