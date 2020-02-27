def myzip(*args):
    iters = list(map(iter, args))
    #iters = map(iter, args)
    count = 0
    while iters:
        print('in while', count)
        res = [next(i) for i in iters]
        print('through iters', count, '\n')
        count += 1
        yield tuple(res)


print(list(myzip('abc', 'lmnop')))

