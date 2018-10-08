class Super:
    def delegate(self):
        print("delgating...")
        self.action()
        print("delgation complete.")

class Sub(Super):
    def action(self):
        print("{} has been assigned a task".format(self.__class__))


if __name__ == '__main__':
    sb = Sub()
    sb.delegate()

    # printing classname...
    for k in Sub,:
        print("-->{}".format(k.__name__))
        print("-->{}".format(k.__class__))
        print("-->{}".format(k.__bases__))