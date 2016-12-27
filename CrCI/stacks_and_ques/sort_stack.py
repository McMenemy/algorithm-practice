from Stack import Stack

class SortStack():
	def __init__(self):
		self.temp = Stack()
		self.stack = Stack()

	def push(self, value):
		while not self.stack.is_empty() and value > self.stack.peek():
			self.temp.push(self.stack.pop())
		self.stack.push(value)
		while not self.temp.is_empty():
			self.stack.push(self.temp.pop())
		return value

	def peek(self):
		if self.stack.is_empty():
			return None
		return self.stack.peek()

	def is_empty(self):
		return self.stack.is_empty()

	def pop(self):
		return self.stack.pop()

	def display(self):
		return self.stack.display()
		
sort_stack = SortStack()
for i in range(0, 5):
	sort_stack.push(i)

sort_stack.display()

print(sort_stack.peek() == 0)
sort_stack.push(7)
print(sort_stack.pop() == 0)
print(sort_stack.peek() == 1)


