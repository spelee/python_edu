import time

def timer(func, *args):
    start = time.clock()
    for i in range(1000):
        func(*args)

    return time.clock() - start # total elapsed time in seconds

print(timer(pow, 2, 1000))

