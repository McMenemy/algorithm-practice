import random

class IntegerStore:
    def __init__(self, n):
        self.inserts = 0
        # make a pretend unintilized array since this is impossible in python
        self.to = [random.randint(0, 9) for i in range(10)]
        self.fromm = []

    def insert(self, num):
        self.to[num] = self.inserts
        self.fromm.append(num)
        self.inserts += 1

    def find(self, num):
        return self.to[num] < self.inserts and self.fromm[self.to[num]] == num

    def delete(self, num):
        self.inserts -=1
        self.to[num] += 1

int_store = IntegerStore(10)
print(int_store.to)
print(int_store.find(5))
int_store.insert(5)
print(int_store.find(5))
int_store.delete(5)
print(int_store.find(5))
