'''
a= """llsjdjdmjdmdjshndhxsnhsjwhwswjwjajahsbdhssshsshsbsshshshsjsxbx
xhxhkhsxgqmnLblbibsbiSQGKBUGQWNBIXHTYIHTATAGJXJIXJGIUFAGJFXGIJOIGIQXFIU
GXJFQGOQJOGQJOFGJFIGOJFJGFJWQFPFPISJFIFPIAJFSIPAJFPGagiafpiryftr
"""
print(a)
print(type(a))
'''
# multiline string input 

#example
# para = [] # list like arrays
# print(type(para))

#call with index value
#para=[25,98,0]
#print(para[2])

'''
para=["25","87","98"]  #must use double string because int cannot join
print("  ".join(para)) 
print(" ,".join(para)) 
print(" | ".join(para)) 
print(" # ".join(para)) 
'''
para=[]
print("enter a para :")

while true: #while true is endless loop
    line = input()
    if line : 
    para.append(line) #append is join
    else :
        break
    print(para)
    output = '\n'.join(para)
    print (output)