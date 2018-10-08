from collections import defaultdict
items = "abcafseajsvzafwseafjl"

d = defaultdict(int, z=100)
for i in items:
    d[i] += 1

print(d)



