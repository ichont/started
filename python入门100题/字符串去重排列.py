

s = "abcdcdcacdcbbabcdab"

se = set(s)
print(sorted(se))

result = []
for i in s:

    if i in result:
        result.remove(i)
    result.append(i)


print(sorted(result))
