
import edu_util as e

M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

e.note("M is a 3x3 array:")
print(M)

e.subnt("Summing each row using a comprehension")
e.code("ans = [sum(row) for row in M])")
ans = [sum(row) for row in M]
print("type(ans): ", type(ans))
print("ans: ", ans)


e.subnt("Summing each row using map")
e.code("ans = list(map(sum, M))")
ans = list(map(sum, M))
print("type(map(sum, M):", type(map(sum, M)))
print("ans: ", ans)


