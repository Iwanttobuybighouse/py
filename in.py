name = 'steven'

result='eve'in name
print(result)



############
print(r'%s说:\'哈哈哈!\''%name)

filename='picture.png'#0123456789
                      #-9 -8-7 -6 -5 -4 -3 -2 -1

print(filename[5])#只能获取一个字母

print(filename[0:7])#包前不包后

print(filename[3:7])#截取字符串

print(filename[3:])#表示一直取到字符串末尾
print(filename[:5])#表示从0 开始取值


print(filename[8:-1])
print(filename[:-2])
print(filename[-1:])
print(filename[-5:-1])
print(filename[3:0])

#[::-1]倒叙
print(filename[::-1])

print(filename[-1:-5:-1])

print(filename[5:0:-1])

print(filename[5:0:1])

print(filename[::2])#间隔一个
print(filename[::-3])#间隔两个
