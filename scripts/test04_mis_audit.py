from tools.get_driver import GetDriver
import page
from page.page_in import PageIn
from page.page_mis_audit import PageMisAudit

class TestMisAudit:
    def setup_class(self):
        self.driver = GetDriver.get_web_driver(page.url_mis)
        self.page_in = PageIn(self.driver)
        self.page_in.page_get_PageMislogin().page_mis_login_success()
        self.audit = self.page_in.page_get_PageMisAudit()

    def teardown_class(self):
        GetDriver.quit_web_driver()

    def test_mis_audit(self, title="test1002-1", channel="数据库"):
        self.audit.page_mis_audit(title, channel)
        if self.audit.page_assert_audit():
            print("审核成功")
        else:
            print("审核失败")

