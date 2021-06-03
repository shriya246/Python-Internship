#class
'''class demo:
    def myFunction(self):
      print("This is myFunctionof class... ")
    def show(self,name):
        print("Value is",name)
d1=demo()
d1.myFunction()
d1.show("Shriya")'''

#EXAMPLE
'''class Myclass:
    def func1(self):
        print('Hello')
    def func2(self,name):
        print('Name is : '+name)
#create a object of Myclass
myc = Myclass()
#calling function
myc.func1()
myc.func2("Amazon")'''

#sum of 2 number using class
'''class Myclass:
    def func1(self,n1,n2):
        ans=n1+n2
        print('Ans is : ',ans)
#creat a object of Myclass
myc = Myclass()
#calling function
myc.func1(20,30)'''

#python constructors
'''class demo:
    def myFunction(self):
        print("This is myFunctionof class...")
    def show(self,name):
        print("Value is ",name)
    def __init__(self,nm):
        print("This is demo class...")
        print("Name is ",nm)
d1=demo("xyz")
d1.myFunction()
d1.show("Shriya")'''

#assign string value to class variable using method
'''class Demo:
    name=""
    def func1(self):
        print("This is normal method...")
    def func2(self,name):
        self.name=name
    def show(self):
        print("Name is ",self.name)
d1=Demo()
d1.func1()
d1.func2("Shriya")
d1.show()'''

#example
'''class Myclass:
    name=""
    def func1(self):
        print("Hello Function1")
    def func2(self,name):
        self.name=name
    def func3(self):
        print("Value is ",self.name)
m1=Myclass()
m1.func1()
m1.func2("Shriya")
m1.func3()'''

#assign string value to class variable using constructor
'''class Myclass:
    name= ""
    def __init__(self,name):
        self.name = name
    def func1(self):
        print("Name is : ", self.name)
myc = Myclass("Shriya Patel")'''            

#Example
'''class Myclass:
    n1=0
    n2=0

    #constructor

    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2

    #Function
    def func1(self):
        ans=self.n1+self.n2
        print('Ans is :',ans)

#create a object of MyClass
myc=Myclass(10,20)

#Calling Function
myc.func1()'''

#single level inheritance
'''class Demo:
    def func1(self):
        print("This is parent class method...")
class Demo1(Demo):
    def func2(self):
        print("This is child class method")
d1=Demo1()
d1.func1()
d1.func2()'''

#parent & child
'''class Demo:
    def __init__(self):
        print("This is Demo class...")
    def func1(self):
        print("This is parent class method...")
class Demo1(Demo):
    def __init__(self):
            print("This is Demo1 class...")
    def func2(self):
        print("This is child class method")
d1=Demo1()
d1.func1()
d1.func2()'''

#multi level inheritance
'''class Demo:
    def __init__(self):
        print("This is Demo class...")
    def func1(self):
        print("This is parent class method...")
class Demo1(Demo):
    def __init__(self):
            print("This is Demo1 class...")
    def func2(self):
        print("This is child class method")
class Demo2(Demo1):
    def func3(self):
        print("This is child method of Demo2 class...")        
d1=Demo2()
d1.func1()
d1.func2()
d1.func3()'''

#multiple inheritance
'''class Demo:
    def __init__(self):
        print("This is Demo class...")
    def func1(self):
        print("This is parent class method...")
class Demo1:
    def __init__(self):
            print("This is Demo1 class...")
    def func2(self):
        print("This is child class method")
class Demo2(Demo,Demo1):
    def func3(self):
        print("This is child method of Demo2 class...")        
d1=Demo2()
d1.func1()
d1.func2()
d1.func3()'''

#hierarchical inheritance
'''class Demo:
    def __init__(self):
        print("This is Demo class...")
    def func1(self):
        print("This is parent class method...")
class Demo1(Demo):
    def __init__(self):
            print("This is Demo1 class...")
    def func2(self):
        print("This is child class method")
class Demo2(Demo):
    def func3(self):
        print("This is child method of Demo2 class...")        
d1=Demo1()
d1.func1()
d1.func2()

d2=Demo2()
d2.func1()
d2.func3()'''

#hybrid inheritance
#define parent class1
'''class MyParentClass1():

    def method__Parent1(self):
        print("Parent1 method called")

#define parent class2
class MyParentClass2():

    def method__Parent2(self):
        print("Parent2 method called")

#define Child class
class ChildClass(MyParentClass1, MyParentClass2):  #Multiple Inheritance   
   
    def child_method(self):
        print("child method")        

#define Child class2
class ChildClass(MyParentClass1):  #Hierarchical Inherit
#define Child class2
class ChildClass(MyParentClass1):  #Hierarchical Inheritance   
   def child_method(self):
        print("child method2") 

c=ChildClass()          #object of child
c.method_Parent1()      #parent class1 method
c.method_Parent2()      #parent class2 method
c.child_method()        #child class method

c2=ChildClass2()         #object of child class 2
c2.child_method()        #child class 2 method
c2.method_Parent1() '''     #parent class1 method


#overriding
'''class parentclass:
    def func1(self):
        print("Parent method called")
class Childrenclass(parentclass):
    def func1(self):
        print("Child method called")
c=Childrenclass()
c.func1()'''

#Example2
'''class parentclass:
    def func1(self):
        print("Parent method called")
class Childrenclass(parentclass):
    def func1(self):
        print("Child method called")
c=Childrenclass()
c.func1()
c=parentclass()'''

#last task
'''class Myclass:
    def func1(self,n1,n2):
        ans=n1+n2
        print("Ans is :",ans)
    def func1(self,n1,n2,n3):
        ans=n1+n2+n3
        print("Ans is :",ans)
    
a=Myclass()
#a.func1(14,78)
a.func1(10,20,30)'''
