
class FirstClass:

    def setdata(self, value):
        self.data = value

    def display(self):
        print(self.data)

    def display2(self):
        print(self.otherdata)

class SecondClass(FirstClass):
    def display(self):
        print('Current value = "%s"' % self.data)


class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data = value

    def __add__(self, other):
        return ThirdClass(self.data + other)

    def __str__(self):
        return '[ThirdClass: %s]' % self.data

    def mul(self, other):
        self.data *= other


if __name__ == '__main__':

    x = FirstClass()
    y = FirstClass()

    x.setdata("King Arthur")
    y.setdata(3.14159)

    x.display()
    y.display()

    x.otherdata = 'new'
    x.display2()

    z = SecondClass()
    z.setdata(42)
    z.display()

    x.data = "New value"
    x.display()

    print('-' * 80)
    a = ThirdClass('abc')
    a.display()
    print(a)

    b = a + 'ayz'
    b.display()
    print(b)

    a.mul(3)
    print(a)


    print('end')