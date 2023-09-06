

import re

content = "hello 123456789@qq.com hello 456789123__-@qq.com"


pattern = re.compile(r"[a-zA-Z0-9_-]+@[A-Za-z0-9]+\.[a-zA-Z]+", re.S)

email = re.findall(pattern, content)
print (email)