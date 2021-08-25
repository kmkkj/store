'''
猜字游戏
需求：
1、猜的数字是系统产生的，不是自己定义的
2、键盘输入的   操作完填入：input（“提示”）
3、判断			操作完填入：if判断条件 elif 判断条件。。。。。。Else
4、循环			操作完填入：while 条件循环
任务：你的初始资金为100 每猜一次减10  资金为0时或者猜成功游戏结束
    猜大 如果你输入的数字和随机数对比 大于随机数  打印一句话为  猜大了
    猜小 如果你输入的数字和随机数对比 小于随机数  打印一句话为  猜小了
'''
import random
num=random.randint(0, 1000)
i = 100
while 1:
    i = int(i)
    a = input("请输入一个数字")
    a = int(a)
    if a > num:
        print("猜大了")
    elif a < num:
        print("猜小了")
    i = i - 10
    print("初始值剩余", i)
    if  a == num :
        print("游戏结束",a)
        break
    elif i == 0:
        print("游戏结束",a)
        break
