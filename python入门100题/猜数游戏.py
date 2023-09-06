

import random

num = random.randint (1, 10)

print (num)
#guess = int (input("请输入一个数字："))


while True :

    guess = int(input("请输入一个数字："))
    if guess == num:
        print ("答对了")
        break
    elif guess > num:
        print ("你输入的数字大了")
    elif guess < num:
        print ("你输入的数字小了")