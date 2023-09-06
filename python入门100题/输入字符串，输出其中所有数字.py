

s = input("请输入字符串:")


result = []

for i in s :
    if i.isdigit() :
        result.append(i)


print ("字符串中的数字是:", "".join(result))