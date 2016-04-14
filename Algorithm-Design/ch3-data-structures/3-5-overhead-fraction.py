import math

n = 10000000000000000000
data_space_a = float(4 * n)
extra_space_a = float(12 * n)
total_space_a = data_space_a + extra_space_a

print 'overhead fraction a: {}'.format(str(data_space_a / total_space_a))

depth = math.log(n + 1, 2)
leafs = 2**(depth - 1)

data_space_b = float(leafs * 4)
extra_space_b = 4 * n
total_space_b = data_space_b + extra_space_b

print 'overhead fraction b: {}'.format(str(data_space_b / total_space_b))
print 'symbolic: (2^(log2(n) - 1) * 4)((4 * n) + (2^(log2(n) - 1) * 4)'
