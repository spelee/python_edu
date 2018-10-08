import tutorials.oop.person as person

import shelve


if __name__ == '__main__':
    bob = person.Person('Bob Smith')
    sue = person.Person('Sue Jones', job='dev', pay=100000)
    tom = person.Manager('Tom Jones', 50000)

    print(tom)


    db = shelve.open('persondb')

    for obj in (bob, sue, tom):
        db[obj.name] = obj
    db.close()


