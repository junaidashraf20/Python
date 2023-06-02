n=int(input("Enter the number:"))
a=0
b=0
for i in range(1,n+1):
    if(i%2!=0):
        if(i>1):
            a=a+2
    else:
        b=a/2
            
if(n%2!=0):
    print(a)
else:
    print(b)
