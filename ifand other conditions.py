   #if-else-elif

# 1.write a program to check the given number is even 
'''
n=int(input("enter the Number :"))

if n%2==0:
    print(n,"is even")
else:
        print(n,"is even")
    '''
# 2. write a program to check vote eligibility by enter his/her name and age
'''
Name=input("Enter the name :")
age=int(input("Enter the age :"))
if age >= 18:
    print(Name,"Age is",age,"eligible")
else:
     print(Name,"Age is",age," not eligible")
     '''

     #elif
'''
     1-5    0.5
     5-10    1
     10-30   5
     >30 membership cancel
     
days=int(input("enter days:"))
if days==0:
    print("Good no fine")
elif days>=1 and days<=5:
     print("fine amount",days*0.5)
elif days>=5 and days<=10:
    print("fine amount",days*1)  
elif days>=10 and days<=30:
    print("fine amount",days*5)
else:
    print("your member ship has been canceled")


     '''
     #nested if statement   

'''
  1. students marks
  total
  average
  result

  if pass grade 
  90-100 A
  80-89 B
  70-79 C
  else D


     '''
m1=int(input("enter the mark1 :"))
m2=int(input("enter the mark2 :"))
m3=int(input("enter the mark3 :"))
total = m1+m2+m3
print("total :",total)
average=int(total/3.0)
print("average :",average)

if m1>=35 and m2>=35 and m3>=35:
    print("Result : pass")
if average>=90 and average<=100:
    print("Grade : A")
elif average>=80 and average<=89:
    print("Grade : B")
elif average>=70 and average<=79:
    print("Grade : C")
else:
    print("Result : Fail")

