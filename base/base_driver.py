from appium import webdriver


def init_driver():
    # 前置代码
    desired_caps = dict()
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '192.168.56.101:5555'
    # app信息com.tpshop.malls/.SPMainActivity
    desired_caps['appPackage'] = 'com.tpshop.malls'
    desired_caps['appActivity'] = '.SPMainActivity'
    # 中文
    desired_caps['unicodekeyboard'] = True
    desired_caps['resetkeyboard'] = True
    # 获取toast
    desired_caps['automationName'] = 'Uiautomator2'

    return webdriver.Remote('http://192.168.22.68:4723/wd/hub', desired_caps)
