import edu_util as e

e.note("Lists are mutable")

e.subnt("But slicing doesn't affect the original list.  Slicing creates a new list.")
L = ['abc', 123, 'zzz', 'xyz', 777]
L2 = L[2:5]
print(L)
print(L2)

e.note("Quick list of some primary methods:")
print("List L:")
print(L)

e.code("L.append('NI')")
L.append('NI')
print(L)

e.code("E = L.pop(2)")
E = L.pop(2)
print("E:", E)
print("L:", L)

e.code("del L[2]")
print(L)

e.note("Other topics include bounds checking (can't index outside a list) and nesting")

e.note("Comprehensions")

M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

e.code("M")
print(M)

e.code("col2 = [row[1] for row in M]")
col2 = [row[1] for row in M]
print(col2)

e.note("Generators")
G = (sum(row) for row in M)
e.code("G = (sum(row) for row in M)")

e.code("type(G)")
print(type(G))

e.code("next(G)")
print(next(G))
e.code("next(G)")
print(next(G))
e.code("next(G)")
print(next(G))
e.code("next(G)")
print(next(G))
