

li = ["hello", "word", "yoyo"]


new = ""
for i in li:
    new += i + "_"

print(new.rstrip("_") )

print("_".join(li))