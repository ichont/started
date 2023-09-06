

def sum_sum(n):
    #result = 0
    #for i in range (1, n+1):
    #    result += i*i
    #return result
    return n*(n+1)*(2*n+1)/6#数学公式


n = int (input ("请输入一个数字："))


print("结果是:%d" %(sum_sum(n)) )
