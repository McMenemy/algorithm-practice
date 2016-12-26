from LinkedList import DoublyLinkedList

def return_k_to_last(llist, k):
	node = llist.tail
	for i in range(0, k):
		node = node.parent
		if not node:
			return None
	
	return node.value

dlList = DoublyLinkedList([1, 2, 3, 4])
print(return_k_to_last(dlList, 2) == 2)
