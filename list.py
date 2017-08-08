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
    