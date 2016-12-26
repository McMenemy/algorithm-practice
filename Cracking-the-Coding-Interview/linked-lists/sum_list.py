from LinkedList import LinkedList

def get_num(list):
	num = ''
	node = list.head
	while node:
		num = str(node.value) + num
		node = node.child
	
	return int(num)

def sum_list(list1, list2):
	rev_sum_string = str(get_num(list1) + get_num(list2))[::-1]

	return LinkedList([int(num) for num in rev_sum_string])

def get_num_fwd(list):
	num = ''
	node = list.head
	while node:
		num += str(node.value)
		node = node.child

	return int(num)

def sum_list_fwd(list1, list2):
	sum_string = str(get_num_fwd(list1) + get_num_fwd(list2))
	return LinkedList([int(num) for num in sum_string])


list1 = LinkedList([7, 1, 6])
list2 = LinkedList([5, 9, 2])
sum = sum_list(list1, list2)
sum.display()

list1 = LinkedList([6, 1, 7])
list2 = LinkedList([2, 9, 5])
sum = sum_list_fwd(list1, list2)
sum.display()
