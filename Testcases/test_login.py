import unittest
import time
import ddt
from selenium import webdriver
from url_datas.global_datas import base_url
from op_datas import login_datas as ld
from PageObject.login_page import LoginPage
from yusuan_datas.Op_datas import Objectpage_datas as dd

# 登录

@ddt.ddt
class Test_Login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(base_url)
        cls.lp = LoginPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def tearDown(self):
        self.driver.refresh()
        print("用例执行完成")

    # 成功的用例
    def test_login_2_suc(self):
        self.lp.login_suc(ld.success["user"], ld.success["passwd"], ld.success["yzm"])
        time.sleep(5)




    # 异常的用例
    @ddt.data(*ld.wrong_datas)
    def test_login_1_err(self,datas):
        time.sleep(1)
        self.lp.login_suc(datas['user'],datas['passwd'],datas['yzm'])




