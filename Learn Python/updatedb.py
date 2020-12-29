import shelve

db  = shelve.open('persondb')

for i in db:
    print(i,db[i])
