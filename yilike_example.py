#单词每个字母都是大写字母
#单词没有连续的字母
word  =input('请输入单词:')

for i in range(len(word)):#循环单词长度的次数
    if word[i]<'A' or word[i]>'Z':
        print('不喜欢')
        break
    else:
        if i>0 and word[i]==word[i-1]:
            print('不喜欢')
            break
else:
    print('喜欢')


