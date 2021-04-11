from tools.get_driver import GetDriver
import page
from page.page_in import PageIn

class TestMpArticle():
    def setup(self):
        self.driver = GetDriver.get_web_driver(page.url_mp)
        self.page_in = PageIn(self.driver)
        self.page_in.page_get_PageMpLogin().page_mp_login_success()
        self.article = self.page_in.page_get_PageMpArticle()

    def teardown(self):
        GetDriver.quit_web_driver()

    def test_mp_article(self, title = "test10001", content = "hahaha"):
        self.article.page_my_article(title, content)


