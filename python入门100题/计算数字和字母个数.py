

#s = input("请输入一个字符串:")
s = "hellow word 123456"


s_count = 0
n_count = 0

for char in s :
    if char.isalpha() :
        s_count += 1
    elif char.isdigit() :
        n_count  += 1


print("字母的数量是：", s_count )
print("数字的数量是：", n_count )