

li = [1, 2, 3]

total = 0
for i in  li:
   total += i

#自建一个方法
"""
def sum_list(li):
    total = 0
    for i in li:
        total +=i 
    return total
"""

print ("列表的和是:",total)
print ("列表的和是:%s"%total)
print ("列表的和是:",sum(li))
print ("列表的和是:%s"%sum(li))