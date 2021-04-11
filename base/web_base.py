from base.base import Base
# noinspection PyUnresolvedReferences
from selenium.webdriver.common.by import By
from time import sleep
class WebBase(Base):
    def web_base_click_element(self, placeholder_text, click_text):
        # 1. 点击复选框
        loc = (By.CSS_SELECTOR, "[placeholder='{}']".format(placeholder_text))
        self.base_click(loc)
        # 2. 暂停，等待加载
        sleep(1)
        # 3. 点击元素
        loc = (By.XPATH, "//*[text()='{}']".format(click_text))
        self.base_click(loc)

    # 判断页面包含指定元素
    def web_base_is_exist(self, text):
        loc = By.XPATH, "//*[text()='{}']".format(text)

        try:
            self.base_find(loc, timeout=3)
            print("找到{}元素！".format(loc))
            return True
        except:
            print("未找到{}元素！".format(loc))
            return False

