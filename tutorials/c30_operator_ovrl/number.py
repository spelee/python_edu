# File number.py

class Number:
    def __init__(self, start):
        self.data = start

    def __sub__(self, other):
        return Number(self.data - other)

    def __repr__(self):
        return str(self.data)


class MyCustomList:
    def __init__(self):
        self.data = list('abcde')

    def __getitem__(self, idx):
        print('getting val @', idx)
        return self.data[idx]


a = MyCustomList()
for v in a:
    print(v)
