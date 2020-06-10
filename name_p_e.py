#循环提示用户输入用户名，密码和邮箱
s=''
while True:
    username = input('请输入用户名:')
    password = input('请输入密码:')
    email = input('请输入邮箱:')

    username=username[0:20]
    password=password[0:20]
    email = email[0:20]
    if username=='q' or username =='Q'or password=='q' or password =='Q'or email=='q' or email =='Q':
        break 
    msg ='{}\t{}\t{}\n'.format(username,password,email)

    msg=msg.expandtabs(20)#把tab改为20
    s+=msg
print(s)
