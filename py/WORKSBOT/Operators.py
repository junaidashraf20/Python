print("ARITHMETIC OPERATORS")
print("--------------------")
a=10
b=5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a//b)
print(a%b)
a="abc"
b="xyz"
c=2
print(a+b)
print(a*c)
#print(a*b) gives eroor as it cannt be done
print("_______________________________________________")
print("RELATIONAL OPERATORS")
print("--------------------")
a=10
b=5
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a==b)
print(a!=b)
a="abc"
b="xyz"
c=5
#print(a>c)error
#print(a<c)error
#print(a>=c)error
#print(a<=c)error
print(a==c)
print(a!=c)
print("_______________________________________________")
print("ASSIGNMENT OPERATORS")
print("--------------------")
a=10
b=5
c=0
c=b
print(c)
a+=b
print(a)
a-=b
print(a)
a*=b
print(a)
a/=b
print(a)
a%=b
print(a)
a=10
b=5
a**=b
print(a)
a//=b
print(a)
a="abc"
b="xyz"
c=2
a+=b
print(a)
#a-=berror
#a*=berror
a*=c
print(a)
#a/=berror
#a%=berror
#a/=cerror
#a%=cerror
print("_______________________________________________")
print("LOGICAL OPERATORS")
print("--------------------")
a=10
b=5
print(a and b)
print(a or b)
print(not a)
#print(a not b)error
a="abc"
b="xyz"
c=2
print(a and b)
print(a or b)
print(not a)
#print(a not b)error
print(a and c)
print(a or c)
print(not a)
print("_______________________________________________")
print("MEMBERSHIP OPERATORS")
print("--------------------")
a=[1,2,3]
b=2
print(b in a)
print(b not in a)
a="abc"
b="a"
print(b in a)
print(b not in a)
print("_______________________________________________")
print("IDENTITY OPERATORS")
print("--------------------")
a=10
b=5
print(a is b)
print(a is not b)
a="abc"
b="xyz"
print(a is b)
print(a is not b)
print("_______________________________________________")
print("BITWISE OPERATORS")
print("--------------------")
a=10
b=5
print(a&b)
print(a|b)
print(a^b)
print(~b)
print(a<<b)
print(a>>b)
a="abc"
b="xyz"
c=2
#print(a&b)error
#print(a|b)error
#print(a^b)error
#print(~b)error
#print(a<<b)error
#print(a>>b)error
#print(a<<c)error
#print(a|c)error
#print(a^c)error
#print(a<<c)error
#print(a>>c)error



