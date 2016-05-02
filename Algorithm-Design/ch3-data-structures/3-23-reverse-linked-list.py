class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, initial):
        if type(initial) == list:
            self.head = self.create_list(initial)
        elif type(initial) == Node:
            self.head = initial

    def create_list(self, array):
        parent = Node(array[0])
        head = parent
        for el in array[1:]:
            link = Node(el)
            parent.next = link
            parent = link
        return head


def reverse_linked_list(link, prev_link=None):
    if link == None:
        return LinkedList(prev_link)

    next_link = link.next
    link.next = prev_link
    new_head = reverse_linked_list(next_link, link)
    return new_head

def reverse_linked_list2(linked_list):
    prev_link = linked_list.head
    link = prev_link.next
    prev_link.next = None
    while link:
        next_link = link.next
        link.next = prev_link
        prev_link = link
        link = next_link
    linked_list.head = prev_link

def print_list(linked_list):
    link = linked_list.head
    while link:
        print(link.value)
        link = link.next

linked_list = LinkedList([1, 2, 3, 4, 5, 6])
print_list(linked_list)
reversed_list = reverse_linked_list(linked_list.head)
print_list(reversed_list)
reverse_linked_list2(reversed_list)
print_list(reversed_list)
