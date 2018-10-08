"""
Homegrown timing tools for function calls
Does total time, best-of time, and best-of-totals time
"""


import time, sys
timer = time.clock if sys.platform[:3] == 'win' else time.time

def total(reps, func, *pargs, **kargs):
    """
    Total time to run func() reps times
    :param reps:
    :param func:
    :param pargs:
    :param kargs:
    :return: (total time, last result)
    """
    #print(reps, func.__name__, "pargs={}".format(pargs), "kargs={}".format(kargs))
    repslist = list(range(reps)) # Hoist out, equalize 2.x, 3.x
    start = timer() # or perf_counter/other in 3.3+

    for i in repslist:
        ret = func(*pargs, **kargs)

    elapsed = timer() - start
    return (elapsed, ret)


def bestof(reps, func, *pargs, **kargs):
    """
    Find the quickest func() among reps runs
    :param reps:
    :param func:
    :param pargs:
    :param kargs:
    :return: (best time, last result)
    """

    best = 2 ** 32  # 136 years
    for i in range(reps): # no need to hoist, range usage not timed here
        #print(i)
        start = timer()
        ret = func(*pargs, **kargs)
        elapsed = timer() - start # or call total() with reps=1

        if elapsed < best: best = elapsed

    return (best, ret)

def bestoftotal(reps1, func_reps, func, *pargs, **kargs):
    """
    Best of totals:
    (best of reps1 runs of (total of func_reps runs of func)
    :param reps1:
    :param func_reps:
    :param func:
    :param pargs:
    :param kargs:
    :return:
    """

    return bestof(reps1, total, func_reps, func, *pargs, **kargs)

def test_func(a, b, c, d):
    #print("->a={}, b={}, c={}, d={}".format(a,b,c,d))
    pow(2, 50)
    return("hello")


print(bestoftotal(50, 1000, test_func, 'a', 'b', c='c', d='d'))
