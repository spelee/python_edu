"""
Experimenting to determine when __getattr__ is called, and whether it is called or not
(and it isn't) by built-in operations.
"""
class Person2:

    def __init__(self):
        self.first = "Default-first-name"
        self.last = "Default-last-name"

    def printName(self):
        print(self.first, self.last)

    def __str__(self):
        return "oopsy"

    def __add__(self, value):
        return 100 + value



class Manager2:

    def __init__(self):
        self.delegate = Person2()

    def __getattr__(self, att):
        print("-> In Manager2, retrieving {} from delegate".format(att))
        return getattr(self.delegate, att)



if __name__ == "__main__":
    m2 = Manager2()
    print("--- Start ---")

    if 0:
        # print name method is not found
        # so __getattr__ dispatches to delegate
        m2.printName()

    if 0:
        # last name attribute is not found
        # so __getattr__ dispatches to delegate
        print(m2.last)

    if 0:
        # what about overloaded operators like __str__?
        # Nope.  We confirm that it is defined in the delegate
        # But that it is not dispatched.
        print("Delegate: ", m2.delegate)
        # Why is it not dispatched?  Because it is inherited from
        # the parent class 'object'
        print("Manager: ", m2)

    if 0:
        # What about if we directly call the overloaded operator?
        # Hard to tell because its possible that the __str__ goes to
        # the object superclass's default implementation
        print("Delegate: ", m2.delegate.__str__())
        print("Manager: ", m2.__str__())

    if 0:
        # What about if we try an overloaded operator that does not have a
        # default implementation
        print("Delegate: ", m2.delegate + 50)
        # Nope... the line below returns with an error
        # Because there is no default inherited from the parent class 'object'
        # And it is not built-in operations don't dispatch through __getattr__
        #print("Manager: ", m2 + 50)

    if 1:
        # What about if we directly called the non-default overloaded operator...
        print("Delegate: ", m2.delegate.__add__(75))
        print("Manager: ", m2.__add__(66))  # it works!!!



    print("--- End ---")



