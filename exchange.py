#大小写相关
#capitalize()   将字符串第一个字符串转写成大写的标识形式
#title()        返回的是将字符串每个单词首字母转成大写的字符串
#istitle()      返回的是布尔类型
#upper()        转大写
#lower()        转小写

#len()          返回字符串长度

message ='mo is a beautiful girl!'

msg =message.capitalize()
print(msg)

msg =message.title()
print(msg)

result = message.istitle()
print(result)

result = msg.istitle()
print(result)

msg = message.upper()
print(msg)

result=msg.lower()
print(result)


print(len(message))

