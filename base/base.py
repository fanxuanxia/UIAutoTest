from selenium.webdriver.support.wait import WebDriverWait
import allure
from tools.get_log import GetLog
log = GetLog.get_logger()
class Base:
    #初始化
    def __init__(self, driver):
        log.info("正在初始化driver:{}".format(driver))
        self.driver = driver

    #查找 方法封装
    def base_find(self, loc, timeout=30, poll_frequency=0.5):
        """"
        loc 的格式为列表或者元组，内容 元素定位信息使用 By类
        """
        log.info("正在查找元素：{}".format(loc))
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency= poll_frequency).until(lambda x: x.find_element(*loc))

    #输入
    def base_input(self, loc, value):
        #获取元素
        el = self.base_find(loc)
        #清空操作
        log.info("正在清空")
        el.clear()
        # 输入
        log.info("正在输入:{} 到:{}".format(value, loc))
        el.send_keys(value)

    def base_click(self, loc):
        #获取元素并点击
        log.info("正在点击{}元素".format(loc))
        self.base_find(loc).click()

    #获取文本
    def base_get_text(self, loc):
        log.info("正在获取:{}的文本，获取的文本值：{}".format(loc, self.base_find(loc).text))
        return self.base_find(loc).text

    #截图方法
    def base_get_image(self):
        #1.调用截图方法
        log.error("断言出错，正在截图~")
        self.driver.get_screenshot_as_file("./image/err.png")

        #2.调用图片写入报告方法
        log.info("正在将错误图片写入报告~")
        self.__base_write_img()

    def __base_write_img(self):
        with open ("./image/err.png", 'rb') as f:
            # 调用allure.attach附加方法,三个参数分别为描述文字、文件和文件格式
            allure.attach("错误原因", f.read(), allure.attachment_type.PNG)
