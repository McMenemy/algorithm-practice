from LinkedList import LinkedList

def palindrome(lList):
	values = []
	walker = runner = lList.head
	while runner and runner.child:
		values.append(walker.value)
		walker = walker.child
		runner = runner.child.child

	if runner:
		walker = walker.child

	while walker:
		if walker.value != values.pop():
			return False
		walker = walker.child

	return True

ll_true = LinkedList([1, 2, 3, 4, 5, 4, 3, 2, 1])
print(palindrome(ll_true))
ll_false = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(palindrome(ll_false))
