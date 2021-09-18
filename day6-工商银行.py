import random
import pymysql
import cursor

bank_name = "中国工商银行的昌平支行"
print("==============================================")
print("|------------中国工商银行账户管理系统------------|")
print("|------------1、开户              ------------|")
print("|------------2、取钱              ------------|")
print("|------------3、存钱              ------------|")
print("|------------4、转账              ------------|")
print("|------------5、查询              ------------|")
print("|------------6、退出              ------------|")
print("==============================================")

con = pymysql.connect(host="localhost",user='root',password='',database='bank')
cursor = con.cursor()

def bank_adduser(account, username, password, country, province, street, door):
    sql = "select count(*) from  data"
    cursor.execute(sql)
    infor = cursor.fetchall()
    if infor[0][0] >= 100:
        return 3
    else:
        # 查询数据库是否存在该用户
        sql1 = "select * from data where account = %s"
        param = [account]
        cursor.execute(sql1, param)
        infor1 = cursor.fetchall()
        if len(infor1) != 0:
            return 2  # 已存在
        else:  # 正常开户：存储到银行 ，插入数据库
            sql2 = "insert into data values(%s,%s,%s,%s,%s,%s,%s,%s,now(),%s)"
            param2 = [account,username,password,country,province,street,door,0,bank_name]
            cursor.execute(sql2, param2)
            con.commit()
            return 1

def adduser():
    username=input("请输入您的用户名")
    password = input("请输入您的密码")
    print("请输入您的地址")
    country=input("\t\t请输入您的国家")
    province=input("\t\t请输入您的省份")
    street=input("\t\t请输入您的街道")
    door=input("\t\t请输入您的门牌号")
    while True:
        account=random.randint(10000000,99999999)
        cursor = con.cursor()
        sql_adduser = "select account from data"
        cursor.execute(sql_adduser)
        infor = cursor.fetchall()
        if account not in infor:
            break
        cursor.close()
    stast=bank_adduser(account, username, password, country, province, street, door)
    if stast == 3:
        print("你去别的银行吧")
    elif stast == 2:
        print("开户失败，你别重复")
    elif stast == 1:
        info = '''
                                                ------------个人信息------------
                                                账号：%s
                                                用户名:%s
                                                密码：*****
                                                地址：%s%s%s%s
                                                余额：%s
                                                开户行名称：%s
                                                --------------------------------
                                                                                  '''
        print(info % (account,username, country, province, street, door, 0, bank_name))
# 存钱
def savemoney():
    account = input("请输入您的账号:")
    account = int(account)
    sql = "select * from data where account = %s"
    param = [account]
    cursor.execute(sql,param)
    infor = cursor.fetchone()
    if infor is None:
        return False
    else:
        sql = "select * from data where account = %s"
        param = [account]
        cursor.execute(sql,param)
        infor1 = cursor.fetchone()
        for i in range(3):
            password = input("请输入您的密码: ")
            if password == infor1[2]:
                print("金额为: ", infor1[7])
                break
            else:
                print("密码错误!")
    savemoney = int(input("请输入存款金额:"))
    money = int(infor1[7]) + savemoney
    sql = "UPDATE data SET money = '%s' WHERE account = '%s'"
    param = [money,account]
    cursor.execute(sql,param)
    con.commit()
    print("余额为：%s元" % (money))

# 取钱
def drawmoney():
    account = input("请输入您的账号:")
    account = int(account)
    sql = "select * from data where account = %s"
    param = [account]
    cursor.execute(sql, param)
    infor = cursor.fetchone()
    if infor is None:
        print("该用户不存在！")
    else:
        sql = "select * from data where account = %s"
        param = [account]
        cursor.execute(sql, param)
        infor1 = cursor.fetchone()
        for i in range(3):
            password = input("请输入您的密码: ")
            if password == infor1[2]:
                print("金额为: ", infor1[7])
                break
            else:
                print("密码不正确!")
    drawmoney = int(input("请输入要取的金额:"))
    if drawmoney <= infor1[7]:
        money = int(infor1[7]) - drawmoney
        sql = "UPDATE data SET money = '%s' WHERE account = '%s'"
        param = [money, account]
        cursor.execute(sql, param)
        con.commit()
        print("余额为：%s元" % (money))
    else:
        print("余额不足！")


# 转账
def transfer():
    out_account = int(input("请输入转出的账号:"))
    sql = "select * from data where account = %s"
    param = [out_account]
    cursor.execute(sql, param)
    out_infor = cursor.fetchone()
    in_account = int(input("请输入转入的账号:"))
    sql = "select * from data where account = %s"
    param = [in_account]
    cursor.execute(sql, param)
    in_infor = cursor.fetchone()
    if out_infor and in_infor is None:
        print("用户不存在！")
    else:
        sql = "select * from data where account = %s"
        param = [out_account]
        cursor.execute(sql, param)
        out_infor1 = cursor.fetchone()
        sql = "select * from data where account = %s"
        param = [in_account]
        cursor.execute(sql, param)
        in_infor1 = cursor.fetchone()
        for i in range(3):
            out_password = input("请输入转出账户密码: ")
            if out_password == out_infor1[2]:
                myhave_money = int(out_infor1[7])
                hishave_money = int(in_infor1[7])
                print("金额为: ", myhave_money)
                break
            else:
                print("密码不正确!")
    out_money = int(input("请输入转出的金额:"))
    if out_money <= myhave_money:
        my_money = myhave_money - out_money
        his_money = hishave_money + out_money
        sql = "UPDATE data SET money = '%s' WHERE account = '%s'"
        param = [my_money, out_account]
        cursor.execute(sql, param)
        con.commit()
        sql = "UPDATE data SET money = '%s' WHERE account = '%s'"
        param = [his_money, in_account]
        cursor.execute(sql, param)
        con.commit()
        print("余额为：%s元" % (my_money))
    else:
        print("余额不足！")

# 查询账户
def select():
    account = input("请输入您的账号:")
    account = int(account)
    sql = "select * from data where account = %s"
    param = [account]
    cursor.execute(sql,param)
    infor = cursor.fetchall()
    if infor is None:
        print("该用户不存在!")
    else:
        sql = "select * from data where account = %s"
        param = [account]
        cursor.execute(sql,param)
        infor1 = cursor.fetchone()
        for i in range(3):
            password = input("请输入您的密码: ")
            if password == infor1[2]:
                info = '''
                                        ------------个人信息------------
                                        账号：%s
                                        用户名:%s
                                        密码：*****
                                        地址：%s%s%s%s
                                        余额：%s
                                        开户行名称：%s
                                        --------------------------------
                                                                          '''
                print(info % (infor1[0],infor1[1],infor1[3],infor1[4],infor1[5],infor1[6],infor1[7],infor1[9]))
                break
            else:
                print("密码错误!")

while True:
    begin = input("请选择业务")
    if begin =="1":
        adduser()
    elif begin == "2":
        drawmoney()
    elif begin == "3":
        savemoney()
    elif begin == "4":
        transfer()
    elif begin == "5":
        select()
    else:
        print(6,"、退出")
        break