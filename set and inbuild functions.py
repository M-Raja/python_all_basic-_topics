'''
 # set
 colletion of unorder and unindex data type   symbol-{}

name={ 'ram','sam','ram'}
print(name)
print(type(name))

 #access values using for loop
names={'raja','ttt','agaa','power'}
for name in names:
     print(name)
#add a new element
names.add("sara")
print("\n",names)
#update
a={1,2,'soom'}
names.update(a)
print("\n",names)
#remove
names.remove('sara')
print("\n",names)
#pop
names.pop()
print("\n",names)
#discard like if condition ex: if sara in the set then remove it
names.discard("soom")
print("\n",names)
# clear all data in sets
names.clear()
print("\nno",names)

 # no duplicates
a={'ram',"ram","ram",'sam','pam'}
print(a)
'''