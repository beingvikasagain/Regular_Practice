# my_data = (10,)
# print(type(my_data))
# x = (1,2,3,4,5,6,7)
# print(x)
# list1 = []
# x=(1,2,3,4,5,6,7)
# y=(8,9,10)
# list1.extend(x)
# list1.extend(y)
# print(list)

x = (1,2,3,4,5,6,7)
print(x)
print(type(x))
y = list(x)
print(x*2)
print(y*2)

print(('A','B')+('C','D')+('E','F')+(1,2,3,4))
print((1,2,3,4,'A','B'))
print(5 in x)
print(16 in x)

print("Length of tuple",len(x))
print("Max in tuple", max(x))