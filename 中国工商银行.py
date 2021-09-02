import random
print("==============================================")
print("|------------中国工商银行账户管理系统------------|")
print("|------------1、开户              ------------|")
print("|------------2、取钱              ------------|")
print("|------------3、存钱              ------------|")
print("|------------4、转账              ------------|")
print("|------------5、查询              ------------|")
print("|------------6、退出              ------------|")
print("==============================================")
bank={}
bank_name="掌上银行"
def bank_adduser(account,username,password,country,province,street,door):
    if len(bank) >100:
        return 3
    if account in bank:
        return 2
    bank[account]={
         "username":username,
         "password":password,
         "country":country,
         "province":province,
         "street":street,
         "door":door,
         "money":0,
         "bank_name":bank_name
     }
    return 1

# 添加用户
def adduser():
    username=input("请输入您的用户名")
    password = input("请输入您的密码")
    print("请输入您的地址")
    country=input("\t\t请输入您的国家")
    province=input("\t\t请输入您的省份")
    street=input("\t\t请输入您的街道")
    door=input("\t\t请输入您的门牌号")
    account=random.randint(10000000,99999999)
    stast=bank_adduser(account,username,password,country,province,street,door)
    if stast == 3:
        print("你去别的银行吧")
    elif stast == 2:
        print("开户失败，你别重复")
    elif stast == 1:
        info = '''
                    ------------个人信息------------
                    用户名:%s
                    账号：%s
                    密码：*****
                    国籍：%s
                    省份：%s
                    街道：%s
                    门牌号：%s
                    余额：%s
                    开户行名称：%s
                '''
        print(info % (username, account, country, province, street, door, bank[account]["money"], bank_name))
#{'frank': {'account': 88474479, 'password': '1234', 'country': '1', 'province': '1', 'street': '1', 'door': '1', 'money': 0, 'bank_name': '狼腾测试猿银行'}}

# 存钱
def savemoney():
    while True:
        account = int(input("请输入您的账号:"))
        if account in bank :
            password = input("请输入您的密码：")
            if password == bank[account]["password"]:
                money = int(input("请输入存款金额:"))
                bank[account]["money"] = int(bank[account]["money"])
                bank[account]["money"] = bank[account]["money"] + money
                print("余额为：", bank[account]["money"])
            else :
                print("密码错误！")
        else :
            return False
        break

# 取钱
def drawmoney():
    while True:
        account = int(input("请输入您的账号:"))
        if account in bank:
            password = input("请输入您的密码：")
            if password == bank[account]["password"]:
                drawmoney = int(input("请输入要取的金额："))
                bank[account]["money"] = int(bank[account]["money"])
                if drawmoney <= bank[account]["money"]:
                    bank[account]["money"] = bank[account]["money"] - drawmoney
                    print("余额为：", bank[account]["money"])
                else :
                    print("余额不足！")
            else :
                print("密码不正确！")
        else :
            print("该用户不存在！")
        break

# 转账
def transfer():
    out_account = int(input("请输入转出的账号:"))
    in_account = int(input("请输入转入的账号:"))
    if out_account and in_account in bank:
        out_password = input("请输入转出账户密码：")
        if out_password == bank[out_account]["password"]:
            out_money = int(input("请输入转出的金额："))
            bank[out_account]["money"] = int(bank[out_account]["money"])
            if out_money <= bank[out_account]["money"]:
                bank[out_account]["money"] = bank[out_account]["money"] - out_money
                bank[in_account]["money"] = bank[in_account]["money"] + out_money
                print("转出账户余额为：",bank[out_account]["money"])
                print("转入账户余额为：",bank[in_account]["money"])
            else:
                print("余额不足！")
        else:
            print("密码不正确！")
    else:
        print("用户不存在！")

# 查询账户
def select():
    while True:
        account = int(input("请输入您的账号:"))
        if account in bank :
            password = input("请输入您的密码：")
            if password == bank[account]["password"]:
                print("账户信息:",bank[account])
            else :
                print("密码错误！")
        else :
            print("该用户不存在！")
        break

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