# part a
def find_second_largest(array):
	largest = float("-inf")
	second_largest = float("-inf")

	for num in array:
		if num >= largest:
			second_largest = largest
			largest = num
		elif num > second_largest:
			second_largest = num

	return second_largest

print(find_second_largest([3, 4, 1, 8, 9]))

# part b
# build a heap in linear time pg 115 book and then take the min element twice (lg(n)) time
