from Stack import Stack

class Que:
	def __init__(self, values=None):
		self.outbox = Stack()
		self.inbox = Stack(values)

	def clear_inbox(self):
		while not self.inbox.is_empty():
			value = self.inbox.pop()
			self.outbox.push(value)

	def add(self, value):
		return self.inbox.push(value)

	def remove(self):
		if self.outbox.is_empty():
			self.clear_inbox()
		return self.outbox.pop()
	
	def is_empty(self):
		return self.inbox.is_empty() and self.outbox.is_empty()

	def display(self):
		self.clear_inbox()
		self.outbox.display()
