import math

class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

class BinaryTree:
    def __init__(self, array):
        self.root = self.create_tree(array)


    def create_tree(self, array):
        if len(array) == 1:
            return Node(array[0])

        if len(array) == 0:
            return None

        mid = math.floor(len(array) / 2)
        parent_node = Node(array[mid])
        parent_node.left = self.create_tree(array[0:mid])
        parent_node.right = self.create_tree(array[mid+1:])

        return parent_node

def print_tree(root):
    print(root.value)
    if root.left:
        print_tree(root.left)

    if root.right:
        print_tree(root.right)

def are_trees_same(my_root, other_root):
    # base cases
    if (my_root == None and other_root != None) or (my_root != None and other_root == None):
        return False
    elif my_root == other_root: # both are None
        return True
    elif my_root.value != other_root.value:
        return False
    else:
        is_left_same = are_trees_same(my_root.left, other_root.left)
        is_right_same = are_trees_same(my_root.right, other_root.right)

    return is_left_same and is_right_same

tree = BinaryTree([1, 2, 3, 4, 5, 6, 7, 8, 9])
tree2 = BinaryTree([1, 2, 3, 4, 5, 6, 7, 8, 9])
tree3 = BinaryTree([1, 2, 3, 4, 5, 6, 7, 8])
tree4 = BinaryTree([2, 3, 4, 5, 6, 7, 8, 9])
tree5 = BinaryTree([2, 3, 5, 6, 7, 8, 9])

print(are_trees_same(tree.root, tree2.root))
print(are_trees_same(tree.root, tree3.root))
print(are_trees_same(tree.root, tree4.root))
print(are_trees_same(tree.root, tree5.root))
