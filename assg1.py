mylist = range(4)
seclist = mylist
print seclist
mylist.append(4)
print seclist
seclist = mylist[:]
print seclist
mylist.append(5)
print seclist

