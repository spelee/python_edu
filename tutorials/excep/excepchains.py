import sys

class MyExceptI(Exception): pass
class MyExceptII(Exception): pass

def func1():
    try:
        print(". func1:\tenter try")
        #raise Exception(". func1: exception raised.")
        func2()
        print(". func1:\texit try")
    except Exception as e:
        print(". func1:except caught:\t{}".format(e))
        print(". func1:context:\t{}".format(e.__context__))
        print(". func1:cause:\t{}".format(e.__cause__))
        print(". func1:exception chain:")
        printExceptionChain(e, 1)
    print(". func1:\toutside")

def func2():
    try:
        print(".. func2:\tenter try")
        raise MyExceptI(".. func2: exception raised.") from MyExceptII(".. func2: from except")
        print(".. func2:\texit try")
    except MyExceptI as e:
        print(".. func2:except caught:\t{}".format(e))
        # this should set the context to the original exception
        raise MyExceptII(".. func2 except handler: exception raised") \
            from MyExceptI(".. func2 except handler: from except")
    print(".. func2:\toutside")

def printExceptionChain(e, prefix_num):
    prefix = "-"
    if e.__context__:
        print("{}:context:{}->{}".format(prefix*prefix_num,e,e.__context__))
        printExceptionChain(e.__context__, prefix_num+1)
    if e.__cause__:
        print("{}:cause:{}->{}".format(prefix*prefix_num,e,e.__cause__))
        printExceptionChain(e.__cause__, prefix_num+1)

func1()
