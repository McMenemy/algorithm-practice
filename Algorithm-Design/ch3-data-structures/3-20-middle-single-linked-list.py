class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class SingleLinkedList:
    def __init__(self, root_node):
        self.root = root_node

    def insert(self, node):
        node.next = self.root.next
        self.root.next = node

    def mid(self):
        runner = self.root
        walker = self.root
        while True:
            runner = runner.next
            if runner == None:
                return walker

            walker = walker.next

            runner = runner.next
            if runner == None:
                return walker

root_node = Node(1)
sl_list = SingleLinkedList(root_node)
sl_list.insert(Node(5))
sl_list.insert(Node(4))
sl_list.insert(Node(3))
sl_list.insert(Node(2))

print(sl_list.root)
print(sl_list.root.next)
print(sl_list.mid().value)
