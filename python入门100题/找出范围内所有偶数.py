

n1 = int(input("请输入一个数:"))
n2 = int(input("请输入一个数:"))


def num(n1, n2):
    result = []
    for i in range (n1,n2+1):
        if i % 2 == 0:
            result.append(i)

    return result


print ("[%d,%d]区间范围内的偶数是:"%(n1,n2), num(n1,n2))

