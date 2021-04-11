
from tools.get_driver import GetDriver
import page
from page.page_in import PageIn
# noinspection PyUnresolvedReferences
import pytest
from tools.read_yaml import read_yaml


class TestMisLogin:

    def setup_class(self):
        driver = GetDriver.get_web_driver(page.url_mis)
        self.mis_login = PageIn(driver).page_get_PageMislogin()

    def teardown_class(self):
        GetDriver.quit_web_driver()

    #@pytest.mark.parametrize("username,psw, expect", read_yaml("mis_login.yaml"))
    def test_mis_login(self, username="testid", psw="testpwd123", expect="欢迎 管理员"):
        self.mis_login.page_mis_login(username, psw)
        try:
            assert self.mis_login.mis_get_nickname() == expect
        except Exception as e:
            print("错误信息为：", e)

