
class MyErrorI(Exception): pass

def test1():
    import tutorials.importing.sub1.sub2.sub3

    print('-'*10)
    print(len(vars()))
    print(vars())

    print('-'*5)
    print(type(tutorials), ':', tutorials.__name__, ':',
          [n for n in tutorials.__dict__ if not n.startswith('__')])

    print('-'*5)
    print(type(tutorials.importing), ':', tutorials.importing.__name__, ':',
          [n for n in tutorials.importing.__dict__ if not n.startswith('__')])

    print('-'*5)
    print(type(tutorials.importing.sub1), ':', tutorials.importing.sub1.__name__, ':',
          [n for n in tutorials.importing.sub1.__dict__ if not n.startswith('__')])

    print('-'*5)
    print(type(tutorials.importing.sub1.sub2), ':', tutorials.importing.sub1.sub2.__name__, ':',
          [n for n in tutorials.importing.sub1.sub2.__dict__ if not n.startswith('__')])

    print('-'*5)
    print(type(tutorials.importing.sub1.sub2.sub3), ':',
          tutorials.importing.sub1.sub2.sub3.__name__, ':',
          [n for n in tutorials.importing.sub1.sub2.sub3.__dict__ if not n.startswith('__')])

def test2():
    from tutorials.importing.sub1.sub2 import sub3
    print('-'*10)
    print(locals())
    print('-'*5)
    print(type(sub3), ':', sub3.__name__, ':',
          [n for n in sub3.__dict__ if not n.startswith('__')])

def safe(func):
    def wrapped(*pargs, **kargs):
        try:
            print("wrapped: {} {} {}".format(func.__name__, pargs, kargs))
            func(*pargs, **kargs)
            print("wrapped: should not be called")
        except:
            import sys
            print("wrapped:", sys.exc_info()[1])
    return wrapped

@safe
def oops(a,b,c,e):
    print("oops {}, {}, {}, {}".format(a, b, c, e))
    raise MyErrorI("raised from oops")

@safe
def testme():
    print("hi")

oops('a', 'b', c='d', e='f')
print('-'*10)
testme()

#test1()
#test2()

