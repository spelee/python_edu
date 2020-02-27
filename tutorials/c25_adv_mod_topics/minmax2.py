def minmax(test, *args):
    res = args[0]
    for arg in args[1:]:
        if test(arg, res):
            res = arg
    return res


def lessthan(x, y): return x < y


def greaterthan(x, y): return x > y

print('I am:', __name__)

if __name__ == '__main__':
    args = [4, 2, 1, 5, 6, 3]
    print(minmax(lessthan, *args))
    print(minmax(greaterthan, *args))
