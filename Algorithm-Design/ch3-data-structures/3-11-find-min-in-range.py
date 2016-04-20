#t  make a pairing table with the answer for every i, j combination

import math

# part A
class MinInRangeDict:
    def __init__(self, array):
        self.array = array
        self.look_up_table = self.create_lookup_table(array)

    def create_lookup_table(self, array):
        table = []
        for i, num1 in enumerate(array):
            table.append([])
            current_min = num1
            for num2 in array[i:]:
                if num2 < num1:
                    current_min = num2

                table[i].append(current_min)
        return table

    def min_in_range(self, i, j):
        j -= i # sine redudancy was avoided in table creation
        return self.look_up_table[i][j]

# dictA = MinInRangeDict([1, 6, 9, 3, 9, 4, 2])
# print(dictA.look_up_table)
# print(dictA.min_in_range(0, 0))
# print(dictA.min_in_range(0, 4))
# print(dictA.min_in_range(2, 4))

# part b
# a binary tree where the first node contains the lowest value in the whole array. The left child then contains the lowest value in the left half of the array and the right child contains the lowest value in the right half of the array. This continues recusively and the leafs then represent the lowest value at a particuluar location. This tree will have n + n/2 + n/4 + ... + 1 nodes. aka O(nlog(n))

class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def set_left_child(self, node):
        self.left_child = node

    def set_right_child(self, node):
        self.right_child = node

class BetterMinRangeDict:
    def __init__(self, array):
        self.array = array
        self.root = self.create_lookup_tree(array)

    def create_lookup_tree(self, array):
        if len(array) == 1:
            return Node(array[0])
        elif len(array) == 0:
            return None

        parent_node = Node(min(array))
        mid = math.ceil(len(array) / 2)
        parent_node.left_child = self.create_lookup_tree(array[0: mid])
        parent_node.right_child = self.create_lookup_tree(array[mid:])
        return parent_node

    def get_min_in_range(self, i, j):
        i_bound = 0
        j_bound = len(self.array)
        mid_length = math.ceil(len(self.array) / 2)
        current_node = self.root
        while True:
            if self.is_between(i, j, i_bound, j_bound):
                return current_node.value
            elif i >= i_bound + mid_length:
                current_node = current_node.right_child
                i_bound += mid_length
            elif j <= j_bound - mid_length:
                current_node = current_node.left_child
                j_bound -= mid_length
            elif current_node.left_child.value < current_node.right_child.value:
                current_node = current_node.left_child
                j_bound -= mid_length
            elif current_node.left_child.value > current_node.right_child.value:
                current_node = current_node.right_node
                i_bound += mid_length
            mid_length = math.ceil(mid_length / 2)

    def is_between(self, i, j, i_bound, j_bound):
        return i_bound >= i and j_bound <= j



dictB = BetterMinRangeDict([1, 6, 9, 3, 9, 4, 2])
# print(dictB.is_between(0, 1, 0, 3))
# print(dictB.root)
# print(dictB.root.left_child.value)
# print(dictB.root.right_child.value)
print(dictB.get_min_in_range(0, 1))
print(dictB.get_min_in_range(0, 4))
print(dictB.get_min_in_range(2, 4))
print(dictB.get_min_in_range(2, 2))
