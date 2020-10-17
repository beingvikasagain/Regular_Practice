dict1 = dict()
print(type(dict1))
dict1['name']='amit'
print(dict1)
dict1[1]=['Red','Yellow','Green']
dict1[2]=['Green','Blue']
print(dict1)

x = dict({'name':'Amit','age':22})
print(x)

print(x['name'])
print(x['age'])

x['age']=43
print(x)

y={1:10,2:11,3:12,4:13,5:14,6:15}
print(y)
y.pop(2)
print(y)
y.popitem()
print(y)

# y.clear()
print(len(y))
print(dict1.keys())
print(type(dict1.values()))
print(dict1.items())
print()
print(dict1.get(2))
print()
for item in dict1.items():
    print(item)
    
print()
aDict = {'host':'earth'}
print(type(aDict))
aDict['port']=80
print(aDict)

aDict['client']=[11,12,13,19,27,29]
print(aDict)

print(aDict.keys())
print(aDict['host'])
print(aDict['client'])

print(type(aDict['client']))

print()
for key,value in aDict.items():
    print(key,value)
    
for key in aDict:
    print(key, aDict[key])
    
d = dict()
print()
print(type(d))
d['name']="Amit"
d['age']=21
print(d)

print()
d1 = {1:'a',2:'b',3:'c'}
print(d1)

print(d["name"])
print(d["age"])

print(d.keys())
print(d.items())
print(d.values())

print()
for item in d.keys():
    print(d[item])
    
list1 = [{"name":"amit","age":21},{'name':"sumit",'age':24},{'name':"ajay",'age':45},{"name":"rohit","age":28}]
print(list1)
print()
i=0
while i<len(list1):
    d=list1[i]
    for item in d.keys():
        if item=='name':
            print(d[item])
    i+=1