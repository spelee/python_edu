import edu_util as e


e.note("""\
bytearray is a bytes/list hybrid.  It supports in-place changes for text, but for only characters that are at most 
8-bits (e.g., ASCII)""")
e.subnt("create, extend , and print a byte array")
e.code("B = bytearray(b'spam')")
e.code("B.extend(b'eggs')")
B = bytearray(b'spam')
B.extend(b'eggs')
print(B)


e.subnt("printing a decoded bytearray")
e.code("B.decode()")
print(B.decode())

e.subnt("can assign an element to be a codepoint")
e.code("B[-1] = 'z'  # will fail")

print()
e.code("B[-1] = ord('z')")
B[-1] = ord('z')
print(B)

e.note("Sequence operations apply to strings, tuples, and lists.")

e.note("The built-in dir function lists variables assigned in the callers scope.")
e.subnt("""\
Or returns a list of all attributes available for any object passed to it -- that is the caller's scope within that
object""")

e.note("The built-in help function can be called on types or methods.")
e.subnt("Both dir and help also accept a real object or the name of a data type.")
