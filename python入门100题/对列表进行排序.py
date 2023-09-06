

li = [3, 5, 17, 9, 14, 13]

#sort用法，会修改原列表，自己只是个函数
li.sort()
print (li)

#sorted用法，不会修改原列表，必须新定义参数，默认升序,会用reverse
lis = sorted(li, reverse = False)#后面那个reverse可以不写
print(lis)
lis = sorted(li, reverse = True)#True为降序
print(lis)
