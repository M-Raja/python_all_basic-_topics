'''''
#user define function in python
#def - keyword  /  function() - function()
def welcome():
    print("welcome bro !")
welcome()


# 9 types of functions

# 1. No return type without argument function in python
 
def add():
    a=int(input("enter a value of A:"))
    b=int(input("enter a value of B:"))
    c=a+b
    print("the value of c is "+c)
add()

# 2. No return type with argument function in python

def sub(a,b):
    c=a-b
    print("the value of c is ",c)
sub(8,4)

# 3. return type with out arguments function

def mul():
  a=int(input("enter a value of A:"))
  b=int(input("enter a value of B:"))
  c=a*b 
  return c

x= mul()
print(x)

# 4. return type with arguments function

def sub(a,b):
    c=a-b
    return c
x=sub(3,1)
print("value of x is ",x)

# 5. arbitary arguments function in python (*)

#def(a,b) --> we can only pass two arguments only

#def(*) --> we can pass unlimeted arguments

def class_10(*students):     #---> (*var_name)
    print(students)
class_10("ram","sam","tam","eam","sara")  #--> method (or) function


# 6. keyword argument function in python

def message(name,age):
    print(name,"& age is",age)
 
message(name='raja',age=43)

#7. arbitrary keyword arguments

def biodata(** data):     #---> (** keyword)
    print(data)    

biodata(name="raja",age=19,gender="male")

#8. default  parameter function        

def user(name,city="salem"):
    print(name,"is form",city)

user("raja",)
user("\nraghul",city="chennai")

#9.passing a list as an argument in function in python 

        --------------------------------------------
x
#10. recursive function in python

def factorial(x):
    if x==1:
        return 1
    else:
        return(x*factorial(x-1))

print("factorial :",factorial(5)) #---> recursive function call itself

#11. lambdafunction in python 

c=lambda a:a+5 #---->used to make task & calculate & use variable as a function
print(c(5))

c=lambda a,b:a*b
print(c(1,2))
'''
