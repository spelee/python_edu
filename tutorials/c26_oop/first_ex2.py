import tutorials.c26_oop.first_ex

class SecondClass(tutorials.c26_oop.first_ex.FirstClass):
    def display(self):
        print('hi there: %s' % self.data)


if __name__ == '__main__':
    x = SecondClass()
    x.setdata('val goes here')
    x.display()
