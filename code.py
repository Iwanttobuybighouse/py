s='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFHGJKLZXCVBNM0123456789'
code=''
import random
j=3
while j>0:
    j-=1
    for i in range(4):
        ran = random.randint(0,len(s)-1)
        code+=s[ran]
    
    print('验证码:'+code)

    code_input =input('请输入验证码:')

    if code_input.lower()==code.lower():
        print('验证码输入正确！')
        break
    else:
        print('验证码错误！')
else:
    print('验证码错误3次！重新确认！')