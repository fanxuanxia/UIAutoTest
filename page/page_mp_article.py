from base.web_base import WebBase
import page
from selenium import webdriver
from time import  sleep
class PageMyArticle(WebBase):
    # 点击 内容管理
    def page_click_content_manage(self):
        sleep(1)
        self.base_click(page.mp_content_manage)
        pass
    # 点击 发布文章
    def page_click_publish_article(self):
        sleep(1)
        self.base_click(page.mp_publish_article)
    # 输入 标题
    def page_input_title(self,title):
        sleep(1)
        self.base_input(page.mp_title,title)
    # 输入 内容
    def page_input_content(self,content):
        sleep(1)
        iframe = self.base_find(page.mp_iframe)
        self.driver.switch_to.frame(iframe)
        self.base_input(page.mp_content,content)
        self.driver.switch_to.default_content()
    # 选择 封面
    def page_click_cover(self):
        sleep(1)
        self.base_click(page.mp_cover)

    # 选择 频道
    def page_click_channel(self):
        sleep(1)
        self.web_base_click_element(placeholder_text="请选择", click_text="数据库")
    # 点击 发表
    def page_click_submit(self):
        sleep(1)
        self.base_click(page.mp_submit)

    # 获取提示信息
    def page_get_info(self):
        return self.base_get_text(page.mp_result)
    # 组合 发布文章方法
    def page_my_article(self, title, content):
        self.page_click_content_manage()
        self.page_click_publish_article()
        self.page_input_title(title)
        self.page_input_content(content)
        self.page_click_cover()
        self.page_click_channel()
        self.page_click_submit()