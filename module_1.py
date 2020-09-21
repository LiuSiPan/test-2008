
# import os
# print(os.listdir())
#
# import random
# print(random.randint(1,90))
# print(random.random())
# print(random.choice("1234"))
# l = random.choices("12345678",k=10)
# print(l)
# print(",".join(l))

# import time
# print(time.time())
# print(time.localtime(time.time()))
# t = time.strftime("%Y-%m-%d %H:%M:%S")




# 1、编写一个返回随机手机号的方法
# 2、编写一个返回指定长度和内容的随机字符串方法
# 3、编写一个返回随机姓名的方法

import random

def randomPhone():
    print("-----------------随机手机号---------------------")
    l = random.choices("123456789", k=9)
    s = random.choice("3578")
    str = "1" + s + "".join(l)
    print(str)
randomPhone()

def randomChangeLenStr(num, str):
    print("\n-----------------指定字符串长度---------------------")
    l = random.choices(str, k=num)
    print("".join(l))
randomChangeLenStr(9,"sdfghjkldfghj")

def randomName(fStr, sStr):
    print("\n-----------------随机姓名---------------------")
    str1 = random.choice(fStr)
    str2 = "".join(random.choices(sStr,k=random.randint(1,3)))
    print(str1+str2)
fStr = "王刘吴周于"
sStr = "一二三四五六"
randomName(fStr,sStr)

print("\n-----------------异常处理---------------------")
try:
    # fh = open("not.txt","r")
    print(1/0)
    print("上面无报错，程序正常运行了")
except (FileNotFoundError,ZeroDivisionError) as e:
    print(e)
else:
    print("没报错")
finally:
    print("不管程序有没有报错都会走这里")

print("git代码更新")