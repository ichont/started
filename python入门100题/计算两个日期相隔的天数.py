

from datetime import datetime


date1 = input("请输入第一个日期(xxxx-xx-xx):")
date2 = input("请输入第二个日期(xxxx-xx-xx):")

date1 = datetime.strptime(date1, "%Y-%m-%d")
date2 = datetime.strptime(date2, "%Y-%m-%d")

day = date2 - date1
print("两个日期相隔的天数:", day.days )