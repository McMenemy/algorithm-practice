import math

class Node:
    def __init__(self, value):
        self.value = value
        self.right_child = None
        self.left_child = None

class PartialSumTree:
    def __init__(self, array):
        self.len = len(array)
        self.tree = self.build_tree(array)

    def build_tree(self, array):
        if len(array) == 1:
            return Node(array[0])

        mid = math.floor(len(array) / 2)

        parent = Node(None)
        parent.left_child = self.build_tree(array[0:mid])
        parent.right_child = self.build_tree(array[mid:])
        parent.value = parent.right_child.value + parent.left_child.value

        return parent

    def add(self, i, value):
        tree_i = self.len
        mid = math.floor(self.len / 2)
        node = self.tree
        while not (node == None):
            node.value += value
            if i < (tree_i - mid):
                tree_i -= mid
                node = node.left_child
            elif i >= (tree_i - mid):
                node = node.right_child
            mid = math.floor(mid / 2)

    def partial_sum(self, i):
        tree_i = self.len
        mid = math.floor(self.len / 2)
        value = 0
        node = self.tree
        while True:
            if i == tree_i:
                return value + node.value
            elif i <= (tree_i - mid):
                tree_i -= mid
                node = node.left_child
            elif i > (tree_i - mid):
                value += node.left_child.value
                node = node.right_child
            mid = math.floor(mid / 2)

tree = PartialSumTree([1, 3, 2, 5])
print(tree.partial_sum(1))
print(tree.partial_sum(2))
print(tree.partial_sum(3))
print(tree.partial_sum(4))
