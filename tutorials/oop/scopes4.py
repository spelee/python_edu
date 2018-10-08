X = 1

def nester():
    X = 2

    class C:
        X = 3	# Class local hides nester's: C.X or I.X (not scoped)
        #print(X)
        def method1(self):
            print(X)  # access global, not class var
            print(self.X)	# Inherited class local: 3

    I = C()
    I.method1()
    #print(I.X)

nester()
print('-'*40)