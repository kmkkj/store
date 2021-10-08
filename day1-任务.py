'''
    任务1：百度上搜索点击
       2:滑动验证其他的都用自动化来做
       3.京东搜索一个商品，点击详情。
'''
# 百度上搜索点击
# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")
# driver.maximize_window()
# driver.find_element_by_id("kw").send_keys("北京冬奥会")
# driver.find_element_by_id("su").click()
# time.sleep(2)
# driver.quit()

# 弹框验证
# import time
# from  selenium import webdriver
# driver = webdriver.Chrome()
# driver.get(r"F:\资料-汉科软\自动化搭建\练习的html\练习的html\弹框的验证/dialogs.html")
# driver.maximize_window()
# driver.find_element_by_xpath("//*[@id='confirm']").click()
# driver.switch_to.alert.dismiss() # 取消
#                     # accept()  确定
# time.sleep(2)
# driver.quit()

#上传文件和下拉列表
# from selenium import webdriver
# import time
# driver = webdriver.Chrome()
# driver.get(r"F:\资料-汉科软\自动化搭建\练习的html\练习的html\上传文件和下拉列表/autotest.html")
# driver.maximize_window()
# # 输入用户名
# driver.find_element_by_xpath("//*[@id='accountID']").send_keys("张三")
# driver.find_element_by_xpath("//*[@id='passwordID']").send_keys("123456")
# driver.find_element_by_xpath("//*[@id='areaID']").send_keys("北京市")
# time.sleep(1)
# driver.find_element_by_xpath("//*[@id='sexID2']").click()
# driver.find_element_by_xpath("//*[@value='spring']").click()
# driver.find_element_by_xpath("//*[@value='Auterm']").click()
# # 上传文件
# driver.find_element_by_xpath("//*[@name='file' and @type='file']").send_keys(r"C:\Users\think\Pictures\Saved Pictures\我问问.jpg")
# driver.find_element_by_xpath("//*[@id='buttonID']").click()
# driver.switch_to.alert.accept()
# time.sleep(2)
# driver.quit()

#跳转页面
# from selenium import webdriver
# import time
# driver = webdriver.Chrome()
# driver.get(r"F:\资料-汉科软\自动化搭建\练习的html\练习的html\跳转页面/pop.html")
# driver.maximize_window()
# driver.find_element_by_xpath("//*[@id='goo']").click()
# time.sleep(2)
# driver.quit()


# 京东搜索一个商品，点击详情
# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("https://www.jd.com")
# driver.maximize_window()
# driver.find_element_by_xpath("//*[@id='key']").send_keys("iphone13 pro")
# driver.find_element_by_xpath("//*[@class='button']").click()
# time.sleep(3)
# driver.find_element_by_xpath("//*[@id='J_goodsList']/ul/li[1]/div/div[1]/a/img").click()
# new_windows = driver.window_handles[-1]
# driver.switch_to.window(new_windows)
# time.sleep(2)
# driver.quit()


# import time
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
#
# wd = webdriver.Chrome()
# wd.get("http://www.jd.com")
# wd.maximize_window()
#
# wd.find_element_by_xpath("//*[@id='key']").send_keys("大黄蜂手办")
# wd.find_element_by_xpath("//*[@id='search']/div/div[2]/button").click()
#
# image = wd.find_element_by_xpath("//*[@id='J_goodsList']/ul/li[1]/div/div[1]/a/img")
# ActionChains(wd).click(image).perform()
#
# time.sleep(10)
# wd.quit()
