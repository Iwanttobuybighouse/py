msg='上课啦！认真听课！'

result =msg.encode('utf-8')
print(result)

m =result.decode('utf-8')
print(m)


#字符串内建函:startswith()    enswith()

filename='笔记.doc'

result=filename.endswith('doc')#filename是否以doc结尾

print(result)


s='hello'
result=s.startswith('he')
print(result)


#文件上传 只能上传图片（JPG，png，gif)
while true:
    path = input('请选择文件:')

    p = path.rfind('\\')

    filename = path[p+1:]

    print(p,filename)

    #判断是否是图片类型?
    if filename.endswith('jpg')or filename.endswith('png') or filename('gif'):
        print('允许上传！')
        break
    
    else:
        print('不是允许上传的文件格式')
