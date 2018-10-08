class General(Exception): pass
class Specific1(General): pass
class Specific2(General): pass


def raiser0():
    X = General()
    raise X

def raiser1():
    raise Specific1()

def raiser2():
    raise Specific2

for func in (raiser0, raiser1, raiser2):
    try:
        func()
    except General:
        import sys
        print('caught: %s' % sys.exc_info()[0])

