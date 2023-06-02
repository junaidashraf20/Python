x=10
y=20
z=30
if x < y:
    print(x)
    if x<y:  #in if one if gets correct it stops there and skips eventhough other if statemnts are correcd to not
        print("Nested block 1")
    elif z>x:       #trueee
        print("Nested block 2")    
else:
    print(y)    