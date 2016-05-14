class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self, root):
        self.root = root

    def append(self, value):
        node = self.root
        new_node = Node(value, node)
        self.root = new_node
        return new_node

    def print_list(self):
        current_node = self.root
        next_node = self.root.next
        print(current_node.value)

        while next_node != None:
            current_node = current_node.next
            next_node = next_node.next
            print(current_node.value)

    def find_node(self, value):
        current_node = self.root
        next_node = self.root.next

        while next_node != None:
            if current_node.value == value:
                return current_node
            current_node = current_node.next
            next_node = next_node.next


def has_loop(linked_list):
    walker = linked_list.root
    runner = linked_list.root.next

    while True:
        print('walker', walker)
        print('runner', runner)
        if walker == runner:
            return True
        elif runner == None:
            break

        runner = runner.next

        print('walker', walker)
        print('runner', runner)
        if walker == runner:
            return True
        elif runner == None:
            break

        runner = runner.next
        walker = walker.next

    return False

init = Node(5)
linked_list = LinkedList(init)
linked_list.append(4)
linked_list.append(3)
linked_list.append(2)
linked_list.append(1)
linked_list.print_list()
print(has_loop(linked_list))

node3 = linked_list.find_node(3)
print(node3.value)
node1 = linked_list.find_node(1)
node3.next = node1

# linked_list.print_list()
print(has_loop(linked_list))
