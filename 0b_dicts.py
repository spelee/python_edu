import edu_util as e

e.note("Ways to create a dictionary.")

e.subnt("{key:val}")

e.subnt("dict(key=val)")

e.subnt("dict(zip([key1, key2, key3], [val1, val2, val3]))")
d = dict(zip(['key1', 'key2', 'key3'], ['val1', 'val2', 'val3']))
print(d)
