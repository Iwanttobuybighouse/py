#筛选a字符串中b字符串没有的字符
a=input('请输入第一个字符串')
b=input('请输入第二个字符串')
for i in b:
    a=a.replace(i,'')
print(a)
