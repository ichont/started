

s = "05350535"

try:
    if s.isdigit():
        print("是数字")
    else:
        print("不是纯数字")
except Exception as e:
    print (e)