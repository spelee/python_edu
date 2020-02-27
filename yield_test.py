class C:
    def __init__(self):
        self.dat = [0, 1, 2, 3, 4]

    def __getitem__(self, item):
        return self.dat[item]

a = C()
print(a[2])

x = iter(a)
y = iter(a)

print('x', next(x))
print('y', next(y))
print('x', next(x))
print('x', next(x))
print('x', next(x))
print('y', next(y))

print('-' * 80)

for a in C():
    print(a)
