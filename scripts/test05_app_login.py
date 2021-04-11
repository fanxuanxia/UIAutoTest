from tools.get_driver import GetDriver
from page.page_in import PageIn
# noinspection PyUnresolvedReferences
from page.page_app_login import PageAppLogin
import pytest
from tools.read_yaml import read_yaml

class TestAppLogin:

    def setup_class(self):
        driver = GetDriver.get_app_driver()
        if driver is None:
            print("获取driver失败")
        self.app_login = PageIn(driver).page_get_PageAppLogin()

    def teardown_class(self):
        GetDriver.quit_app_driver()

    @pytest.mark.parametrize("phone_number, code", read_yaml("app_login.yaml"))
    def test_app_login(self, phone_number, code):
        self.app_login.page_app_login(phone_number, code)
        if self.app_login.app_base_is_exit():
            print("登录成功！")

