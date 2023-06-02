##is and not is
x=100
y=100
print(x==y) #Equality op
print(x is y)  #IDentity op
print(id(x))
print(id(y))

a=100000
b=100000
print(a is b)
print(id(a),id(b))
#somtimes varibles are stored in same addres so it is truuu
#but at large scal it become false so identity op better usedwhen needed to compare memory adress


v1=3
v2=5
print(id(v1),id(v2))
