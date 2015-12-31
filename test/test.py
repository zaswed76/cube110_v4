


class Iter:
    def __init__(self, x, y):
        self.y = y
        self.x = x
        self.data = list(zip(self.x, self.y))

    def __iter__(self):
        self.id = 0
        return self

    def __next__(self):
        if self.id == len(self.x):
            raise StopIteration
        else:
            res = self.data[self.id]
            self.id += 1
            return res


a = [1, 2, 3]
b = [7, 8, 9]
i = Iter(a, b)
for x in i:
    print(x)

