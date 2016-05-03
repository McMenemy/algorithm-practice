# use a prefix tree

class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

class PreFixTree:
    def __init__(self):
        self.root = Node('', {})

    def add(self, value):
        current = self.root
        i = 0
        key = value[i]
        while key in current.next:
            current = current.next[key]
            i += 1
            key = value[i]

        print(value[i:])
        for char in value[i:]:
            new_node = Node(char, {})
            current.next[char] = new_node
            current = new_node

tree = PreFixTree()
tree.add('www.google.com')
tree.add('www.yahoo.com')
tree.add('msn.com')
tree.add('w.com')
