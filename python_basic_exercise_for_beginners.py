# def myfun(income):
#     tax1 = tax2 = tax3=0
#     if income<=10000:
#         tax1 = 0
#         return tax1
#     elif income<=20000:
#         excess_amt = income-10000
#         tax2 = excess_amt*0.1
#         return tax2
#     else:
#         tax1 = 0
#         tax2 = 10000 * 0.1
#         rest_amt = income - 20000
#         tax3 = rest_amt * 0.2
#         return tax3
    
# mytotaltax = myfun(10000)    
# print(mytotaltax)

# def mytable(num):
#     for i in range(1,num+1):
#         for j in range(1,11):
#             print(i*j, end=" ")
#         print()

# mytable(10)

# def mypattern():
#     rows = 5
#     for i in range(rows,0,-1):
#         for j in range(i):
#             print("*",end="")
#         print()
# mypattern()

def myfun(base,exp):
    return base**exp

result = myfun(5,4) 
print(result)