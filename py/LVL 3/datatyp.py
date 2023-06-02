aj=[1,"hi","hello",22]    ##lists #muttable #indexable
aj[0]=100
print(aj)


tup=(1,2,"add","Adadcc",2,1)
##tup(0)=2000
print(tup)   ##error becuse tuple immutable
s1=tuple("python")
print(s1)
##print(tup(2))  #not indexable

st={1,2,44,66,2,1,2}   ##set #immutable #not indexable
print(st)
s2=set("programming")
print(s2)

dic ={1:"one",2:"two",3:"three"} ##dictionary   #unmutable #not indexable
dic2={"students":("junaid","krishna"),"teachers":("harsh","ramu")}

print(dic.get(2))
print(dic2)
print(dic2.get("students"))