

li = [10, 20, 30, 10, 30]

uli = []
for i in li:
    if i not in uli:
        uli.append(i)


print ("去除重复之后的列表是:", uli)


print(set(li))

