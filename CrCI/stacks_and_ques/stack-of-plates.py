from Stack import Stack

class SetOfStacks:
	def __init__(self, substack_size, values=None):
		self.substack_size = substack_size
		self.stacks = [Stack()]
		if values:
			self.add_values(values[::-1])

	def add_values(self, values):
		while len(values) > 0:
			self.push(values.pop())

	def push(self, value):
		current_stack = self.stacks[-1]
		if current_stack.len >= self.substack_size:
			current_stack = Stack()
			self.stacks.append(current_stack)
		return current_stack.push(value)

	def pop(self):
		current_stack = self.stacks[-1]
		popped_val = current_stack.pop()
		if current_stack.is_empty():
			self.stacks.pop()
		return popped_val

	def peek(self):
		return self.stacks[-1].peek()

	def pop_at_index(self, idx):
		if abs(idx) >= len(self.stacks):
			return None
		current_stack = self.stacks[idx]
		return current_stack.pop()
			
		
sStacks = SetOfStacks(3, [1, 2, 3, 4, 5, 6, 7, 8])
print(sStacks.peek())
print(sStacks.pop() == 8)
print(sStacks.pop() == 7)
print(sStacks.pop() == 6)
sStacks.push(6)
print(sStacks.peek() == 6)
sStacks.push(7)
print(sStacks.peek() == 7)
print(sStacks.pop_at_index(0) == 3)
print(sStacks.pop_at_index(5) == None)
