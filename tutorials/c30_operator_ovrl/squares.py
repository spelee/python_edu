class Squares:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop

    def __getitem__(self, i):
        print('boom')
        if i >= self.stop:
            raise IndexError

        self.value += 1
        return self.value ** 2

'''
    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2
'''


if __name__ == '__main__':
    for i in Squares(1, 5):
        print(i, end=' ')