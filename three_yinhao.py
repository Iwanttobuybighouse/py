s1='abc'
s2="abc"
s3='''abc'''
s4='''
abc
'''
print(id(s1),id(s2),id(s3),id(s4))
print(s1==s2)
print(s1 is s2)
print(s1==s3)
print(s1 is s3)
print(s1==s4)
print(s1 is s4)


s1=input('请输入s1:')
s2=input('请输入s2:')
print(s1==s2)
print(s1 is s2)

print(id(s1),id(s2))
