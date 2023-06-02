# & | ~ ^ << >>
#bin() to convert  ->int to bin
x=100
print(bin(x))
A=3
B= 2
print("Outpt of bit and op::",A & B)   #it does not adds or print T or F
print(id(A),"\n",id(B)) #it actually checks bits 0 and ones
print(A>>2) #shifts left

print(B<<2)  #shifts right


v1=3
v2=7
print("Bins of v1 and v2->>",bin(v1),bin(v2)) 
print(v1^v2)   #Use the XOR operator ^ to perform the "exclusive or" operation. 
#Use the XOR operator ^ between two values to perform bitwise "exclusive or" on their binary representations. 
# When used between two integers, the XOR operator returns an integer. ... XOR between two booleans returns a boolean.
print(bin(4))