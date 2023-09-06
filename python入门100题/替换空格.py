

a = "we are happy"


def demo(s):
    new = ""
    for i in s:
        if i == " ":
            new += "!"
        else:
            new += i
    return new


print (demo(a))