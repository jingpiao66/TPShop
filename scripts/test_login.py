import pytest

from base.base_driver import init_driver
from page.page import Page
from base.base_analyze import analyze_with_file

class TestLogin:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    @pytest.mark.parametrize("args",analyze_with_file('login_data','test_login'))
    def test_login(self,args):

        self.page.home.click_mine_btn()
        self.page.mine.click_login_sign_up_btn()
        self.page.login.input_username(args['username'])
        self.page.login.input_pwd(args['password'])
        self.page.login.click_login_btn()
        assert self.page.login.is_toast_text(args['expect'])

    @pytest.mark.parametrize("args",analyze_with_file('login_data','test_login_miss_part'))
    def test_login_miss_part(self,args):

        self.page.home.click_mine_btn()
        self.page.mine.click_login_sign_up_btn()
        self.page.login.input_username(args['username'])
        self.page.login.input_pwd(args['password'])
        assert not self.page.login.is_login_btn_enabled()





