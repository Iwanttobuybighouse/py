#产生10个随机数，将其保存到列表中

#产生随机数
#将随机数放到列表中

import random
ranlist=[]

#for i in range(10):
i=0
while i <10:
    ran=random.randint(1,20)
    if ran not in ranlist:
        i+=1
        ranlist.append(ran)
        

print(ranlist)

###找出列表中最大值
##max_value=max(ranlist)
##print(max_value)
##min_value=min(ranlist)
##print(min_value)
##sum_value=sum(ranlist)
##print(sum_value)
##
##print('#'*40)
##max_value=ranlist[0]
##min_value=ranlist[0]
##sum_value=0
##for i in ranlist:
##    sum_value+=i
##    if i>max_value:
##        max_value=i
##    if i<min_value:
##        min_value=i
##print('最大值是:',max_value)
##print('最小值是:',min_value)
##print('和是:',sum_value)

#排序:sorted 排序 默认升序  
new_list = sorted(ranlist)
print(new_list)
new_list = sorted(ranlist,reverse=True)#降序
print(new_list)
