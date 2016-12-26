from LinkedList import LinkedList

def partition(lList, cutoff):
	node = lList.head
	left = []
	right = []
	while node:
		if node.value < cutoff:
			left.append(node.value)
		elif node.value >= cutoff:
			right.append(node.value)
		
		node = node.child

	return LinkedList(left + right)

lList = LinkedList([3, 5, 8, 5, 10, 2, 1])
partioned_list = partition(lList, 5)
partioned_list.display()
