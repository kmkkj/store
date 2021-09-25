from threading import Thread
egg_tart = 500
money = 3000

import time
class Producer(Thread):
    username = ""
    count = 0
    def run(self) -> None:
        global egg_tart, money
        while True:
            if 0 <= egg_tart < 500 and money > 0:
                self.count = self.count + 1
                egg_tart = egg_tart + 1
                print(self.username, "生产了", self.count, "个蛋挞","盘子里共有", egg_tart, "个蛋挞" )
            elif money == 0:
                print("结束")
                break
            elif egg_tart == 500:
                print("盘子里蛋挞满了！")
                time.sleep(3)


class Consumer(Thread):
    username = ""
    count1 = 0
    def run(self) -> None:
        global egg_tart, money
        while True:
            if money > 0:
                if egg_tart > 0:
                    money = money - 2
                    self.count1 = self.count1 + 1
                    egg_tart = egg_tart - 1
                    print(self.username,"一共买了",self.count1,"个蛋挞","钱包还剩",money,"元","盘子里还有",egg_tart,"个蛋挞")
                else :
                    print(self.username,"请稍等！蛋挞正在做......")
                    time.sleep(2)
                # break
            elif money == 0:
                print(self.username,"已经没钱了！")
                break



u1 =  Producer()
u1.username  = "生产者1号"

u2 =  Producer()
u2.username = "生产者2号"

u3 =  Producer()
u3.username = "生产者3号"

p1 = Consumer()
p1.username = "消费者1号"

p2 = Consumer()
p2.username = "消费者2号"

p3 = Consumer()
p3.username = "消费者3号"

p4 = Consumer()
p4.username = "消费者4号"

p5 = Consumer()
p5.username = "消费者5号"

p6 = Consumer()
p6.username = "消费者6号"

u1.start()
u2.start()
u3.start()
p1.start()
p2.start()
p3.start()
p4.start()
p5.start()
p6.start()


