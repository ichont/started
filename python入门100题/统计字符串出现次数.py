

s = "Hello, welcome to my world."

word = input ("请输入一个字符:")
num = 0


for i in s:
    if word == i:
        num += 1

if num == 0:
    print ("没有这个字符")

print ("%s一共出现了%d次" %(word, num))