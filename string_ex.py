# str1 = "JaSonAy"
# def myfun(mystr):
#     start = (len(mystr)-3)//2
#     return mystr[start:start+3]

# result= myfun(str1)
# print(result)

# def mynewfun(mystr):
#     mid = len(mystr)//2
#     start = mid-1
#     end = mid+2
#     return mystr[start:end]
# result = mynewfun(str1)
# print(result)

# def myfun1(str1,str2):
#     mid = len(str1)//2
#     mynewstr = str1[:mid]+str2+str1[mid:]
#     print(mynewstr)

# myfun1('Ault','Kelly')

# def myfun2(s1,s2):
#     s3 = s1[0]+s2[0]+s1[int(len(s1)/2):int(len(s1)/2)+1]+s2[int(len(s2)/2):int(len(s2)/2)+1]+s1[-1]+s2[-1]
    
#     print(s3)
    
# myfun2('America','Japan')

# def mych(s1):
#     mylower = []
#     myupper = list()
#     for i in s1:
#         if i.islower():
#             mylower.append(i)
#         else:
#             myupper.append(i)
#     newstr = ''.join(mylower)+''.join(myupper)
#     print(newstr)
    
# mych("PaEsIdYTss")
# print("----------")

# def myfun3(s1):
#     count_lower = count_upper = count_digit = count_specialch = 0
#     for i in s1:
#         if i.isdigit():
#             count_digit+=1
#         elif i.islower():
#             count_lower+=1
#         elif i.isupper():
#             count_upper+=1
#         else:
#             count_specialch+=1
            
#     print("count_digit:",count_digit,"count_lower: ",count_lower, "count_upper",count_upper,"count_special:",count_specialch)
    
# myfun3("P@#yn26at^&i5ve")

# s1 = "Abc"
# s2 = "Xyz"

# s2 = s2[::-1]

# lens1 = len(s1)
# lens2 = len(s2)

# length = lens1 if lens1>lens2 else lens2
# resultstr = ' '
# for i in range(length):
#     if i<lens1:
#         resultstr+=s1[i]
#     if i<lens2:
#         resultstr+=s2[i]
    
# print(resultstr)

# resultstr = ""
# for i in range(len(s1)):
#     if i<len(s1):
#         resultstr+=s1[i]
#     if i<len(s2):
#         resultstr+=s2[i]
        
# print(resultstr)

# s1 = "yn"
# s2 = "Pynative"
# print(s1 in s2)

# str1 = "Welcome to USA usa awesome, isn't it?"
# mylist = str1.lower().split()
# print(mylist)

# print(mylist.count('USA'.lower()))

# str1 = "JhonDipPeta"
# mynewstr = ''
# mynewstr = str1[int(len(str1)/2-1):int(len(str1)/2+2)]
# print(mynewstr)

# s1 = "Ault"
# s2 = 'Kelly'

# newstr = s1[:2]+s2+s1[2:]
# print(newstr)

# s1 = "America"
# s2 = 'Japan'

# newstr = s1[0]+s2[0]+s1[len(s1)//2]+s2[len(s2)//2]+s1[-1]+s2[-1]
# print(newstr)

# str1 = 'PyNaTive'
# count_low = count_upper = ''
# for char in str1:
#     print(char.islower())
#     if char.islower():
#         count_low+=char
#     if char.isupper():
#         count_upper+=char
# print(count_low)
# print(count_upper)
# mynewstr = count_low+count_upper
# print(mynewstr)

# str1 = 'P@#yn26at^&i5ve'
# chars = digits = symbol = 0
# for i in str1:
#     if i.isdigit():
#         digits+=1
#     elif i.islower() or i.isupper():
#         chars+=1
#     else:
#         symbol+=1
# print("Char: ",chars)
# print("Digits: ",digits)
# print("Symbol: ",symbol)

# s1 = "Abc"
# s2 = "Xyz"
# s2_reverse = s2[::-1]
# newstr=''
# length = len(s1) if len(s1)>len(s2) else len(s2)
# for i in range(length):
#     if i<len(s1):
#         newstr+=s1[i]
#     if i<len(s2):
#         newstr+=s2_reverse[i]
# print(newstr)

# s1 = "Ynf"
# s2 = "PYnative"

# print(s1 in s2)

# str1 = "Welcome to USA . usa awesome, isn't it?"
# str1.lower()
# count = str1.lower().split().count('usa')
# print(count)

# str1 = "English = 78 Science = 83 Math = 68 History = 65"
# digi_list = list()
# for item in str1.split():
#     if item.isdigit():
#         digi_list.append(int(item))
# total_ = sum(digi_list)
# avg_ = sum(digi_list)/len(digi_list)
# print("Total: ",total_)
# print("Average: ",avg_)

# str1 = "Apple"
# mydic = dict()
# count=1
# for i in str1:
#     item = i.count(i)
#     mydic[i]=item
    
# print(mydic)

# str1 = "PYnative"
# print(str1[::-1])

# str1 = "Emma is a data scientist who knows Python. Emma works at google."
# idx = str1.rfind('Emma')
# print(idx)

# str1 = "Emma-is-a-data-scientist"
# mystr = str1.split("-")
# for item in mystr:
#     print(item)

# str_list= ['Emma','Jon','','Kelly',None,'Eric','']
# new_list = list()

# for item in str_list:
#     if item=='' or item is None:
#         str_list.remove(item)
        
# print(str_list)

# import string
# str1 = "/*Jon is @developer & musician"
# new_str = str1.translate(str.maketrans('','',string.punctuation))
# print(new_str)

# import re
# str2 = re.sub(r'[^\w\s]', '', str1)
# print(str2)

# str1 = "I am 25 years and 10 months old"
# res = "".join([item for item in str1.split() if item.isdigit()])
# print(res)

