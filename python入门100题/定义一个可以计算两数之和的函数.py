

n1 = input("请输入一个数字:")
n2 = input("请输入一个数字:")


def sum_sum(n1, n2):
    try:
        n1 = float(n1)
        n2 = float(n2)
        return n1 + n2
    except:
        print("你输入的不是数字")


print(sum_sum(n1, n2))