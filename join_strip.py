new_str = '-'.join('abc')
print(new_str)

#列表--list=['a','v','o','9']--数字
list1=['a','v','o','9']
result = ' '.join(list1)
print(result)

result = ''.join(list1)
print(type(result))

#lstrip rstrip strip

s='           hello                 '
s=s.lstrip()#去除字符串左侧的空格
print(s+'8')

s=s.rstrip()#去除字符串右侧的空格
print(s+'8')

s='           hello                 '
s = s.strip()
print(s+'8')