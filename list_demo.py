#声明 list
names = ['Jack','Tom','Lucy','super','jackson','jacky']

computer_brands=[]

#地址
print(id(names))
print(id(computer_brands))


print(names[0])
print(names[1])

#获取最后一个元素
print(names[-1])

print(len(names))
print(len(computer_brands))

#获取第一个元素
print(names[-4])

for name in names:
    if name=='super':
        print(name)

if 'super' in names:
    print('super')

print(names)

#names[-1]='Hasee'

for name in names:
    if 'super' in names:
        name ='aaa'

print (names)   #name ='aaa'但是列表内还是没有改变

for i in range(len(names)):
    if 'super' in names[i]:
        names[i]='aaa'  #这个时候names才改为'aaa'
        break
print(names)
print('*'*20+'删除'+'*'*20)
del names[2]
print(names)
del names[2]
print(names)

print('*'*30+'删除'+'*'*30)
I=len(names)

##for i in range(l):
##    if 'jack' in names[i]:
##        del names[i]
i=0
while i<I:
    if'jack'in names[i]:
        del names[i]
        I-=1;
        i-=1;
    i+=1;
    print(i)
print(names)
