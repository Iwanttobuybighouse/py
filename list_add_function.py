#list列表的添加：
#临时的小数据库


#传建一个空列表
girls=['杨幂']
while True:
    name=input('请输入你心目中的美女名字:')

#列表的函数:append extends insert
#append()末尾追加
    if name=='quit':
        break
    girls.append(name)
print(girls)

#extend 用于合并列表
names=['黑嘉嘉','孙俪','巩俐']
name=input('请输入你心目中的美女名字:')
girls.extend(names)
print(girls)
#符号+ 也可以用于合并列表

girls =girls+names
print(girls)

#insert 指定位置插入，其后往后移
girls.insert(1,'刘涛')
print(girls)

