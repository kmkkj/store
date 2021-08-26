# 实现输入10个数字，并打印10个数的求和结果
a = []
for i in range(0,10):
    m = input("请输入一个整数：")
    a.append(int(m))
for i in a:
    print(i,end="")
print()
s = sum(a)
print("元素的和为：",s)

# 从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数
a = []
for i in range(0,10):
    m = input("请输入一个整数：")
    a.append(int(m))
for i in a:
    print(i,end="")
print()
m1 = max(a)
print("最大的数为：",m1)
s = sum(a)
print("元素的和为：",s)
a1 = s/10
print("平均数为：",a1)

# 使用random模块，如何产生 50~150之间的数
import random
num=random.randint(50, 150)
print(num)

# 从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形（结果判断：等腰，等边，直角，普通，不能形成三角形。）
a = int(input("请输入一个边长a"))
b = int(input("请输入一个边长b"))
c = int(input("请输入一个边长c"))
while 1:
    if a + b < c or a + c < b or c + b < a:
        print("不能构成三角形")
        break
    if a == b == c:
        print("等边三角形")
    elif a == b or a == c or b == c:
        print("等腰三角形")
    elif a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a:
        print("直角三角形")
    elif a + b > c and a + c > b and b + c > a:
        print("普通三角形")
    break

# 有以下两个数，使用+，-号实现两个数的调换。A=56  B=78  实现效果：A=78  B=56
A=56
B=78
S=A+B
A=S-A
B=S-B
print("(A,B)=",A,B)

# 实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）
count = 0
username = "root"
userpassword = "admin"
name = input("登录用户名：")
if name == username:
    while count < 3:
        password = input("登录密码：")
        if password == userpassword:
            print("欢迎登录!")
            break
        else:
            print("账号和密码不匹配")
            count += 1
    else:
        print("对不起，您的账号连续输错三次密码已被锁定")

# 打印三角形
for i in range(8):
    for j in range(0, 8 - i):
        print(end=" ")
    for k in range(8 - i, 8):
        print("*", end=" ")
    print("")

# 使用while循环实现99乘法表的打印
a = 1
while a <= 9:
    b = 1
    while b <= a:
        print("%d*%d=%d\t" % (b, a, a * b), end="")
        b += 1
    print("")
    a += 1

# 编程实现99乘法表的倒叙打印
for i in range(9,0,-1):
    for j in range(1,i+1):
        print('%d*%d=%2d\t' % (j, i, i * j), end='')
    print() # 此处的目的主要是利用print特性换行

# 一只青蛙掉在井里了，井高20米，青蛙白天网上爬3米，晚上下滑2米，问第几天能出来？请编程求出。
jing = -20
up = 3
down = -2
num = 1
while jing < 0:
	print("day",num,end="   ")
	jing+=up
	print("up",jing,end="   ")
	if jing >= 0:
		break
	jing+=down
	print("down",jing)
	if jing >= 0:
		break
	num+=1

# 用循环来实现20以内的数的阶乘。（1! +2!+3!+…..+20!）
import math
Sum=0
num = int(input('请输入一个数字：'))
for i in range(1,num+1):
    F=math.factorial(i)
    Sum +=F
print('阶乘之和：',Sum)



