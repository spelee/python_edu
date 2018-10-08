import sys

print("Hello")

try:
    sys.exit(100)

except BaseException as e:
    print('-'*10)
    print(e)
    print('-'*10)
    print(type(sys.exc_info()[2]))
    print(sys.exc_info()[2].__class__.__file__)

finally:
    print("before you go...")
