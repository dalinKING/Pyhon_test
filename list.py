"""# list test for append , insert sort()  reverse() remove() 

# just take test！！TypeError: 'int' object is not iterable

# list test for append , insert sort()  reverse() remove()  
"""



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

print("-" *60)


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
print("-" *60)
shcool=(22,"ee",90)
print(shcool)
print(shcool[2])

print(type(shcool))

# 不能修改元祖里面的值  其他跟list差不多   元祖单一 加逗号

#  dict___ {key:value,key:value,key:value,key:value,key:value,key:value}
print("-" *60)
info={"name":"haone","sex":"man","wife":"wangrong"}

print(info.keys())

print(info["sex"])

print(type(info))

print(info.items(),"\n",info.get("wife"))
print("-" *60)
info["monly"]=8000
print(info)
del info["sex"]

print(info.get("monly"))

print(info)
print("-" *60)
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
print("-" *60)
for i,n in enumerate(number):
    print(i,n,end='-')
print(end='\n')
# 常用函数  cmp() 比较两个值    len()计算个数    max()最大值   min()   del()

#  print(cmp(number,number))
print("the max in number is:",max(number))
print("the min in number is:",min(number))
print("the len in info is:",len(info))
print("-" *60)

amount =10000
inrate =0.15
period =5
value = 0
year =1
print("-" *60)
while year <= period:
    value =amount + (inrate*amount)
    print("Year {} Rs. {:.2f}".format(year,value))   # 字符串格式化 str.format()中的参数 传到 {}中
    amount = value
    year +=1

print("-" *60)
fahrenheit =0
print("F.Celsius")
while fahrenheit <=250:
    Celsius =(fahrenheit-32)/1.8  #转为华氏温度
    print("{:5d}  {:7.2f}".format(fahrenheit ,Celsius))
    fahrenheit +=50


i = 1
print("-" *60)
while i < 11:
    n =1
    while n<= 10:
        print("{:5d}".format(i*n),end=' ')  # 乘法表！
        n +=1
    print()
    i +=1
print("-" *60)

#fopen = open("./test.py")
#fopen.read()
# 类的继承！！！！！
class Person(object):
    def __init__(self,name):
        self.name =name

    def get_details(self):
        return self.name

class Student(Person):
    def __init__(self,name,branch,years):
        Person.__init__(self,name)
        self.branch =branch
        self.years = years
    def get_details(self):
        return "{} studens{} and is in {} year.".format(self.name,self.branch,self.years)

class Teacher(Person):
    def __init__(self,name,papers):
        Person.__init__(self,name)
        self.papers =papers

    def get_details(self):

        return "{} teachs {}".format(self.name,','.join(self.papers))

person1 =Person ('jiami')
#studentter= Student('Kutasha','CSEA',2005)
stufen = Student('Kutasha','CSEA',2005)
teacehr1 = Teacher('piter',['C++','JAVA','PHP'])
print(person1.get_details())
print(stufen.get_details())
print(teacehr1.get_details())
print("-" *60) 


#global

G_list=[22,15,48,69,3]

def A() :
    G_list.append(59)
    return G_list

print(A())

#/////////  file system operation

f=open("README.md",'r')
print(f.read())
f.seek(0,0)
print(f.readlines())
f.close()


MYSTR_Llist = str(info)
print(type(MYSTR_Llist),MYSTR_Llist)

print(type(eval(MYSTR_Llist)))


class Man_:
    def __init__(self,name):
        self.name = name
        self.xue = 1000
    
    def reload(self,danjia,zidan):
        danjia.save(zidan)
class Danjia:
    def __init__(self,conten):
        self.contenler = conten
        self.contenlerList = []
    def save(self,zidan):
        if len(self.contenlerList) < self.contenler:
            self.contenler.append(zidan)
            

class Zidan:
    pass

class Qiang:
    pass

king = Man_("dalin")
danjia = Danjia
zidan = Zidan
print(king.name)


