

import re


content = '小s上街买菜，买了3斤黄瓜花了9元;买了4斤苹果花了13元;买了5斤西瓜花了5元'

for data in content.split(";"):
    result = re.search(r"买了(\d)斤(.*)花了(\d+)元", data)
    print (result.groups())