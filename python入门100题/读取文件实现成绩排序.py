

def read_file():
    result = []

    with open("student.txt ","r", encoding= "utf-8") as f:
        while True :
            line = f.readline()
            if len(line) == 0:
                break
            scores = line.split(",")[-1].strip()
            result.append(scores)
    return result


scores = read_file()
scores.sort()
scoress = sorted(scores,reverse=True)#倒序这样来搞
print("学生成绩排名:",scores)
print("学生成绩倒序排名:",scoress)
