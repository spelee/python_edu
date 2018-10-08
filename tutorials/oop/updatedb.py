import shelve

db = shelve.open('persondb')

for key in sorted(db):
    print(key, "\t=>", db[key])


sue = db['Sue Jones']
sue.giveRaise(.10)

db['Sue Jones'] = sue  # assign to key to update in shelv

db.close()