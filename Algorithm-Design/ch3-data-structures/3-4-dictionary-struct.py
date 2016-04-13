class DictStruct():
    def __init__(self, array):
        self.data = self.process_array(array)

    def process_array(self, array):
        data = [0] * (max(array) + 1)
        for num in array:
            data[num] += 1

        return data

    def insert(self, num):
        self.data[num] += 1
        return num

    def delete(self, num):
        if self.data[num] == 0:
            return 'entry not in dictionary'
        else:
            self.data[num] -= 1
            return num

    def search(self, num):
        if self.data[num] > 0:
            return num
        else:
            return 'entry not in dictionary'

    def all(self):
        return self.data

dict = DictStruct([1, 5, 4, 3, 2, 8, 9])

print dict.all()
print dict.search(4)
print dict.insert(6)
print dict.all()
print dict.search(6)
print dict.delete(6)
print dict.all()
print dict.search(6)
