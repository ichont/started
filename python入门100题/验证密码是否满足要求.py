
"""
要求：
1.长度在[6,20]之间
2.必须包含至少一个小写字母
3.必须包含至少一个大写字母
4.必须包含至少一个数字
"""

import re

code = input("请输入你的密码:")

def check_password(password):
    if not 6 <= len(password) <= 20:
        return False, "密码长度在[6,20]之间"
    if not re.findall(r"[a-z]", password):
        return False, "密码必须包含至少一个小写字母"
    if not re.findall(r"[A-Z]", password):
        return False, "密码必须至少包含一个大写字母"
    if not re.findall(r"[0-9]", password):
        return False, "必须包含一个字母"
    return True

print (check_password(code) )
