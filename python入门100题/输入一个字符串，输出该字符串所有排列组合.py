

import itertools

def demo(s):
    result = list(itertools.permutations(s))
    for i in result:
        new = "".join(i)
        print(new)


demo("abc")