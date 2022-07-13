'''
tupel
immutable
surrounded by round brackets (1,1,3)

a=(1,2.3,True,'ram')
print(type(a))
print(a)
 #call by index value
print(a[3]) 
print(a[2])
 #call by index value with starting and ending
print(a[0:3])
 #change tuple to list because we cantadd value in tuple so first change into list then add value
b=list(a)
print(type(b))
b.append("raja")
print(b)

#list to tuple
a=tuple(b)
print(a)

#tuple with for loop
a=(1,2.3,True,'ram')
for i in a:
    if "ram" in a:
        print("ram is founded")
    else:
            print("not found")

#length
a=(1) #int
print(type(a))
b=(1,) #tuple  use , to tell that is tuple 
print(type(b))

print(len(b)) # length

#delete
a=(1,3,44,56,765,8.5)
print(a)
print(type(a))
del a
b=a
print(b)

#count
a=(1,3,4,5,2,6)
b=(1,3,4,5,2,6)
c=a+b
print(c)
print(c.count(6))

# nested tuple
c=((1,3,5,5,7,8,9),(23,45,65,3,4,6))
print(c[0][3])  #var [parentindex][childindex]

#max , min ,*

# *
x=('raja',)*10
print(x)

#max & min 
a=(1,3,4,6,4,5)
print(max(a))
print(min(a))
'''