# # python does not support method overloading by default
# # but we have dispatch fun by which we can
# # implement method overloading
# # @dispatch(int,int) and @dispatch(float, float)

# from multipledispatch import dispatch
# class abc:
#     @dispatch(int,int)
#     def logic1(self,i,j):
#         print("A")
#         self.i=i
#         self.j=j
#         result = (self.i*self.j)/2
#         print(result)
        
#     @dispatch(float,float)
#     def logic1(self,i,j):
#         print("B")
#         self.i=i
#         self.j=j
#         result = (self.i*self.j)/5
#         print("{:.2f}".format(result))
        
# obj = abc()
# obj.logic1(10,10)
# obj.logic1(10.2, 20.36)

# from multipledispatch import dispatch
# class A:
#     @dispatch(int,int)
#     def abc(self,i,j):
#         print("A")
#         self.i=i
#         self.j=j
#         return self.i+self.j
#     @dispatch(float,float)
#     def abc(self,x,y):
#         print("B")
#         self.x=x
#         self.y=y
#         return self.x+self.y
    
# obj = A()
# result1 = obj.abc(16,20)
# print(result1)
# result2 = obj.abc(10.0,23.3)
# print(result2)

# class A:
#     def __init__(self):
#         print("This is A class Cons")
#     def abc(self):
#         print("This is method abc!")
        
# class B(A):
    
#     def __init__(self):
#         super().__init__()
#         print("This is B class Cons")
    
        
# class C(B):
#     def __init__(self):
#         super().__init__()
#         print("This is C class Cons")
#     def abc(self):
#         print("------")
#         super().abc()
#         print("This is method abc overrided!")
#         print("------")
# class D(C):
#     pass

# obj = D()
# obj.abc()
# obj1= A()
# obj1.abc()

# class Abc:
    
#     def __init__(self, i, j):
#         self.i = i
#         self.j = j
#         print("I am constructor of class ABC")
        
#     def logic(self):
#         print("I am function of class Math")
#         z = (self.i+self.j)/2
#         print(z)
        
# obj = Abc(10,12)
# obj.logic()

class Abc:
    def __init__(self):
        print("I am constructor from Abc")
        
    def logic(self):
        print("I am function of class ABc")
        
obj = Abc()
obj.logic()