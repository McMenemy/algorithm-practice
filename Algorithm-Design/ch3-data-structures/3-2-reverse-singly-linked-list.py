class Node:
    def __init__(self, data):
        self.data = data
        self.next = 'none'

class SingleLinkedList:
    def __init__(self, head = 'none'):
        self.head = head

    def insert(self, node):
        if self.head == 'none':
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def find_by_idx(self, idx):
        node = self.head
        for i in range(0, idx):
            node = node.next
            if node == 'none':
                return 'Error: not that many nodes in list'
        return node.data

n5 = Node(5)
n4 = Node(4)
n3 = Node(3)
n2 = Node(2)
n1 = Node(1)

list = SingleLinkedList()
list.insert(n5)
list.insert(n4)
list.insert(n3)
list.insert(n2)
list.insert(n1)

def rev_list(list):
    # base case of one node
    if list.head.next == 'none':
        return list

    node = list.head.next
    prev_node = list.head
    list.head.next = 'none'

    while True:
        next_node = node.next
        node.next = prev_node
        if next_node == 'none':
            list.head = node
            break
        else:
            prev_node = node
            node = next_node

rev_list(list)

print list.find_by_idx(0)
print list.find_by_idx(1)
print list.find_by_idx(2)
print list.find_by_idx(4)
