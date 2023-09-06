

li = [1, 2, 3, 4, 5]

print (list(map(lambda x:x**2, li)))#lambda方法比较晦涩


def demo(x):
    return x * x

print(list(map(demo, li)))


lis = [1, 4, 9, 16, 25]
result = [x for x in lis if x>10]
print (result)

results = [x for x in map(lambda  x:x**2, li) if x > 10]#合到一起使用
print (results)