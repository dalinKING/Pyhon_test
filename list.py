'''
# list test for append , insert sort()  reverse() remove() 

# just take test！！TypeError: 'int' object is not iterable

# list test for append , insert sort()  reverse() remove()  '''



number=[36,5,56,3,2,8,7,9,6,5,47,4,7,152]
number.sort(reverse=False)
print(number)


def good(list):

   list.append(88)
   number.sort(reverse=True)

good(number)
print(number)


for name in range(len(number)):
    if number[name]==9:
        print("ni hao ",number[name],"weizhishizai",name)
        name+1
        break
else:
    print("is none")




#ber = len(number)
#print (ber)

Mywill=20

print("The number totle %d option\n"%len(number))
ber=0

while (ber < len(number)):
    if number[ber]==Mywill:
       print("you have found your number is %d in %d times"%(number[ber],ber+1))
       break
    else:
        ber += 1


else:
    print("you have not find %d"%Mywill)
    

#  tuple test

shcool=(22,"ee",90)
print(shcool)
print(shcool[2])

print(type(shcool))

# 不能修改元祖里面的值  其他跟list差不多   元祖单一 加逗号

#  dict___ {key:value,key:value,key:value,key:value,key:value,key:value}

info={"name":"haone","sex":"man","wife":"wangrong"}

print(info.keys())

print(info["sex"])

print(type(info))

print(info.items(),"\n",info.get("wife"))

info["monly"]=8000
print(info)
del info["sex"]

print(info.get("monly"))

print(info)

for n in number:
    print(n,end='-')

for n in shcool:
    print(n,end='-')

print(end='\n')
for n in info.keys():
    print(n,end='-')
print(end='\n')
for n in info.values():
    print(n,end='-')
print(end='\n')
for x,y in info.items():
    print(x,"=",y)
print(end='\n')

# ///////// enumerate !!!

for i,n in enumerate(number):
    print(i,n,end='-')
print(end='\n')
# 常用函数  cmp() 比较两个值    len()计算个数    max()最大值   min()   del()

#  print(cmp(number,number))
print("the max in number is:",max(number))
print("the min in number is:",min(number))
print("the len in info is:",len(info))

