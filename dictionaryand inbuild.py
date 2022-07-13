'''
#dictionary
user={
 #key:value
"name":"raja",
"age": 25,
"is married":True

}
print(type(user))
print(user)

#inbuild functions
print(user["name"]) # - get output by using key
print(user.get("age")) # -get value by get method
print(user.keys()) # -get only key word as output
print(user.values()) # -get only  value as output
print(user.items()) # -get both key and value as output
print("\n\n\t\t\n\n")

#changing values 
 #add or append new values
user.update({'gender':"male"})
print(user)
# overwrite the value
user["age"]= 35
print(user)
# use pop method to remove firstvalue
user.pop('age')
print(user)
#delete all data in the set
user.clear()
print(user)
'''
#nested ditionary
users={
"user1":{
"name":"raja",
"age": 25,
"is married":True
},
"user2":{
"name":"raghul",
"age": 25,
"is married":True
    }
  }
print(users)