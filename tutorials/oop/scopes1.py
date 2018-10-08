X = 1
def nester():

  print(X)	# Global: 1

  class C:
    print(X)	# Global: 1  (class has access to enclosing scopes)

    def method1(self):
      print(X)	# Global: 1 (method has access to enclosing global scope)

    def method2(self):
      X = 3	# Hides global
      print(X)	# Local: 3

  I = C()
  I.method1()
  I.method2()

print(X)	# Global: 1
nester()	# 1, 1, 1, 2
print('-'*40)