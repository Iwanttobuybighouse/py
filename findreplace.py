#替换

#find()     返回-1代表没找到，否则返回字母第一次出现的位置
#rfind()    从右侧检索
#lfind()
#index()    index(str,beg=0,end=len(string))跟find一样，只不过字符或字符串不在指定字符串内会报一个异常


#rindex()
#lindex()
#replace()  将字符串中的str1替换成str2，如果max指定，则替换不超过max次

message ='mo is a beautiful girl!'
result = 'c' in message


position = message.find('c')
print(position)

position = message.find('a')
print(position)

p= message.find('a',position+1,len(message)-5)#指定开始位置找
print(p)

url='https://blog.csdn.net/u011535541/article/details/83379151'

p=url.rfind('/')
print(p)

filename = url[p+1:]
print(filename)

p=url.rfind('.')
print(p)

filename = url[p+1:]
print(filename)

##p='hello'.index('x')
##print(p)


rurl=url.replace('/','//')
print(rurl)
rurl=url.replace('/','')
print(rurl)
