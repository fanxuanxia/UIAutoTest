""""
谷歌浏览器通过F12进行元素定位，在按Ctrl+F进行校验
"""
from selenium.webdriver.common.by import By

"""以下数据为自媒体、后台管理URL"""
url_mp = "http://ttmp.research.itcast.cn/#/login"
url_mis = "http://ttmis.research.itcast.cn/#/"


"""以下数据为自媒体模块配置数据"""
# 用户名
mp_username = (By.CSS_SELECTOR, "[placeholder='请输入手机号']")
# 验证码
mp_code = (By.CSS_SELECTOR, "[placeholder='验证码']")
# 登录按钮
mp_login_btn = (By.CSS_SELECTOR, ".el-button--primary")
# 昵称
mp_nick_name = (By.CSS_SELECTOR, ".user-name")
# 内容管理
mp_content_manage = By.XPATH, "//span[text()='内容管理']/.."
# 发布文章
mp_publish_article =By.XPATH, "//*[contains(text(),'发布文章')]"
# 输入标题
mp_title = By.CSS_SELECTOR, "[placeholder='文章名称']"
# iframe
mp_iframe = By.CSS_SELECTOR, "#publishTinymce_ifr"
# 输入内容
mp_content = By.CSS_SELECTOR, "#tinymce"
# 封面自动
mp_cover = By.XPATH, "//*[text() = '自动']"
#发表
mp_submit = By.XPATH, "//*[text() = '发表']/.."
# 结果
mp_result = By.XPATH, "//*[contains(text(),'新增文章成功')]"

"""以下为后台管理系统配置数据"""
# 后台管理系统
mis_username = By.CSS_SELECTOR, "[placeholder='用户名']"
mis_psw = By.CSS_SELECTOR,"[placeholder='密码']"
mis_login_btn = By.CSS_SELECTOR, "#inp1"
mis_nickname = By.XPATH, "//*[contains(text(),'管理员')]"

#文章审核
mis_info_manage = By.XPATH, "//*[text()='信息管理']/."
mis_content_audit = By.XPATH, "//*[text()='内容审核']/."
mis_input_title = By.CSS_SELECTOR, "[placeholder='请输入: 文章名称']"
mis_input_channel = By.CSS_SELECTOR, "[placeholder='请输入: 频道']"
mis_find = By.CSS_SELECTOR, ".find"
mis_id = By.CSS_SELECTOR, ".cell>span"
mis_pass_btn = By.XPATH, "//*[text() = '通过']/.."
mis_confirm_btn = By.CSS_SELECTOR, ".el-button--primary"

"""以下为app配置信息"""
appPackage = "com.itcast.toutiaoApp"
appActivity = ".MainActivity"
app_phone_number = By.XPATH, "//*[@class ='android.widget.EditText' and @index='1']"
app_code = By.XPATH, "//*[@class ='android.widget.EditText' and @index='2']"
app_login_btn = By.XPATH, "//*[@class ='android.widget.Button']"
app_login_result = By.XPATH,"//*[@class ='android.widget.ImageView' and @index='3']"

