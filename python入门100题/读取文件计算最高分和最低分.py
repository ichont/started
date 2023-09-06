

def read_file():
    result = []
    with open ("student.txt ","r",encoding= "utf-8") as f:
        while True :
            line = f.readline()
            if len(line) == 0:
                break
            #print(line)
            scores = line.split(",")[-1].strip()
            result.append(scores)
    return result


scores = read_file()
max_scores = max(scores)
min_scores = min(scores)
print("学生最高分是:",max_scores )
print("学生最低分是:",min_scores )