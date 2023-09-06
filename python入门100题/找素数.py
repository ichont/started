

#s = int(input ())
#e = int(input ())

s,e =map (int,input("请输入范围：").split())

#s = 1
#e = 10


def demo (s,e):
    result = []
    for i in range (s,e+1):
        if is_prime(i):
            result.append(i)
    return result


def is_prime(n):
    if n <= 1:
        return False
    for i in range (2, n):
        if n % i == 0:
            return False
    return True

print (demo(s,e))