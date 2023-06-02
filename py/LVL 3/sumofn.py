#to find sum of n numbers.
n=int(input("Enter the value for n->>"))
inp=int(input("1.To add numbers\n2.Add n natural numbers\n3.To add even numbers\n4.Add odd numbers\nEnter the choice->>"))
sum1=0
sum2=0
sum3=0
sum4=0
if inp==1: ##code for add given inputs
   for i in range(0,n):
    a = int(input("Numbers->"))
    sum1 += a
   print("Sum of n mnumbesr->",sum1)    
  
elif(inp==2):   ##code to add n natural numbers
   
   for j in range(0,n+1):
     sum2=sum2+j
   print("Sum of n numbers",sum2)


elif(inp==3):  ##code to add even postive numbers
   for i in range(1,n+1):
      if (i%2==0):
        sum3 +=i
 print("Sum of even numbers->",sum3) 

elif (inp==4):   ##code too add odd postive numbrs
   for i in range(1,n+1):
      if(i%2 !=0):
        sum4 +=i
 print("sum of odd numbers",sum4)

              
      
       
              
