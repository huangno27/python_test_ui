import unittest
import time
import ddt
from selenium import webdriver
from url_datas.global_datas import base_url
from op_datas.schd_input_data import Wycs_da as sj
from PageObject.schd_page import Ob_cxfw_one

# 查询和服务->我要查询

@ddt.ddt
class Test_cxhfw(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(base_url)
        cls.lp = Ob_cxfw_one(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def tearDown(self):
        self.driver.refresh()
        print("用例执行完成")

    # 成功的用例
    def test_cxhfw_1_suc(self):
        self.lp.cxhfw_func1(sj.sucess["user"], sj.sucess["passwd"], sj.sucess["yzm"])
        time.sleep(3)
        # 断言
        # 定位退出按钮
