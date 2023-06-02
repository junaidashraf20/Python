n1=int(input())
n2=int(input())
n3=int(input())
n4=int(input())
n5=int(input())
if ((n1>n2) and (n1>n3) and (n1>n4) and (n1>n5)):
    print("largeast",n1)
elif((n2>n1) and (n2>n3) and (n2>n4) and (n2>n5)):
    print("largest ",n2)
elif((n3>n1) and (n3>n2)and (n3>n4) and (n2>n5)):
    print("laargest",n3)
elif((n4>n1) and (n4>n2)and (n4>n3) and (n4>n5)):
    print("laargest",n4)
else:
    print("laergest is ",n5)
