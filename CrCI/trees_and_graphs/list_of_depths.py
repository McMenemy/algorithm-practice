from BinaryTree import BinaryTree

b_tree = BinaryTree([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
layers = b_tree.get_layers()
for i, layer in enumerate(layers):
	print('layer ', i)
	layer.display()
