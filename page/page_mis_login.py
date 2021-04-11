from base.web_base import WebBase
import page
from time import sleep
# noinspection PyUnresolvedReferences
from selenium import webdriver
from tools.get_log import GetLog
log = GetLog.get_logger()

class PageMisLogin(WebBase):
    def mis_input_username(self,username):
        sleep(1)
        self.base_input(page.mis_username, username)

    def mis_input_psw(self,psw):
        sleep(1)
        self.base_input(page.mis_psw, psw)

    def mis_click_login(self):
        js = "document.getElementById('inp1').disabled = false"
        self.driver.execute_script(js)
        sleep(1)
        self.base_click(page.mis_login_btn)
    def mis_get_nickname(self):
        sleep(1)
        return self.base_get_text(page.mis_nickname)

    def page_mis_login(self,username, psw):
        self.mis_input_username(username)
        self.mis_input_psw(psw)
        self.mis_click_login()

    def page_mis_login_success(self, username="testid", pwd="testpwd123"):
        log.info("正在调用自后台管理系统自动登录依赖方法，登录的用户名为：{}，验证码为:{}".format(username, pwd))
        self.mis_input_username(username)
        self.mis_input_psw(pwd)
        self.mis_click_login()

