'''
#list
a=[1,2,3,4,5,True,'ram',2.3]
print(a)
print(type(a))
print((a[0]))
print((a[6]))

#nested list 
a=[1,False,'ram',2.5,[1,2,3,4,5]]
print(a[4][3])



#inbuild functions
#clear
a=[1,2,3,4,5]
a.clear()
print(a)

#copy
a=[1,2,3,4,5]
b=a.copy()
print("A =",a)
print("\nB =",b)

#count
a=[10,25,30,25,25,4,45,98]
print(a.count(25))

#index
a=[1,2,3,4,5,6,78,8,9]
print(a.index(3))

#length
a=[1,2,3,4,5,6,78,8,9]
print(len(a))

#max and min
a=[1,2,3,4,5,6,78,8,9]
print(max(a))
print(min(a))

#pop
a=[1,2,3,4,5,6,78,8,9]
a.pop(1)
print(a)

#remove  - used to remove value in list but only first occurance
a=[1,2,1,1,3,4,5,6,78,8,9]
a.remove(1)
print(a)

#append  add or insert
name=["ram"]
name.append("kumar")
print(name)

#extends - join or append list 
name=["raja","ram","sam"]
name2=["power","ranger","action"]
name.extend(name2)
print(name)

#insert
name=["raja","ram","sam"]
name.insert(0,"mohan")  #-(index,value)
print(name)

#list constructor 
print(list((range(5))))
print(list("raja robert"))

#sort & Reverse sort
a=[1,15,10,100,25,85,65,75,95]
b=["orange","apple","raja"] 
a.sort() #asscending order -1 to 100
a.sort(reverse=True) #dsscending order -100 to 1
b.sort(key=len) #calculate letters
print(a)
print(b)
'''


