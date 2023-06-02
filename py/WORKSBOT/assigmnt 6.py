#abstract method
#An abstract method is a method that has a declaration but does not have an implementation
from abc import ABC,abstractmethod
class one(ABC):
    @abstractmethod
    def fun(self):
        pass

class two(one):
    def fun(self):
        print("inside class two")

class three(one):
    def fun(self):
        print("inside class three")

x=two()
x.fun()

y=three()
y.fun()
print("________________________________________________________________")

#multilevel interihance.
class one:
    def mul(self,a,b):
        print("multiplication of ",a ,"and" ,b,":",a*b)
class two(one):
    def div(self,a,b):
        print(f"division of {a} and {b}:",a/b)

class three(two):
    def add(self,a,b):
        print("addition of {a} and {b}:",a+b)
var1=three()
var1.add(20,30)    
var2=one()
var2.mul(11,88)    

#method overloading
print("________________________________________________________________")
class A:
    def display(self):
        print("HI THIS IS CLASS A")
class B(A):
    def display(self):
        print("HEY THIS IS CLASS B")
        
var1=B()
var1.display()        
print("--------------------------------------------------------")
#data inside and outside fuction
def fun1():
    global var
    print("variable using global inside function:",var)
    var = 12#local variable
    print("variable inside function without global:",var)
    
var=5#global variable
print("variable outside function:",var)
fun1()
print("global variable after it was changed in function:",var)


print("________________________________________________________")
#Hybrid inheritance
class shape:
    def __init__(self,a,b):
        self.side1=a
        self.side2=b
    def draw(self):
        for i in range(self.side2):
            print("* "*self.side1)
    def perimeter(self):
        p=(self.side1+self.side2)*2
        if self.side1==self.side2:
            print(self.side1,self.side2)
            print("perimeter of square:",p)
        else:
            print("perimeter of rectangle:",p)

class rectangle(shape):
    def __init__(self,a,b):
        super().__init__(a,b)
    def area(self):
        area=self.side1*self.side2
        if self.side1==self.side2:
            print("area of square:",area)
        else:
            print("area of rectangle:",area)

class square(shape):
    def __init__(self,a,b=None):
        super().__init__(a,b)
    def volume(self,height):
        volume=self.side1*self.side1*height
        if self.side1==self.side2:
            print("volume of cube:",volume)
        else:
            print("volume of rectangle:",volume)

class all(rectangle,square):
    def __init__(self,a,b):
        self.side1=a
        self.side2=b
var4=all(10,20)
var4.volume(110)        
var4.area()
var4.draw()
print("_______________________________________________________")
#polymorphism using built in fuction
a="worksbot"
b=[1,2,3,4,5]
c="works"
d="bot"
e=10
f=20
#polymorphism of len function
print(len(a))
print(len(b))
#polymorphism of + operator
print(c+d)
print(e+f)