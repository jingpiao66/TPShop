import allure
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class LoginPage(BaseAction):

    username = By.ID, "com.tpshop.malls:id/edit_phone_num"
    pwd = By.ID, "com.tpshop.malls:id/edit_password"
    login_btn = By.ID, "com.tpshop.malls:id/btn_login"

    @allure.step(title="输入用户名")
    def input_username(self, text):
        self.input(self.username, text)

    @allure.step(title="输入密码")
    def input_pwd(self, password):
        self.input(self.pwd, password)

    @allure.step(title="点击登录按钮")
    def click_login_btn(self):
        self.click(self.login_btn)

    @allure.step(title="判断登录按钮是否可用")
    def is_login_btn_enabled(self):
        self.is_location_enabled(self.login_btn)
