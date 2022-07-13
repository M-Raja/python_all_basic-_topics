'''
# try except block in python
compiletime error - , ; '' ""
runtime error - 

# 1.try except in python 
 
try:
     a=10/0
except Exception as e:
    print(e)
   
# 2. try except else in python

try:
     a=10/0 #(5 (or) 0)
except Exception as e:
    print(e)
else:
    print("A value is",a)
 '''
 # 3. try except else finally in python

 # finally part is executed compulsory 
try:
     a=10/0 #(5 (or) 0)
except Exception as e:
    print(e)
else:
    print("A value is",a)
finally:
    print("im finally###")





