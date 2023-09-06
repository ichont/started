

def read_file():
    result = {}

    with open("student1.txt ", "r", encoding= "utf-8") as f:
        content = f.read()
        words = content.split(" ")
        for word in words :
            if word not in result :
                result[word] = 0
            result[word] +=1
    return result


words = read_file()
from collections import Counter
count = Counter(words)
print(count.most_common(1))
max_word = count.most_common(1)[0][0]
max_count = count.most_common(1)[0][1]
print("文章中出现最多的单词是%s，出现了%s次"%(max_word, max_count))