# def myfun():
#     age = int(input("Enter age: "))
#     name = input("Enter name: ")
#     print("{} is {} years old".format(name,age))
    
# myfun()

# def myfun(**args):
#     for item in args.items():
#         print(item)
        
# myfun(name='vikas',age=21)

# def myfun(*args, **kwargs):
#     print(args)
#     print(kwargs)
    
# myfun(20,13,'vikas','kumar',age=21,salary=20000)

# def calculation(a,b):
#     add = a+b
#     sub = a-b
#     return add,sub

# add,sub = calculation(20,10)
# print(add)
# print(sub)

# def showEmployee(name, salary=9000):
#     print("Employee {} Salary is {}".format(name,salary))
# name = input("Enter a name: ")
# salary = int(input("Enter salary: "))
# showEmployee(name,salary)

# def outer():
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     def inner(a,b):
#         return a+b
#     return inner(a,b)

# result = outer()
# print(result)

# def outer(a,b):
#     def inner(a,b):
#         return a+b
#     return inner(a, b)+5

# result = outer(10,5)
# print(result)
# def myfun(n):
#     result = 0
    
#     if n<=0:
#         return 0
#     else:
#         result = n+myfun(n-1)
#         return result
    
# result = myfun(10)
# print(result)

# def myfun():
#     print("This is myfunction!")
# mynewfun = myfun
# mynewfun()

mylist = [item for item in range(4,31) if item%2==0]
print(mylist)
print(max(mylist))