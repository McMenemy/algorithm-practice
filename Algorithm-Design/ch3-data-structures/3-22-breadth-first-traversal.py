import math

class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, array):
        self.root = self.create_tree(array)

    def create_tree(self, array):
        if len(array) == 1:
            return Node(array[0])

        if len(array) == 0:
            return None

        mid = math.floor(len(array) / 2)
        parent = Node(array[mid])
        parent.left = self.create_tree(array[0:mid])
        parent.right = self.create_tree(array[mid+1:])

        return parent

    def breadth_traversal(self):
        children = [self.root]

        while len(children) > 0:
            child = children.pop(0)
            print(child.value)
            if child.left:
                children.append(child.left)

            if child.right:
                children.append(child.right)

tree = BinaryTree([1, 2, 3, 4, 5, 6, 7])
tree.breadth_traversal()
