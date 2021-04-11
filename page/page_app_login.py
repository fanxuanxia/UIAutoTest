from base.app_base import AppBase
import page
from time import sleep
class PageAppLogin(AppBase):
    def page_input_phone_number(self, phone_number):
        print("等待3秒开始执行输入")
        sleep(3)
        self.base_input(page.app_phone_number, phone_number)
        print("已输入手机号")

    def page_input_code(self,code):
        print("等待3秒开始执行输入")
        sleep(3)
        self.base_input(page.app_code, code)
        print("已输入验证码")

    def page_click_login_btn(self):
        sleep(5)
        self.base_click(page.app_login_btn)

    def page_is_login_success(self):
        sleep(5)
        return self.app_base_is_exit(page.app_login_result)

    def page_app_login(self, phone_number, code):
        self.page_input_code(code)
        self.page_input_phone_number(phone_number)
        self.page_click_login_btn()