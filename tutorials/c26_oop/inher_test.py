class Parent1:
    x = 'p1'
    z = 'zp1'


class Parent2:
    x = 'p2'
    y = 'yp2'

    def print_d(self):
        print(self.__dict__)
        print('---->', self.bz)

    def add_me(self):
        self.me = 'too'


class Child1(Parent1, Parent2):
    x = 'c1'

    def do_dad(self):
        print('hi')



if __name__ == '__main__':
    c1 = Child1()
    c2 = Child1()

    print(c1.x)
    print(c1.y)
    print(c1.z)
    print('-')


    #c2.print_d()
    c2.bz = 'bobo'
    c2.print_d()
    c2.add_me()
    c2.print_d()

    print('-')

    print(c1.x)
    print(c1.y)
    print(c1.z)

    Parent1.z = 'changed zp1'
    print('-')

    print(c1.x)
    print(c1.y)
    print(c1.z)

    print(c2.bz)
