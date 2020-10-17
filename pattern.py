rows = 3
stop = 1
num=1

for i in range(rows):
    for column in range(stop):
        print(num, end=" ")
        num+=1
    print()
    stop+=2

print()
    
rows = 8
for i in range(1,rows+1):
    #print(i)
    for j in range(i-1,-1,-1):
        print(2**j, end="  ")
    print()
    
print()

rows = 8
for i in range(8):
    for j in range(i,-1,-1):
        print(2**j, end=" ")
    print()

print()

rows = 9
for i in range(rows):
    for j in range(i):
        print(2**j, end=" ")
    for k in range(j-1,-1,-1):
        print(2**k, end=" ")
    print()
    
print()
rows = 3
stop = 1
num=0
for i in range(rows):
    for i in range(stop):
        num+=1
        print(num, end=" ")
    print()
    stop+=2
print()

rows = 4
stop=1
num=1
for i in range(rows):
    for j in range(stop):
        print(num, end=" ")
        num+=1
    print()
    stop+=1
print()
        
start=1
stop=2
currentnumber = stop
for row in range(2,6):
    for col in range(start,stop):
        currentnumber -= 1
        print(currentnumber, end=" ")
    print(" ")
    start = stop
    stop += row
    currentnumber = stop

print()
rows = 5
lastevennumber = 2 * rows
for i in range(rows):
    evennumber = lastevennumber
    for j in range(i+1):
        print(evennumber, end=" ")
        evennumber -= 2
    print()
        
    