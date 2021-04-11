# 测试页面对象层
from base.base import Base
import page
# noinspection PyUnresolvedReferences
from time import sleep
from tools.get_log import GetLog
log = GetLog.get_logger()

class PageMpLogin(Base):
    # 输入用户名
    def page_input_username(self, username):
        self.base_input(page.mp_username, username)
    # 输入验证码
    def page_input_code(self,code):
        self.base_input(page.mp_code, code)
    # 点击登录按钮
    def page_click_login_btn(self):
        sleep(1)
        self.base_click(page.mp_login_btn)
    # 获取昵称
    def page_get_nickname(self):
        return self.base_get_text(page.mp_nick_name)
    # 组合
    def page_mp_login(self,username, code):
        log.info("正在调用自媒体业务方法，登录的用户名为：{}，验证码为:{}".format(username, code))
        self.page_input_username(username)
        self.page_input_code(code)
        self.page_click_login_btn()
        self.page_get_nickname()

    def page_mp_login_success(self,username="13912345678", code="246811"):
        log.info("正在调用自媒体业务方法，登录的用户名为：{}，验证码为:{}".format(username, code))
        self.page_input_username(username)
        self.page_input_code(code)
        self.page_click_login_btn()





