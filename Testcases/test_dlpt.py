import unittest
import time
import ddt
from selenium import webdriver
from url_datas.global_datas import base_url
from op_datas.dlfw_input_data import Wycs_da as sj
from PageObject.dlpt_page import Ob_cxfw_dlpt

# 代理平台

@ddt.ddt
class Test_cxhfw(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(base_url)
        cls.lp = Ob_cxfw_dlpt(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def tearDown(self):
        self.driver.refresh()
        print("用例执行完成")

    # 成功的用例
    def test_cxhfw_1_suc(self):
        self.lp.dlpt_func(sj.sucess["user"], sj.sucess["passwd"], sj.sucess["yzm"],sj.sucess["dh1"],sj.sucess["dh2"],sj.sucess["dh3"],sj.sucess["lx1"],sj.sucess["lx2"]
                          , sj.sucess["lx3"],sj.sucess["dh4"],sj.sucess["lx4"],sj.sucess["lx5"],sj.sucess["lx6"],sj.sucess["gj"],sj.sucess["city"])
        time.sleep(3)
        # 断言
        # 定位退出按钮

