l = [1,2,3]
l[0] = 333
print(l[0])

p = (1,3,6)
print(p[0])

s = {1,9,9,8}
print(s)

a = 20
b = "2.9"
print(a + float(b))

pp = {"name":"哈哈哈","age":19}
print(pp["name"])
print(pp)


nums = [40, 36, 89, 2, 36, 100, 7, -20.5, 36]
print("36出现了%d%s次" % (nums.count(36), nums.count(36)))




def demo(obj) :
    obj += obj
    print("形参值为：",obj)

print("-------值传递-----")
a = "C语言中文网"
print("a的值为：",a)
demo(a)
print("实参值为：",a)

print("-----引用传递-----")
a = [1,2,3]
print("a的值为：",a)
demo(a)
print("实参值为：",a)

b = []
print(b)#　输出：[]
print(id(b))


add = "http://c.biancheng.net/python/"
#for循环，遍历 add 字符串
for ch in range(len(add)):
    # print(ch,end="")
    print(ch, end="|")

# my_list = [1,2,3,4,5]
# for ele in my_list:
#     print('ele =', ele, end="|")
#
# for i in range(100):
#     print("顺序：%d，index：%d"%(i,i+1),end="\n")
#
# i = 0
# while i < 2:
#     print("循环次数：%d" %(i))
#     i += 1
#
# print(list(range(10)))
# print(set(range(1,10)))
# print(tuple(range(1,10,2)))
# print(tuple(range(-5,-1,1)))


score = 800
if (score > 80):
    assert score > 80
print("\n%s"%score)

count = 0
for i in range(1,101):
    count += i
    if i == 100:
        print(count)

for i in range(1, 101):
    if (i%7 == 0 or i%10 == 7):
        print(i)


print("-----------------冒泡排序--------------------------")
myList  = [3,4,5,1,99,56,7]
for i in range(len(myList)):
    for j in range(len(myList) - i -1):
        if myList[j] < myList[j+1]:
            myList[j],myList[j+1] = myList[j+1],myList[j]
print(myList)

print("-----------------内置排序--------------------------")
myList2 = [3,4,5,1,99,56,7]
myList2.sort()
print(myList2)

myList3 = [3,4,5,1,99,56,7]
sorted(myList3)
print(sorted(myList3,reverse=True))

print("-----------------乘法表--------------------------")
# for i in range(1,10):
#     for j in range(1,10):
#         print("%d*%d=%d"%(i,j,i*j),end="\t")
#         # print("{}*{}={}".format(i,j,i*j),end="\t")
#         if (i <= j):
#             break
#     print("")

for i in range(1,10):
    for j in range(1,i+1):
        print("%d*%d=%d"%(i,j,i*j),end="\t")
        # print("{}*{}={}".format(i,j,i*j),end="\t")
        if (i <= j):
            break
    print("")

def test(a=1,b=7):
    c = a+b
    print(c)
test(1,b=7)
test(1,b=7)

def test2(a,*arg,b=10,**kargs):
    print(a)
    print(arg)
    print(b)
    print(kargs)

test2(1,1,2,3,b=3,hh="n",jj = "ggg")

print(isinstance(1,int))

# file = open("hhh.txt","w")
# file.write("jjjjjjjjjjjjjjjj")
# file.close()
#
# file = open("hhh.txt","r")
# print(file.read())
# file.close()

#定义一个比较字符串大小的函数
def str_max(str1,str2):
    '''
    比较 2 个字符串的大小
    '''
    str = str1 if str1 > str2 else str2
    return str
help(str_max)
#print(str_max.__doc__)

a=lambda x:x*x
print(a(3))

print("------------------------闭包函数---------------------------")
def nth_power(exponent):
    def exponent_of(base):
        return base ** exponent
    return exponent_of # 返回值是 exponent_of 函数
square = nth_power(2) # 计算一个数的平方
cube = nth_power(3) # 计算一个数的立方

print(square(2))  # 计算 2 的平方
print(cube(2)) # 计算 2 的立方

print(nth_power(2)(2))  # 计算 2 的平方
print(nth_power(3)(2)) # 计算 2 的立方


class Person:
    def who(self):
        print("哈哈哈哈哈哈哈哈哈")
zhangsan = Person()
#第一种方式
zhangsan.who()
#第二种方式
who = zhangsan.who
who()#通过 who 变量调用zhangsan对象中的 who() 方法


print("\n--------------------------方法调用测试(start)-----------------------")
class testFun():
    def __init__(self):
        print("构造方法")

    def shiliFun(self):
        print("实例化方法")

    @classmethod
    def clsFun(cls):
        print("类方法")

    @staticmethod
    def staticFun():
        print("静态方法")

testFun()
testFun().shiliFun()
testFun.clsFun()

testFun.staticFun()
testFun().staticFun()
print("--------------------------方法调用测试(end)-----------------------")


class Parent():

    def __init__(self,a):
        self.a = a

    first_name = "王"
    __second_name = "五"

    @classmethod
    def name(cls):
        print("我叫" + cls.first_name + cls.__second_name)

    def ji_neng(self):
        print("锁匠")


class Son(Parent):

    # def __init__(self,a,b):
    #     super().__init__(a)
    #     self.b = b

    __second_name = "八"

    @classmethod
    def name(cls):
        print("我叫" + cls.first_name + cls.__second_name)

son = Son(1)
son.name()
son.ji_neng()



# p = Parent(19)
# print(p.a)
# s = Son(1)
# print(s.a)