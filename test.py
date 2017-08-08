#encoding:UTF-8
print('hello')

print("good")

def manc():

    print("nizhend meiyoushenm")

print(manc(),'zhend hao')


import sys

def man():

    print ('hello world',sys.argv[0])



if __name__=='__main__':

    print(man())


    print("\t  zhoulvlv.\n ni shi ge da huai dan! \n")


def repeat(s,exclaim):

    result =s+s+s+s

    if exclaim :
        result = result + '!!!'

    return result


print (repeat("zhoulvlv",True))



'''
if name =='wang':
    print(repeat(name)+'!!!!')
else:
    print(repeat(name))
'''


print(2**10)

'''import sys
print('================Python import mode==========================');
print (':')
for i in sys.argv:
    print (i)
print ('\n python ',sys.path)'''

# this is the test for 



