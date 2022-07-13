'''
# union and interscetion concepts
a={1,2,3,4,5,'a'}
b={'a','b','c',3,4}
#union and update both are similar
c=a.union(b)
print(c)
a.update(b)
print(a)
#interscetion and update both are similar
c=a.intersection(b)
print(c)
a.intersection_update(b)
print(a)

#sysmetric difference - remove the comman things
a={1,2,3,4,5,6}
b={5,6,7,8,9,10}
c=a.symmetric_difference(b)
print(c)
a.symmetric_difference_update(b)
print(a)

#set relationship
a={1,2,3,4,5}
b={5,6,7,8,9}
c=a.isdisjoint(b)
print(c)
c=a.issubset(b)
print(c)
c=a.issuperset(b)
print(c)
'''