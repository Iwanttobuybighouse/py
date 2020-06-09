import random

print('*'*30)
print('欢迎进入澳门赌场!')
print('*'*30)

username = input('请输入顾客大名:')
money =0
answer = input('确定进入游戏吗？（y/n）')

if(answer=='y'):
    while money<2:
        n=int(input('金币不足，请充值（100的倍数）:'))
        money+=n
print('当前剩余游戏币是{}，玩一局游戏扣除2个游戏币'.format(money))
print('进入游戏。。。。。。')

while True:
    #模拟筛子的值
    t1=random.randint(1,6)
    t2=random.randint(1,6)

    print('系统洗牌完毕，请猜大小:')
    guess = input('输入大或者小')

    #判断
    if((t1+t2)>6 and guess=='大') or ((t1+t2)<=6 and guess == '小'):
        print('恭喜{}！本局游戏获奖励1个游戏币！'.format(username))
        money += 1
    else:
        print('很遗憾！本局游戏输啦！')
        
    answer = input('是否再来一局游戏,要扣除2枚游戏币？（y/n)')
    if answer!='y' or money<2:
        print('退出游戏!')
        break
