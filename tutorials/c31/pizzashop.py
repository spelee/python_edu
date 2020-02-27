from tutorials.c31.employees import PizzaRobot, Server


class Customer:
    def __init__(self, name):
        self.name = name

    def order(self, server):
        print(self.name, 'orders from', server)

    def pay(self, server):
        print(self.name, 'pays for item to', server)


class Oven:
    def bake(self):
        print('oven bakes')


class PizzaShop:
    def __init__(self):
        self.server = Server('Pat')
        self.chef = PizzaRobot('Bob')
        self.oven = Oven()

    def order(self, name):
        customer = Customer(name)
        customer.order(self.server)
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)

if __name__ == '__main__':
    shop = PizzaShop()
    print(shop.server, shop.chef)

    import pickle
    f = open('datafile.pkl', 'wb')
    shop.chef.name = 'Steve'
    pickle.dump(shop, f)
    f.close()

    f = open('datafile.pkl', 'rb')
    new_obj = pickle.load(f)
    print(type(new_obj))
    print(new_obj.server, new_obj.chef)


