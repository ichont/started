

a = ["hello", "word", "yoyo", "congratulations"]

length = len(a[0])
for i in a:
    if len(i) > length :
        length = i
print(length )

result = []
for i in a:
    result.append(len(i))

print(result.index(max(result)))
print(a[result.index(max(result))])