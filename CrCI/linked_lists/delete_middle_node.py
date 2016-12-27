from LinkedList import LinkedList

def delete_middle_node(lList, idx):
	i = 0
	is_post_idx = False
	node = lList.head
	while node:
		if i == idx:
			node.value = node.child.value
			is_post_idx = True
		elif is_post_idx and node.child.child == None:
			node.value = node.child.value
			node.child = None
		elif is_post_idx:
			node.value = node.child.value

		node = node.child
		i += 1

	return lList

lList = LinkedList([1, 2, 3, 4, 5])
edited_lList = delete_middle_node(lList, 2)
edited_lList.display()

