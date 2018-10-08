class MyExcepI(Exception): pass
class MyExcepII(Exception): pass
class MyExcepIII(Exception): pass
class MyExcepIV(Exception): pass

exception_tuple = (MyExcepI, MyExcepII, MyExcepIII, MyExcepIV)

try:
    raise MyExcepI("exc 1")
except exception_tuple as e:
    print("caught:{}".format(e))
