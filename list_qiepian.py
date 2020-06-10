#字符串的切片操作
list1 = ['杨超越','佟丽娅','杨幂','刘亦菲',100,99,9.9]

print(list1)
print(list1[3])

#列表也支持切片
print(list1[3:6])
print(list1[-1:])
print(list1[-3:-1])
#步长
print(list1[::2])

print(list1[1-5:-1:2])

#反方向
print(list1[-1::-1])
print(list1[-1::-2])
