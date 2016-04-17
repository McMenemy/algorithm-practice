# make a pairing table with the answer for every i, j combination

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
