# 测试脚本业务层
from tools.get_driver import GetDriver
from page.page_in import PageIn
import page.page_mp_login
import page
# noinspection PyUnresolvedReferences
import pytest
# noinspection PyUnresolvedReferences
from tools.read_yaml import read_yaml
from tools.get_log import GetLog
log = GetLog.get_logger()

class TestMpLogin:
    # 初始化
    def setup_class(self):
        driver = GetDriver.get_web_driver(page.url_mp)
        # 通过统一入口类获取PageMpLogin对象
        self.mp = PageIn(driver).page_get_PageMpLogin()

    # 结束
    def teardown_class(self):
        GetDriver.quit_web_driver()

    # 测试
    @pytest.mark.parametrize("username,code, expect", read_yaml("mp_login.yaml"))
    def test_mp_login(self, username, code, expect):
        print("test")
        self.mp.page_mp_login(username, code)
        try:
            #断言
            assert expect == self.mp .page_get_nickname()
        except Exception as e:
            #输出错误信息
            log.error("断言出错，错误信息：{}".format(e))
            print("错误原因：", e)
            #截图
            self.mp.base_get_image()
            #抛异常
            raise
