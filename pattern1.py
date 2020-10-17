row = 4
num=1
for i in range(row):
    for j in range(i+1):
        print(num, end=" ")
        num+=1
    print()
    
print()

row = 3
stop = 2
currentnumber = 1

for i in range(row):
    for j in range(1,stop):
        print(currentnumber, end=" ")
        currentnumber+=1
    stop+=2
    print()
    
row =4
num= 1
for i in range(4):
    for j in range(i+1):
        print(num, end=" ")
        num+=1
    print()
    
print()

rows = 5
start = 0
for i in range(1,rows):
    start+=i
    current_value=start
    for j in range(i):
        print(current_value, end=" ")
        current_value-=1
    print()
    
print("------------")

rows = 6
start = 10
for i in range(1,rows):
    current_val = start
    for j in range(i):
        print(current_val, end=" ")
        current_val-=2
    print()

print("------------")

rows = 6

for i in range(1,rows+1):
    for j in range(1,i-1):
        print(j, end=" ")
    for k in range(i-1,0,-1):
        print(k, end=" ")
    print()
    
print("------------")

rows = 6
for i in range(1,rows+1):
    for j in range(1,i-1):
        print(j, end=" ")
    for j in range(i-1,0,-1):
        print(j, end=" ")
    print()
    
print("------------")
rows = 5
for i in range(rows,0,-1):
    for j in range(i,0,-1):
        print(j, end=" ")
    print()
        
print("------------")

rows = 7
for i in range(1,rows+1):
    for j in range(i):
        print(j*(i-1), end=" ")
    print()
    
print("------------")
rows = 5
start = rows
num = 1
for i in range(1,rows+1):
    current_val = i
    for j in range(start,0,-1):
        print(current_val, end=" ")
        current_val+=1
    start-=1
    print()
print("------------")