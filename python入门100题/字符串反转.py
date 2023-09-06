

s = input ("请输入一个字符串")
print (s)
print(s[ : :-1])#-1为步长，正常为1，-1就是倒着读取

result = []
for i in s:
    #result = [],放在这里是错的，不能重复定义
   #print (i)
    result.append(i)


result.sort(reverse= True )#对中文无效，中文不是逆序，是按照拼音首字母降序排列
print ("".join(result))