from selenium import webdriver
import appium.webdriver
import page
from time import sleep

class GetDriver:
    __web_driver = None
    __app_driver = None

    @classmethod
    def get_web_driver(cls,url):
        if cls.__web_driver is None:
            cls.__web_driver = webdriver.Chrome()
            cls.__web_driver.maximize_window()
            cls.__web_driver.get(url)
        return cls.__web_driver

    @classmethod
    def quit_web_driver(cls):
        if cls.__web_driver:
            cls.__web_driver.quit()
            # 这是重点，一定要清空。不置空的话，只有第一次才能成功。
            cls.__web_driver = None

    @classmethod
    def get_app_driver(cls):
        if cls.__app_driver is None:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '10'
            desired_caps['deviceName'] = '51ad332d'
            desired_caps['appPackage'] = page.appPackage
            desired_caps['appActivity'] = page.appActivity
            desired_caps['newCommandTimeout'] = 3600
            desired_caps['automationName'] = 'UiAutomator2'
            cls.__app_driver = appium.webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        return cls.__app_driver

    @classmethod
    def quit_app_driver(cls):
        if cls.__app_driver:
            cls.__app_driver.quit()
            cls.__app_driver = None

if __name__ == '__main__':
    GetDriver.get_app_driver()
    sleep(3)
    GetDriver.quit_app_driver()