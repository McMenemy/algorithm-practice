from linkedlist import DoublyLinkedList

class Stack(DoublyLinkedList):
	def pop(self):
		payload = self.tail.value
		self.len -= 1
		if self.tail.parent:
			self.tail.parent.child = None
			self.tail = self.tail.parent
		else:
			self.tail = None
		return payload

	def push(self, value):
		self.add(value)
		return value

	def peek(self):
		return self.tail.value

	def is_empty(self):
		return self.tail == None
