# for i in range(0,5):
#     for j in range(0,i):
#         print(j, end="")
#     print()
    
    
# print()
# print()

# for i in range(0,6):
#     for j in range(i,6):
#         print(j, end="")
#     print()
    
# print()
# print()

# for i in range(1,6):
#     for j in range(0,i):
#         print(i, end="")
#     print()
    
# print()
# print()

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j, end="")
#     print()
    
# print()
# print()

# for i in range(1,6):
#     for j in range(6,i,-1):
#         print(i, end="")
#     print()
    
# print()
# print()

# row = 5
# b= 0
# for i in range(row,0,-1):
#     b+=1
#     for j in range(1,i+1):
#         print(b, end="")
#     print()
    
# print()
# print("Check this")


# for i in range(5, 0,-1):
#     for j in range(1,i+1):
#         print("5", end="")
#     print()
    
# print()
# print()

# row = 5
# for i in range(row,0,-1):
#     for j in range(1,i+1):
#         print(i, end="")
#     print()
    
# print()
# print()

# rows = 5
# for i in range(5,0,-1):
#     for j in range(0,i+1):
#         print(j, end="")
        
#     print()
    
# print()
# print()

# rows = 5
# for i in range(5,0,-1):
#     for j in range(0,i+1):
#         print(j, end="")
#     print()
# print()
# print()
    
# rows = 5
# for i in range(1,rows+1):
#     for j in range(i,0,-1):
#         print(j, end=" ")
#     print()
        
# print()
# print()

# rows = 8

# for i in range(1,rows+1):
#     for j in range(-1+i,-1,-1):
#         print(2**j, end=" ")
#     print()
               
# print()
# print()

# rows = 8
# for i in range(0,rows):
#     for j in range(i,-1,-1):
#         #print(j)
#         print(2**j, end=" ")
#     print()
    
# print()
# print()

# rows = 8
# print(1)
# for i in range(1,rows):
#     for j in range(0,i):
#         print(2**j,end=" ")        
#     for k in range(i,-1,-1):
#         print(2**k, end=" ")
#     print()
# print()
# print()

# rows=9
# for i in range(1,rows):
#     for i in range(0,i,1):
#         print(2**i, end=" ")
#     for i in range(-1+i,-1,-1):
#         print(2**i, end=" ")
#     print(" ")

# aDict = {'host':'earth'}
# print(type(aDict))

# aDict['port'] = 80
# print(aDict)

# aDict['client']=[11,12,13,19,27,29]
# print(aDict)

# print(aDict.keys())
# print(aDict['host'])
# print(aDict['client'])
# print(type(aDict['client']))
# for key in aDict:
#     print(key,aDict[key])

d = {}
print(d)
print(type(d))

d['name']="Amit"
print(d)
d['age'] = 21
print(d)

d1 = {1:'a',2:'b',3:'c'}
print(d1)

print(d['name'])
print(d['age'])

print(d.keys())
print(d.items())
print(d.values())

for item in d.keys():
    print(d[item])
    
list1 = [{"name":'amit','age':21},{'name':'sumit','age':24},{'name':'ajay','age':45}]
print(list1)

i=0
while(i<len(list1)):
    d = list1[i]
    for item in d.keys():
        if item == 'name':
            print(d[item])
    i+=1