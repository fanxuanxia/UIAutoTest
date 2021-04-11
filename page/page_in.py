from page.page_mp_login import PageMpLogin
# noinspection PyUnresolvedReferences
from page.page_mp_article import PageMyArticle
from page.page_mis_login import PageMisLogin
from page.page_mis_audit import PageMisAudit
from page.page_app_login import PageAppLogin

class PageIn:
    def __init__(self, driver):
        self.driver = driver

    # 获取PageMpLogin对象
    def page_get_PageMpLogin(self):
        return PageMpLogin(self.driver)

    # 获取PageMpArticle对象
    def page_get_PageMpArticle(self):
        return PageMyArticle(self.driver)

    # 获取PageMisLogin对象
    def page_get_PageMislogin(self):
        return PageMisLogin(self.driver)

    # 获取PageMisAudit对象
    def page_get_PageMisAudit(self):
        return PageMisAudit(self.driver)

    # 获取PageAppLogin对象
    def page_get_PageAppLogin(self):
        return PageAppLogin(self.driver)