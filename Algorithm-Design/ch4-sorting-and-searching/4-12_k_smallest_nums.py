class MinHeap:
    def __init__(self, array):
        self.heap = []
        self.construct_heap(array)

    def construct_heap(self, array):
        for num in array:
            self.insert(num)

    def insert(self, num):
        self.heap.append(num)
        self.bubble_up(num, len(self.heap)-1)

    def bubble_up(self, child, child_idx):
        if child_idx == 0: # already at root no need to check parents
            return

        if child_idx % 2 == 0:
            parent_idx = int((child_idx - 2) / 2)
        else:
            parent_idx = int((child_idx - 1) / 2)
        parent = self.heap[parent_idx]

        if child < parent:
            self.heap[parent_idx] = child
            self.heap[child_idx] = parent
            self.bubble_up(child, parent_idx)
        # else: nothing we are done the child is dominated by parent

    def take_min(self):
        min = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.bubble_down(self.heap[0], 0)
        return min

    def bubble_down(self, parent, parent_idx):
        child1_idx = parent_idx * 2 + 1
        child2_idx = parent_idx * 2 + 2

        if child1_idx >= len(self.heap) or child2_idx >= len(self.heap): # no need to continue if no parents
            return

        child1 = self.heap[child1_idx]
        child2 = self.heap[child2_idx]

        if child1 <= child2:
            child = child1
            child_idx = child1_idx
        else:
            child = child2
            child_idx = child2_idx

        if parent > child:
            self.heap[child_idx] = parent
            self.heap[parent_idx] = child
            self.bubble_down(parent, child_idx)

def k_smallest(k, array):
    min_heap = MinHeap(array)
    mins = []

    for i in range(k):
        mins.append(min_heap.take_min())

    return mins

array = [6, 4, 9, 2, 1, 11, 4, 7, 12]
print(k_smallest(5, array))
