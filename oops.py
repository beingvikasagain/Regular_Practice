# class A:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#         print("This is Class A")
        
#     def findarea(self):
#         print("This is class Base findArea()")
#         area = (self.x*self.y)/2
#         print(area)
        
# class B(A):
#     def __init__(self,l,b):
#         self.l = l
#         self.b = b
#         print("This is b class cons")
        
#     def findarea(self):
#         print("This is child class FindArea()")
#         area = (self.l*self.b)/2
#         print(area)
        
# obj=B(10,20)
# obj.findarea()
        

class Employee:
    def __init__(self,name,age,salary):
        self.d = {}
        self.d['name']=name
        self.d['age']=age
        self.d['salary']=salary
        
    def fetchEmployee(self):
        print(self.d)
    
    def updateEmployee(self,name,age,salary):
        if self.d['name']==name:
            self.d['age']=age
            self.d['salary']=salary
            
name = input("Enter employee name: ")
age = int(input("Enter employee age: "))
salary = int(input("enter employee salary"))

rakesh = Employee(name,age,salary)
rakesh.fetchEmployee()

print("Enter details for update value")
name = input("Enter employee name: ")
age = int(input("Enter employee age: "))
salary = int(input("Enter employee salary: "))

rakesh.updateEmployee(name,age,salary)
rakesh.fetchEmployee()

