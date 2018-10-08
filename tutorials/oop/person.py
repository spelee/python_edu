"""
Record and process information about people.
Run this file directly to test its classes.
"""

from tutorials.oop.classtools import AttrDisplay

class Person(AttrDisplay):
    """
    Create and process person records
    """

    def __init__(self, name, job=None, pay=0):
        """ Test doc"""
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1+percent))

class Manager(Person):
    """
    A customized Person with special requirements
    """

    def __init__(self, name, pay):
        Person.__init__(self, name, job="mgr", pay=pay)

    def giveRaise(self, percent, bonus=.10):
#        self.pay = int(self.pay * (1+percent+bonus))
        Person.giveRaise(self, percent + bonus)

class Departement:

    def __init__(self, *args):
        self.members = list(args)

    def addMember(self, person):
        self.members.append(person)

    def giveRaises(self, percent):
        for p in self.members:
            p.giveRaise(percent)

    def showAll(self):
        for p in self.members:
            print(p)



# recall that the __name__ attribute of a module holds the module's name
# as known to importers.
# It is __main__ if it is the top level script
if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    tom = Manager('Tom Jones', 50000)

    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    tom = Manager('Tom Jones', 50000)
    tom.giveRaise(.10)
    print(tom.lastName())
    print(tom)

"""
    development = Departement(bob, sue)
    development.addMember(tom)
    development.giveRaises(.10)
    development.showAll()
"""




