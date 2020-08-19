from selenium import webdriver
import time
import random

def auto_healthreport(name, passwd):
    #打开综合服务大厅
    opt = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=opt)
    driver.get('http://one.xjtu.edu.cn/EIP/nonlogin/user/index.htm')
    #最大化窗口
    driver.maximize_window()
    time.sleep(3)
    #找到登录按钮
    driver.find_element_by_xpath("//a[@class='login-btn']").click()
    time.sleep(3)

    #输入用户名和密码
    driver.find_element_by_xpath("//input[@type='text']").click()
    driver.find_element_by_xpath("//input[@type='text']").send_keys(name)
    driver.find_element_by_xpath("//input[@type='password']").click()
    driver.find_element_by_xpath("//input[@type='password']").send_keys(passwd)
    driver.find_element_by_xpath("//div[@class='login_btn account_login']").click()
    time.sleep(3)

    #登陆成功，跳转到综合服务大厅
    driver.get('http://jkrb.xjtu.edu.cn/EIP/user/index.htm')
    time.sleep(3)
    #有坑，网站嵌套了iframe，需要一层层进入iframe，最终才能点击
    iframelist = []
    iframe = driver.find_element_by_xpath("//*[@id='mini-17$body$2']/iframe")
    iframelist.append(iframe)
    driver.switch_to.frame(iframelist[0])
    iframe = driver.find_element_by_xpath("//*[@id='ab0ab54c0e7048a7b583d5c1c8da7c06']/div/div[2]/div[2]/iframe")
    iframelist.append(iframe)
    driver.switch_to.frame(iframelist[1])
    #点击 ‘本科生每日健康状况填报’
    driver.find_element_by_xpath("//*[@id='form']/div[2]/div/ul[1]/li[2]/div").click()
    time.sleep(3)
    #焦点切换回默认frame
    driver.switch_to.default_content()
    iframe = driver.find_element_by_xpath("//*[@id='mini-17$body$3']/iframe")
    iframelist.append(iframe)
    driver.switch_to.frame(iframelist[2])
    #点击‘返校登记后每日健康填报’
    driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/ul/li[2]/span[1]").click()
    time.sleep(3)

    #开始填写表单 焦点切换回默认frame
    driver.switch_to.default_content()
    iframe = driver.find_element_by_xpath("//*[@id='mini-17$body$4']/iframe")
    iframelist.append(iframe)
    driver.switch_to.frame(iframelist[3])
    iframe = driver.find_element_by_xpath("//*[@id='mini-14$body$2']/iframe")
    iframelist.append(iframe)
    driver.switch_to.frame(iframelist[4])
    #点击健康码为绿色
    driver.find_element_by_xpath("//*[@id='mini-2$ck$2']").click()
    #填写今日体温
    temperature = 36 + random.randint(5, 7) * 0.1
    #随机生成36.5~36.7之间的体温
    driver.find_element_by_xpath("//*[@id='BRTW$text']").send_keys(str(temperature))

    #填写完毕 提交按钮在第三层iframe上，我们现在在第四层iframe，因此回到这一层的父层
    driver.switch_to.parent_frame()
    #点击提交按钮
    driver.find_element_by_xpath("//*[@id='sendBtn']").click()
    driver.find_element_by_xpath("//*[@id='mini-17']/span").click()

    time.sleep(5)

if __name__ == '__main__':
    #用户名和密码
    name = '用户名'
    passwd = '密码'
    auto_healthreport(name,passwd)