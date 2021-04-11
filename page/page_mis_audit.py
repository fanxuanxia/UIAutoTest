from base.web_base import WebBase
from time import sleep
import page

class PageMisAudit(WebBase):
    article_id = None

    #点击信息管理
    def page_click_info_manage(self):
        sleep(1)
        self.base_click(page.mis_info_manage)

    #点击内容审核
    def page_click_content_audit(self):
        sleep(1)
        self.base_click(page.mis_content_audit)

    # 输入标题
    def page_input_title(self, title):
        self.base_input(page.mis_input_title, title)

    # 输入频道
    def page_input_channel(self, channel):
        self.base_input(page.mis_input_channel, channel)

    # 选择 状态  待审核
    def page_choose_statues(self, placeholder="请选择状态", click_text="待审核"):
        self.web_base_click_element(placeholder, click_text)

    # 点击查询按钮
    def page_find(self):
        self.base_click(page.mis_find)
        sleep(1)

    def page_get_article_id(self):
        sleep(1)
        return self.base_get_text(page.mis_id)

    # 点击通过
    def page_click_pass_btn(self):
        self.base_click(page.mis_pass_btn)

    # 点击确认
    def page_click_confirm_btn(self):
        sleep(1)
        self.base_click(page.mis_confirm_btn)

    def page_mis_audit(self, title, channel):
        self.page_click_info_manage()
        self.page_click_content_audit()
        self.page_input_title(title)
        self.page_input_channel(channel)
        self.page_choose_statues()
        self.page_find()
        self.article_id = self.page_get_article_id()
        print("获取的文章ID为：", self.article_id)
        self.page_click_pass_btn()
        self.page_click_confirm_btn()

    def page_assert_audit(self):
        sleep(3)
        self.page_choose_statues(click_text="审核通过")
        sleep(1)
        self.page_find()
        sleep(2)
        return self.web_base_is_exist(self.article_id)